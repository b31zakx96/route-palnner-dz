from flask import Flask, request, json
import pymongo
import pprint
import json
import re
from flask_cors import CORS

############-Initializing-################################################################################################
type_error = [ 'lieu-dit', 'sécurité et protection', 'santé', 'justice', 'administration','autre','service','education/enseignement', 'hotels', 'restauration','banque','sport']
type_comp = ["Organisme","Nom de lieu-dit","Numéro","Unité de batiment","Voie","Zone","Boite postale","Localité"]


app = Flask(__name__)
cors = CORS(app)

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydb"]
mycol = mydb["adresse"]

########-Function Section-#####################################################################################################
######## reshaping document ########
def reclasse(doc):
    k = []
    v = []
    v1 = []
    k1 = []
    doc = json.loads(doc)
    for key, value in doc.items() : 
        if key == 'Composants':
            comp = value
    for key, value in doc.items() :
        k.append(key)
        v.append(value)
    abc = v[k.index('Composants')]
    for dicti in abc : 
        for key, value in dicti.items() :
            if key == 'Type' :
                v1.append(value)
            if key == 'ValeurInformation' :
                k1.append(value)
    v_for_changes = "" 
    k_for_changes = "" 
    indx1 = 0
    indx2 = 0
    for i in range(0,len(v1)-1): 
        for i in range(0,len(v1)-1): 
            if i+1 > len(v1)-1 : 
                break
            elif type_comp.index(v1[i])>type_comp.index(v1[i+1]) : 
                k_for_changes = v1[i]
                v1[i] = v1[i+1]
                v1[i+1] = k_for_changes
                v_for_changes = comp[i]
                comp[i] = comp[i+1]
                comp[i+1] = v_for_changes
                indx1 +=1
        if indx1 == indx2:
            break
        else : 
            indx2 = indx1
            continue
    
    doc.update({ "Composants":comp})
    return(doc)

####### filtering address ########
def FilterAdress(input_adress): 
    list = input_adress.split()
    if list[0].lower() in type_error:
        list.pop(0)
        filtred_adress = ' '.join([str(elem) for elem in list]) 
        return filtred_adress
    else:
        return input_adress

####### making the address function ##########
def make_adrss(select_id) : 
    adrss = []
    sss = mycol.find( {"Id" :select_id} )

    for ss in sss : 
        mkmkm =  ss['Composants']

    for k in mkmkm : 
        # using json.dumps() for cast it to string
        m = k['ValeurInformation']
        lll = json.loads(json.dumps(m))
        for key, value in lll.items() :
            if type(value) == int : 
                adrss.append(value)
            else :
                adrss.append(value.capitalize())
        adrss.append(',')
        
    adrss = adrss[:-1]
    #x = FilterAdress( ' '.join(map(str, adrss)))
    return(','.join(map(str, (FilterAdress( ' '.join(map(str, adrss)))).split(' ,'))))

#####################################################################################################

@app.route('/geocoding')
def geocoding():
    address = request.args['address']
    
    #developper les requetes ici pour obtenir la position de l'address entrer
    #
    #

    #recuper la position dans un objet json 
    position = {
        "isExist": False,
        "address": address,
        "lat": "35.73436456343",
        "lng": "-0.5744564553453"
    }
    return f'{json.dumps(position)}'

@app.route('/reverseGeocoding')
def reverseGeocoding():
    lat = float(request.args['lat']) 
    lng = float(request.args['lng']) 

    #developper les requetes ici pour obtenir l'adresse correspondante a cette position
    adresse = 'none address'
    bb  = mycol.aggregate([
        {
            '$geoNear': {
                'near': { 'type': 'Point', 'coordinates': [ lat, lng ]},
                'distanceField': 'ObjetAdressable.PositionAdresse.Geometrie.coordinates',
                'spherical': True, 
                "maxDistance": 20,
            }
        }
    ])
    for i in bb :
        adresse = i ['Adresse'] 
        if adresse == 'none address' : 
            continue
        else : 
            break
    if adresse == 'none address' : 
        position = {
            "isExist" : False
        }
    else :
        position = {
            "isExist" : True,
            "address" : adresse,
            "lat" : lat,
            "lng" : lng
        }
    
    #recuper la position dans un objet json 
    return f'{json.dumps(position)}'


@app.route('/autocomplete')
def autocomplete():

    sugg_input = request.args['input']
    
    #developper les requetes ici pour obtenir les propositions d'address correspond a ce input
    if sugg_input[0] in [' ', ',', ';','.'] :
        sugg_input = sugg_input[1:]

    es = [","," ,", ", "," ;","; ","   ","  "]
    for i in range(0,len(es)) :
        sugg_input = ' '.join(map(str,sugg_input.split(es[i])))
    words_adrs = sugg_input.split(' ')
    val_adrs = []
    adrs = []
    sss = mycol.find({},{"_id":0, "Adresse" : 1})
    for ss in sss :  
            val_adrs.append(ss["Adresse"])
    adrs = val_adrs
    val_adrs = []
    for k in range(0,len(words_adrs)) : 
        for kk in adrs : 
         if  re.search(words_adrs[k].lower(), kk.lower()) != None : 
            val_adrs.append(kk)
        adrs = val_adrs
        val_adrs = []
    if len(adrs)> 10 :
        adrs = adrs[0:10]
    #

    return f'{json.dumps(adrs)}'# >>> autocoplete

@app.route('/insertion', methods=['POST'])
def insertion():
    form = request.args['form']

    #developper les requetes ici pour inserer cette adresse form
    doc = reclasse(form)
    doc.update({ "Id" : mycol.find().count() + 1})
    mycol.insert_one(doc)
    mycol.update_one({"Id" : mycol.find().count()},{"$set" : {"Adresse" : make_adrss(mycol.find().count())}})
    #'The address was successfully insered!'
    return 'The address was successfully insered!'

@app.route('/selectedSuggestion')
def selectedSuggestion():
    adresse = request.args['address']

    #developper les requetes ici pour inserer cette adresse form
    #
    kkk = mycol.aggregate([
        { "$match": { "Adresse": adresse } },
        { "$project": { "_id": 0, "coordinates" : "$ObjetAdressable.PositionAdresse.Geometrie.coordinates"}},
        { "$sort": {"Id": 1}}
    ])
    for kk in kkk :
        tt = kk

    try:
        tt
    except NameError:
        rep ={
            "isExist" : False,
            "address": adresse,
        }
    else:
        for key , value in kk.items() :
            coord = value
        rep ={
            "isExist" : True,
            "address": adresse,
            "lat" : coord[0],
            "lng" : coord[1]
        }

    #recuper la position dans un objet json 

    return f'{json.dumps(rep)}'

if __name__ == '__main__':
    app.run(debug=True, port=5000)





