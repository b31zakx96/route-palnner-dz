<template>

  <div class="container">
    
    <!-- button fro get direction -->
    <b-button pill v-b-toggle.sidebar-1 class="mb-2 " variant="light" >
      Get Directions <b-icon icon="map" animation="throb" ></b-icon> 
    </b-button>
    <!-- fin button fro get direction -->


    <!-- Calcul d'itinéraire -->
    <!-- panel! sidebar routing option -->
    <b-sidebar id="sidebar-1" class="sidebar" width="380px" bg-variant="light" title="Get Directions" shadow>
      
      <div class="px-3 py-2" >

          <ul class="list-group" >



              <!-- input section -->
              <div class="row">

                <div class="col-10">

                  <vue-bootstrap-typeahead 
                  ref="inputAutocomplete"
                  v-model="newInput"
                  @input="getSuggestedAddress" 
                  :data="SuggestedAddresses"
                  placeholder="Search locations..."
                  size="sm"
                  />

                </div>

                <b-button size="sm" id="search_botton" class="mb-2" variant="outline-info">
                    <b-icon @click="checkInput"  icon="search" animation="fade"></b-icon>
                </b-button>
                
              </div>
              <!-- fin  input section -->




              <!-- modal ask for add new address to database -->
              <b-modal ref="modal-no-backdrop" hide-backdrop content-class="shadow" :footer-bg-variant="'light'" :header-bg-variant="'warning'" title="Notice!">
                <template >
                    <h5>Can't find this address in the database.</h5>
                </template>

                <template >
                    <p>  {{ AddressInfo }} </p>
                    <h6 class="my-2">If you want to add this address click the botton below</h6>
                    <b-button size="sm" class="mb-2" variant="info">
                        <b-icon icon="file-arrow-down" ></b-icon><router-link to="/Add-New-Address" > Add New Address </router-link>
                    </b-button>
                </template>

                <template v-slot:modal-footer="{ cancel }">
                    <b-button size="sm" variant="outline-danger" @click="cancel()">
                        Cancel
                    </b-button>
                </template>
              </b-modal>
              <!-- fin modal ask for add new address to database -->




              <!-- section des bottons routing, reverse, find me; select profile -->
              <div class="panel-title">

                  <b-button pill size="sm" @click="findMyPosition" variant="outline-success" class="mb-2 float-right">
                      <b-icon icon="bullseye" name="addPoint" animation="throb" ></b-icon> Find Me
                  </b-button>
                  <b-button pill size="sm" @click="reverseRoute" variant="outline-warning" class="mb-2 float-right">
                      <b-icon icon="arrow-up-down" name="inverseRoute" animation="cylon-vertical"></b-icon> Reverse
                  </b-button>
                  <b-button v-model="isActive" :class="{ disabled: isActive}" pill size="sm" @click="routingWay" variant="outline-primary" class="mb-2">
                      <b-icon icon="cursor" name="calculateRoute" animation="cylon" ></b-icon> Routing
                  </b-button>
              
              </div>

              <div class=" selector row">
              
                <div class="col-sm">
                  <b-form-select v-model="profil" :options="options" size="sm" class="mt-3"></b-form-select>
                </div>
                
              </div>  
              <!-- fin section des bottons routing, reverse, find me; select profile -->



              <!-- section info routing -->
              <li v-show="showInfo" class="list-group-item clearfix" id="routingInfo">
                 <b-icon icon="X" class="float-right" @click="hideInfo" ></b-icon>
                <div class="panel-info" >
                  <h4> Itinéraire </h4>  <h6> Profile: {{ profile }} </h6>
                  <h6 v-if="Math.round(distance).toString().length > 3" > Distance: {{ (distance/1000).toFixed(2)}} km. Temps: {{ convertSecondstoTime(time) }}. </h6>
                  <h6 v-if="Math.round(distance).toString().length <= 3" > Distance: {{ Math.round(distance) }} m. Temps: {{ convertSecondstoTime(time) }}. </h6>
                  
                  <b-button size="sm" v-b-toggle.sidebar-right class="mb-2" variant="outline-info">
                    <b-icon icon="map" ></b-icon> More Instructions
                  </b-button>

                  <!-- Instructions is in the MAp components -->

                </div>

              </li>
              <!-- fin section info routing -->  



            <!-- section position info list -->
            <div class="position-list" id="position-list">

              <li class="list-group-item clearfix" :key="index" v-for="(position, index) in markers" >
                  <label class="text-left" v-show="position.showJustAddress" > <strong>OSM:</strong> {{position.addressOnline}} </label> <br v-show="position.showJustAddress">
                  <label class="text-left"> <strong>Local:</strong> {{position.addressLocale}} </label><br>
                  <strong v-if="!position.editing">{{ position.lat.toFixed(6) }}, {{ position.lng.toFixed(6) }}</strong>
                  <input v-model="position.lat" v-if="position.editing" @keyup.enter="editPosition(position, index)" type="number" class="pull-left">
                  <input v-model="position.lng" v-if="position.editing" @keyup.enter="editPosition(position, index)" type="number" class="pull-right">      
                  <div class="btn-group btn-group-sm float-right" role="group">
                      <b-button pill size="sm" @click="position.editing = !position.editing" variant="outline-success" class="mb-2 pill-right">
                        <b-icon icon="pencil" ></b-icon></b-button>
                      <b-button pill size="sm" @click="removePosition(index)" variant="outline-danger" class="mb-2 pill-right">
                          <b-icon icon="trash" ></b-icon> 
                      </b-button>
                      <!-- <button type="button" class="btn btn-default" @click="cancelPosition(position)">cancel</button> -->
                  </div>
              </li>

            </div>
            <!--fin  section of position info list -->
            


          </ul>

      </div>
      
    </b-sidebar>
    <!--fin  panel! sidebar routing option -->
  
  </div>

</template>


<script>
import axios from 'axios';
//import Navbar from '../components/Navbar';

export default {

name: "Directions",

data: function(){
  return{

    modal: false,
    isActive: true,
    profile: '',
    profil: null,
    options: [
      { value: null, text: 'Please select a profile for routing' },
      { value: 'driving', text: 'Cars' },
      { value: 'foot', text: 'Foot' }
    ],
    SuggestedAddresses: [],
    show: false,
    showInfo: false,
    newInput: '',
    time: " ",
    distance: " ",
    AddressInfo: " " //this variable assign address input for just print the address in the modals asking for new adding data
    
  }

}, //data

components:{

  //Navbar


}, //components

watch:{

  markers: function(){
    if (this.markers.length <= 1 || this.profil == null ){
      this.isActive = true; //disable route button
    }else{
      this.isActive = false; //enable route button 
    }
  }, 

  profil: function(){
    if (this.markers.length <= 1 || this.profil == null ){
      this.isActive = true; //disable route button
    }else{
      this.isActive = false; //enable route button 
    }
  }

}, //watch

computed:{

  markers: function() {
    return this.$store.state.positions;
  }

}, //computed

methods: {
  test(){
    console.log('home');
  },

  showModal() {  //show asking modal if you want to insert address in database
    this.$refs['modal-no-backdrop'].show()
  },

  hideInfo: function(){ // hide panel routing info
    this.showInfo = false;
    this.$store.commit('clearWaypoints'); //clear le polyline from map
  },

  getSuggestedAddress: function(){
    if (this.newInput == '') return this.SuggestedAddresses = [];
    //console.log('@input work fine!');
    
    //var x = this.newInput.slice(-1); //get the last caractere 
    //if ( x == " " || x == ";" || x == "," ){
      console.log('call autocomplet here');
      
      axios({
      method: 'get',
      url:'http://127.0.0.1:5000/autocomplete?',
      params:{input: this.newInput}
      }).then((response) => {

      var data = response.data;
      console.log(data);
      this.SuggestedAddresses = [];
      this.SuggestedAddresses = data;
      });  

    //}
    
  },

  checkInput: function(){ // check input section string or number

    if (this.newInput == '')
    return;

    var separators = [' ', ';', ','];
    var indexSEP = [];
    
    for (let i = 0; i < separators.length; i += 1) {

      indexSEP[i] = this.newInput.indexOf(separators[i]);
      if (indexSEP[i] > 0){
        var ind = i;
        if (ind < i){ ind = i }
      }
      
    }

    var res_1 = this.newInput.substring(0, indexSEP[ind]);
    var res_2 = this.newInput.substring(indexSEP[ind] + 1, this.newInput.length);
   
    var myNum_1 = +res_1;var myNum_2 = +res_2;
    if (isNaN(myNum_1) || isNaN(myNum_2) ) {
      
      //alert('string'); 
      if ( this.newInput.includes("+") == false ){

        this.$store.commit('getInput', this.newInput); //send this newinput to store
        axios({  ///get position if the user select one of the propositions
        method: 'get',
        url:'http://127.0.0.1:5000/selectedSuggestion?',
        params:{address: this.newInput}
        })
        .then((response) => {
          var data = response.data;
          this.$store.commit('getSelctedAddress', data.isExist);
          
          if(data.isExist == true){ this.addNewPositionFromAddress(data.lat, data.lng, data.address); }
        })
        .catch( (error) => {
          console.log(error);
          console.log('Network Error: from locale server!\n>> http://127.0.0.1:5000/selectedSuggestion');
        })
        .then(() => {
          
          if ( this.$store.state.suggSelected == false ){

            console.log('isSelected = false')
            ///////////////////////////////////////geocoding////////////////////////////////////////
            axios({
            method: 'get',
            url:'http://127.0.0.1:5000/geocoding?',
            params:{address: this.$store.state.input}
            })
            .then((response) => {
              var data = response.data;
              //console.log(data);

              if (data.isExist == true){
                console.log('call New Position From Address: Geocode Local');
                this.addNewPositionFromAddress(data.lat, data.lng, data.address);
              }else{
                console.log('call form: add new address');
                this.showModal();
              }
            })
            .catch( (error) => {
              console.log(error);
              console.log('Network Error: from locale server!\n>> http://127.0.0.1:5000/geocoding');
            });
            //////////////////////////////////////fin-geocoding//////////////////////////////////////////
          }

        });

      }else{
        
        //string & ('this is a plus code')
        if ( this.newInput.toUpperCase().indexOf("+") == 8 ){
          var OpenLocationCode = require('open-location-code').OpenLocationCode; 
          var openLocationCode = new OpenLocationCode();
          //Decode a full code: exemple: 8C7X2C2J+22
          var coord = openLocationCode.decode(this.newInput);
          this.addNewPosition(coord.latitudeCenter, coord.longitudeCenter)
        } else {
          alert("Open Location Code/Plus Code Incomplete code, expected formats: either 'AABBCCDD+EE'\nIllegalArgumentException: Passed Open Location Code is not a valid full code: "+this.newInput); 
        }

      }

    } else {

      //alert('number');
      this.addNewPosition(res_1, res_2)

    }

    this.AddressInfo = this.newInput;
    this.newInput = '';
    this.$refs.inputAutocomplete.inputValue = '';

  },

  addNewPositionFromAddress: function(lat, lng, adr){
    //console.log(adr)
    const newPoint = {
      lat: parseFloat(lat),
      lng: parseFloat(lng),
      icon: this.iconDefault,
      editing: false,
      addressOnline: "",
      addressLocale: adr,
      showJustAddress: false
    }
    this.$store.commit('getPosition', newPoint);
    this.$store.commit('clearWaypoints'); //clear le polyline from map
    this.showInfo = false;

  },

  addNewPosition: function(latitude, longitude) { //add position in map

    var url = 'https://graphhopper.com/api/1/geocode?locale=fr&debug=true&key=80e1f2d2-89f4-4e28-8349-9552cfaf537e&reverse=true&point='  + latitude + ',' + longitude;
    
    // get request from graphhopper reverseGeocoding online
    axios.get(url).
    then((r) => {
      var addressObj = r.data.hits[0];
      var addressObj1 = r.data.hits[1];
      var tempAddress = addressObj.name + ' ' + addressObj1.city + ', ' + addressObj.postcode + ' ' + addressObj1.state + ', ' + addressObj1.country;
      //console.log(tempAddress);
      this.$store.commit('getAddressOn', tempAddress);
    })
    .catch( (error) => {
      var tempAddress = 'You are offline!'
      console.log(tempAddress);
      this.$store.commit('getAddressOn', tempAddress);
      console.log(error);
      console.log('Network Error: from Graphhopper API!');
    })
    .then(() =>{
        
        axios({
        method: 'get',
        url:'http://127.0.0.1:5000/reverseGeocoding?',
        params:{lat: parseFloat(latitude), lng: parseFloat(longitude)}
        })
        .then((response) => {
          if(response.data.isExist == true){
              this.$store.commit('getAddressOff', response.data.address);
              //console.log(response.data.address);
          }else{ this.$store.commit('getAddressOff', "There is no address in database for these coordinates!"); }
        })
        .catch( (error) => {
          console.log(error);
          console.log('Network Error: from locale server!\n>> http://127.0.0.1:5000/reverseGeocoding');
        })
        .then(() =>{ 
          const newPoint = {
              lat: parseFloat(latitude),
              lng: parseFloat(longitude),
              icon: this.iconDefault,
              editing: false,
              addressOnline: this.$store.state.tempAddressOn,
              addressLocale: this.$store.state.tempAddressOff,
              showJustAddress: true
          }
          this.$store.commit('getPosition', newPoint);
          this.$store.commit('clearWaypoints'); //clear le polyline from map
          this.showInfo = false;
        });

    });

  },

  removePosition(index) { // remove position from map

    this.$store.commit('deletePosition', index);
    this.$store.commit('clearWaypoints'); //clear le polyline from map
    this.showInfo = false;
    
  },

  editPosition: function(position, index){ // editPosition

    //this._originalPosition = Object.assign({}, position);
    position.editing = false;

    var url = 'https://graphhopper.com/api/1/geocode?locale=fr&debug=true&key=80e1f2d2-89f4-4e28-8349-9552cfaf537e&reverse=true&point=' + position.lat + ',' + position.lng;
    
    // get request from graphhopper reverseGeocoding online
    axios.get(url).
    then((r) => {
      var addressObj = r.data.hits[0];
      var addressObj1 = r.data.hits[1];
      var tempAddress = addressObj.name + ' ' + addressObj1.city + ', ' + addressObj.postcode + ' ' + addressObj1.state + ', ' + addressObj1.country;
      console.log(tempAddress);
      this.$store.commit('getAddressOn', tempAddress);
    })
    .catch( (error) => {
      var tempAddress = 'You are offline!'
      console.log(tempAddress);
      this.$store.commit('getAddressOn', tempAddress);
      console.log(error);
      console.log('Network Error: from Graphhopper API!');
    })
    .then(() =>{
        
        axios({
        method: 'get',
        url:'http://127.0.0.1:5000/reverseGeocoding?',
        params:{lat: parseFloat(position.lat), lng: parseFloat(position.lng)}
        })
        .then((response) => {
          if(response.data.isExist == true){
              this.$store.commit('getAddressOff', response.data.address);
              console.log(response.data.address);
          }else{ this.$store.commit('getAddressOff', "There is no address in database for these coordinates!"); }
        })
        .catch( (error) => {
          console.log(error);
          console.log('Network Error: from locale server!\n>> http://127.0.0.1:5000/reverseGeocoding');
        })
        .then(() =>{ 
          const editingPosition = {
              lat: parseFloat(position.lat),
              lng: parseFloat(position.lng),
              icon: this.iconDefault,
              editing: false,
              addressOnline: this.$store.state.tempAddressOn,
              addressLocale: this.$store.state.tempAddressOff,
              showJustAddress: true
          }
          this.$store.commit('updatePosition', {editingPosition, index} );
          this.$store.commit('clearWaypoints'); //clear le polyline from map
          this.showInfo = false;
        });

    });

  },

  /*cancelPosition: function(position){
      Object.assign(position, this._originalPosition);
      position.editing = false;

  },*/

  reverseRoute: function () { //reverse the marker 

    this.markers.reverse();
    this.$store.commit('clearWaypoints'); //clear le polyline from map
    this.showInfo = false;
    
  },

  getPosition: function(position){ //get my position from browser

    var url = 'https://graphhopper.com/api/1/geocode?locale=fr&debug=true&key=80e1f2d2-89f4-4e28-8349-9552cfaf537e&reverse=true&point='  + position.coords.latitude + ',' + position.coords.longitude;
    
    // get request from graphhopper reverseGeocoding online
    axios.get(url).
    then((r) => {
      var addressObj = r.data.hits[0];
      var addressObj1 = r.data.hits[1];
      var tempAddress = addressObj.name + ' ' + addressObj1.city + ', ' + addressObj.postcode + ' ' + addressObj1.state + ', ' + addressObj1.country;
      //console.log(tempAddress);
      this.$store.commit('getAddressOn', tempAddress);
    })
    .catch( (error) => {
      var tempAddress = 'You are offline!'
      console.log(tempAddress);
      this.$store.commit('getAddressOn', tempAddress);
      console.log(error);
      console.log('Network Error: from Graphhopper API!');
    })
    .then(() =>{
        
      axios({
      method: 'get',
      url:'http://127.0.0.1:5000/reverseGeocoding?',
      params:{lat: parseFloat(position.coords.latitude), lng: parseFloat(position.coords.longitude)}
      })
      .then((response) => {
          if(response.data.isExist == true){
              this.$store.commit('getAddressOff', response.data.address);
              //console.log(response.data.address);
          }else{ this.$store.commit('getAddressOff', "There is no address in database for these coordinates!"); }
      })
      .catch( (error) => {
          console.log(error);
          console.log('Network Error: from locale server!\n>> http://127.0.0.1:5000/reverseGeocoding');
      })
      .then(() =>{ 
          const myPosition = {
              lat: parseFloat(position.coords.latitude),
              lng: parseFloat(position.coords.longitude),
              icon: this.iconDefault,
              editing: false,
              addressOnline: this.$store.state.tempAddressOn,
              addressLocale: this.$store.state.tempAddressOff,
              showJustAddress: true
          }
          this.$store.commit('getMyPosition', myPosition); // send my position to store 
          this.$store.commit('clearWaypoints'); //clear le polyline from map
          this.showInfo = false;
      });

    });
    
  },

  findMyPosition: function(){ //get my position from browser

    if (navigator.geolocation) {
      navigator.geolocation.getCurrentPosition(this.getPosition);
    } else { 
      console.error("Geolocation is not supported by this browser.");
    }

  },

  convertSecondstoTime: function(time) { // converter time for routing info
    
    var dateObj = new Date(time * 1000); 
    var hours = dateObj.getUTCHours(); 
    var minutes = dateObj.getUTCMinutes(); 
    var seconds = dateObj.getSeconds(); 

    return hours.toString().padStart(2, '0') 
      + ':' + minutes.toString().padStart(2, '0') 
      + ':' + seconds.toString().padStart(2, '0'); 

  },

  routingWay: function(){ // botton routing => do routing
    
    if (this.isActive == true){
      alert('Error: At least you should have 2 positions and a profile selected');
      return;
    }
    
    this.checkroute = '';
    this.showInfo = true;
    this.profile = this.profil;
    this.$store.commit('clearWaypoints'); //clear le polyline from map

    // convert the 'markers' object to array && switch lng with lat
    var arr = [];
    for (let i = 0; i < this.markers.length; i += 1) {
      if (typeof (this.markers[i]) === 'object') {
        try {
          arr.push([ 
            this.markers[i].lng, this.markers[i].lat //switching here
          ]);
        } catch (e) {
          console.error(e);
          console.log('Network Error: from OSRM API!');

        }
      }
    }

    // stringify the array 'arr' of positions to concats with the request url
    var strPosition = arr.map(a => a.join(",")).join(";");
    var dockerUrl ='http://router.project-osrm.org/route/v1/'
    //if(this.profil == 'driving') dockerUrl = 'http://127.0.0.1:5000/route/v1/'
    //if(this.profil == 'foot') dockerUrl = 'http://127.0.0.1:5001/route/v1/'

    //exp: strPosition = '-0.57077,35.72390;-0.56781,35.70408';
    var url = dockerUrl + this.profil + '/'+ strPosition + '?steps=true&overview=simplified&geometries=geojson ';
    
    // get request from OSRM 
    axios.get(url).then((r) => {
      var coords = r.data.routes[0].geometry.coordinates;
      this.distance = r.data.routes[0].legs[0].distance;
      this.time = r.data.routes[0].legs[0].duration;
      //console.log("distance: " + this.distance + "duration: " + this.time);

      // get instructions
      var steps = r.data.routes[0].legs[0].steps;
      var version = 'v5'
      var osrmTextInstructions = require('osrm-text-instructions')(version)

      var arabic = []; var french = []; var distanceSteps = []
      window.arabic = arabic; window.french = french; window.distanceSteps = distanceSteps
      steps.forEach( (step) => { 
        var instructionAr = osrmTextInstructions.compile('ar', step)
        var instructionFr = osrmTextInstructions.compile('fr', step)
        var distance = Math.round(step.distance)
        distanceSteps.push(distance)
        arabic.push(instructionAr)
        french.push(instructionFr)
      });
      this.$store.commit('getInstructions', this.profil);
      this.$store.commit('getInstructions', this.distance);
      this.$store.commit('getInstructions', this.time);
      this.$store.commit('getInstructions', distanceSteps);
      this.$store.commit('getInstructions', arabic);
      this.$store.commit('getInstructions', french);


      var routes = [];
      // reverse between lng and lat
      for (var i=0; i<coords.length; i++){
        routes.push([
          coords[i][1], coords[i][0] // reverse here
        ]);
      }

      // send to store for draw the route
      this.$store.commit('getWays', routes);
    })

  }

  
}//methods

}//export default  

</script>



<!--  style  -->

<style lang="scss" >

.container {
  position: absolute;
  z-index:100;
  margin-left: 10px;
  margin-top: 10px;
}

.sidebar{
  z-index:200;
  opacity: 0.92;
}

.SuggestedAddress{
  position: relative;
  z-index:300;
  opacity: 0.94;
}

.derection-box{
  height: 85vh;width: 75vh;
  opacity: 0.8;
  background-color: white;
  padding: 05px;
}

#position-list::-webkit-scrollbar {
  width: 6px;
  background-color: #F5F5F5;
} 

#position-list::-webkit-scrollbar-thumb {
  background-color: rgb(197, 194, 194);
}

#position-list::-webkit-scrollbar-track {
  -webkit-box-shadow: inset 0 0 6px rgba(141, 140, 140, 0.3);
  background-color: #F5F5F5;
}

.position-list{
  margin-top: 0px;
  height: 65vh;
  overflow-y: scroll;
  
  li{
    background-color:white;
    display: block;
    cursor: pointer;
    &:hover {
      background-color:#fbf4de;
    }
  }

  label {
    margin-bottom: 0.1rem;
  }
}

.position-list > label{
  padding: 0px;
  margin: 0px;
}

.btn-width{
		width: 50px;
    float: right;
}

.input-height{
  width: 346px ;
  height: 30px;
}

strong{
  line-height: 2.2;
}

.selector{
  margin-top: -16px;
  margin-bottom: 7px;
}

.a:link, a:hover{
  text-decoration: none;
  color: white;
}

.col-10{
  padding-right: 0px;
}
#search_botton{
  margin-left: 8px;
}
#routingInfo{
  margin-bottom: 6px;
}
</style>