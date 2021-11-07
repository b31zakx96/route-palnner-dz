<template>
    
    <div>
        
        <Navbar :flag="true" :btnColor="'outline-secondary'" :color="'light'" />

        <!-- router links 
        <b-breadcrumb class="breadcrumb">
            <b-breadcrumb-item >
            <b-icon icon="house-fill" scale="1.25" shift-v="1.25" aria-hidden="true"></b-icon>
            <router-link to="/" > Home</router-link>
            </b-breadcrumb-item>
            <b-breadcrumb-item ><router-link to="/Demo-Map" >Demo</router-link></b-breadcrumb-item>
            <b-breadcrumb-item active>Add</b-breadcrumb-item>
        </b-breadcrumb>
         fin router links --> 
        
       
        
<!-- ------------------------------------------------------------------------------------------------------------------------------ -->

        <b-container fluid class="bv-example-row">
            <label id="title">Form | Add a New Address:  </label>
            <b-row>
                
                <b-col sm="7"> <!-- form serction -->
                    
                    <b-form @submit="onSubmit" @reset="onReset" v-if="show">
<!-- ------------------------------------------------------------------------------------------------------------------------------ -->
                        <label class="title-address">Address</label>
                        <div class="address"> <!-- address part doc --> 
                            
                            <b-row class="my-1"> <!--Classe -->
                                <b-col sm="4">
                                    <label for="input-small">Classe:</label>
                                </b-col>
                                <b-col sm="8">

                                    <b-form-group size="sm" id="Classe-select" label-for="adresse-Classe-select">
                                        <b-form-select
                                        id="Classe-select"
                                        name="adresse-Classe-select"
                                        v-model="form.Classe"
                                        size="sm"
                                        required
                                        :options="Classe"
                                        @change="typeCompAdr_classAdr"
                                        ></b-form-select>
                                    </b-form-group>                                     

                                </b-col>
                            </b-row> <!--f Classe -->


                            <b-row class="my-1"> <!--Niveau Preference -->
                                <b-col sm="4">
                                    <label for="input-small">Niveau Preference:</label>
                                </b-col>
                                <b-col sm="8">

                                    <b-form-group id="NiveauPreference-input" label-for="adresse-NiveauPreference-input">
                                        <b-form-input
                                        id="NiveauPreference-input"
                                        name="adresse-NiveauPreference-input"
                                        type="number"
                                        size="sm"
                                        v-model.number="form.NiveauPreference"
                                        required
                                        placeholder="Enter Niveau Preference"
                                        ></b-form-input>
                                    </b-form-group>   

                                </b-col>
                            </b-row> <!--f Niveau Preference -->


                            <b-row class="my-1"> <!--PhaseCycle -->
                                <b-col sm="4">
                                    <label for="input-small">Phase Cycle Vie:</label>
                                </b-col>
                                <b-col sm="8">

                                    <b-form-group size="sm" id="PhaseCycle-select" label-for="adresse-PhaseCycle-select">
                                        <b-form-select
                                        id="PhaseCycle-select"
                                        name="adresse-PhaseCycle-select"
                                        size="sm"
                                        v-model="form.PhaseCycle"
                                        required
                                        :options="PhaseCycle"
                                        ></b-form-select>
                                    </b-form-group>   

                                </b-col>
                            </b-row> <!--f PhaseCycle -->


                            <b-row class="my-1"> <!--StatutAdresse -->
                                <b-col sm="4">
                                    <label for="input-small">Statut Adresse:</label>
                                </b-col>
                                <b-col sm="8">

                                    <b-form-group size="sm" id="StatutAdresse-select" label-for="adresse-StatutAdresse-select">
                                        <b-form-select
                                        id="StatutAdresse-select"
                                        name="adresse-StatutAdresse-select"
                                        size="sm"
                                        v-model="form.StatutAdresse"
                                        required
                                        :options="StatutAdresse"
                                        ></b-form-select>

                                        <b-form-invalid-feedback id="input-live-feedback">This is a required field.</b-form-invalid-feedback>
                                    </b-form-group>   

                                </b-col>
                            </b-row> <!--f StatutAdresse -->


                            <b-row class="my-1"> <!--LangueAdresse -->
                                <b-col sm="4">
                                    <label for="input-small">Langue Adresse:</label>
                                </b-col>
                                <b-col sm="8">

                                    <b-form-group size="sm" id="LangueAdresse-select" label-for="adresse-LangueAdresse-select">
                                        <b-form-select
                                        id="LangueAdresse-select"
                                        name="adresse-LangueAdresse-select"
                                        size="sm"
                                        v-model="form.LangueAdresse"
                                        required
                                        :options="TypeLangue"
                                        ></b-form-select>
                                    </b-form-group>   

                                </b-col>
                            </b-row> <!--f LangueAdresse -->

                        </div>  <!-- fin address part doc --> 



<!-- ------------------------------------------------------------------------------------------------------------------------------ -->



                        <label class="title-address">Objet Adressable</label>
                        <div class="address"> <!-- ObjetAdressable part doc --> 
                        
                            <b-row class="my-1"> <!--TypeObjetAdressable -->
                                <b-col sm="4">
                                    <label for="input-small">Type Objet Adressable:</label>
                                </b-col>
                                <b-col sm="8">

                                    <b-form-group size="sm" id="TypeObjetAdressable-select" label-for="ObjetAdressable-TypeObjetAdressable-select">
                                        <b-form-select
                                        id="TypeObjetAdressable-select"
                                        name="ObjetAdressable-TypeObjetAdressable-select"
                                        size="sm"
                                        v-model="form.ObjetAdressable.TypeObjetAdressable"
                                        required
                                        :options="TypeObjetAdressable"
                                        ></b-form-select>
                                    </b-form-group>   

                                </b-col>
                            </b-row> <!--f TypeObjetAdressable -->
                            

                            <b-row class="my-1"> <!-- coords input -->
                                <b-col sm="4">
                                    <label for="input-small">Position (Coordinates):</label>
                                </b-col>
                                <b-col sm="8">
                                    <b-input-group id="coords-input" size="sm" class="mb-2">
                                        <b-form-input required type="text" placeholder="Latitude"
                                        v-model="form.ObjetAdressable.PositionAdresse.Geometrie.coordinates[0]" 
                                        ></b-form-input>
                                        <b-form-input required type="text" placeholder="Longitude"
                                        v-model="form.ObjetAdressable.PositionAdresse.Geometrie.coordinates[1]"                             
                                        ></b-form-input>  
                                    </b-input-group>
                                </b-col>
                            </b-row> <!--f coords input -->


                            <b-row class="my-1"> <!--TypePositionAdresse -->
                                <b-col sm="4">
                                    <label for="input-small">Type Position Adresse:</label>
                                </b-col>
                                <b-col sm="8">

                                    <b-form-group size="sm" id="TypePositionAdresse-select" label-for="ObjetAdressable-TypePositionAdresse-select">
                                        <b-form-select
                                        id="TypePositionAdresse-select"
                                        name="ObjetAdressable-TypePositionAdresse-select"
                                        size="sm"
                                        v-model="form.ObjetAdressable.PositionAdresse.TypePositionAdresse"
                                        required
                                        :options="TypePositionAdresse"
                                        ></b-form-select>
                                    </b-form-group>   

                                </b-col>
                            </b-row> <!--f TypePositionAdresse -->


                            <b-row class="my-1"> <!--TypeAcces -->
                                <b-col sm="4">
                                    <label for="input-small">Type Access:</label>
                                </b-col>
                                <b-col sm="8">

                                    <b-form-group size="sm" id="TypeAcces-select" label-for="ObjetAdressable-TypeAcces-select">
                                        <b-form-select
                                        id="TypeAcces-select"
                                        name="ObjetAdressable-TypeAcces-select"
                                        size="sm"
                                        v-model="form.ObjetAdressable.PositionAdresse.TypeAcces"
                                        required
                                        :options="TypeAcces"
                                        ></b-form-select>
                                    </b-form-group>   

                                </b-col>
                            </b-row> <!--f TypeAcces -->

                        </div> <!-- fin ObjetAdressable part doc --> 



<!-- ------------------------------------------------------------------------------------------------------------------------------ -->



                        <label class="title-address">Composant Adresse</label>
                        <div class="address" :key="index" v-for="(composant, index) in form.Composants" > <!-- composant address part doc --> 

                                <b-row class="my-1"> <!-- TypeComposantAdresse dynamic -->
                                    <b-col sm="12" class="iconDel" >
                                        <b-icon icon="x" class="float-right" @click="closeComposant(index, composant)" ></b-icon>
                                        <b-icon icon="plus" class="float-right" @click="addComposant(composant)" ></b-icon>
                                    </b-col>
                                    

                                    <b-col sm="4"> <!-- Langue Composant Adresse -->
                                        <label for="input-small">Langue Composant Adresse:</label>
                                    </b-col>
                                    <b-col sm="8">

                                        <b-form-group size="sm" id="LangueComposantAdresse-select" label-for="TypeComposantAdresse-LangueComposantAdresse-select">
                                            <b-form-select
                                            id="type-select"
                                            name="TypeComposantAdresse-LangueComposantAdresse-select"
                                            size="sm"
                                            v-model="composant.LangueComposantAdresse"
                                            required
                                            :options="TypeLangue"
                                            ></b-form-select>
                                        </b-form-group>

                                    </b-col> <!-- fin Langue Composant Adresse -->


                                    <b-col sm="4"> <!-- Type Composant Adresse -->
                                        <label for="input-small">Type Composant Adresse:</label>
                                    </b-col>
                                    <b-col sm="8">

                                        <b-form-group size="sm" id="type-select" label-for="TypeComposantAdresse-type-select">
                                            <b-form-select
                                            id="type-select"
                                            name="TypeComposantAdresse-type-select"
                                            size="sm"
                                            v-model="composant.Type"
                                            required
                                            :options="types"
                                            @change="resetDataType(composant)"
                                            ></b-form-select>
                                        </b-form-group>

                                    </b-col> <!-- fin Type Composant Adresse -->
                                    

                                </b-row>  <!--fin TypeComposantAdresse dynamic -->

                                
                                
                                


                                <!--v-if Numéro -->

                                <b-row class="my-1" v-if=" composant.Type == 'Numéro' " > <!--PrefixeNumero -->
                                    <b-col sm="4">
                                        <label for="input-small">Préfixe Numéro:</label>
                                    </b-col>
                                    <b-col sm="8">

                                        <b-form-group id="PrefixeNumero-input" label-for="composantadresse-PrefixeNumero-input">
                                            <b-form-input
                                            id="PrefixeNumero-input"
                                            name="composantadresse-PrefixeNumero-input"
                                            type="text"
                                            size="sm"
                                            v-model="composant.ValeurInformation.PrefixeNumero"
                                            placeholder="Enter Préfixe Numéro"
                                            ></b-form-input>
                                        </b-form-group>   

                                    </b-col>
                                </b-row> <!--fin v-if PrefixeNumero -->

                                <b-row class="my-1" v-if=" composant.Type == 'Numéro' " > <!--ValeurNumero -->
                                    <b-col sm="4">
                                        <label for="input-small">Valeur Numéro:</label>
                                    </b-col>
                                    <b-col sm="8">

                                        <b-form-group id="ValeurNumero-input" label-for="composantadresse-ValeurNumero-input">
                                            <b-form-input
                                            id="ValeurNumero-input"
                                            name="composantadresse-ValeurNumero-input"
                                            type="number"
                                            size="sm"
                                            v-model.number="composant.ValeurInformation.ValeurNumero"
                                            placeholder="Enter Valeur Numéro"
                                            ></b-form-input>
                                        </b-form-group>   

                                    </b-col>
                                </b-row> <!--fin v-if ValeurNumero -->

                                <b-row class="my-1" v-if=" composant.Type == 'Numéro' " > <!--SuffixeNumero -->
                                    <b-col sm="4">
                                        <label for="input-small">Suffixe Numéro:</label>
                                    </b-col>
                                    <b-col sm="8">

                                        <b-form-group id="SuffixeNumero-input" label-for="composantadresse-SuffixeNumero-input">
                                            <b-form-input
                                            id="SuffixeNumero-input"
                                            name="composantadresse-SuffixeNumero-input"
                                            type="text"
                                            size="sm"
                                            v-model="composant.ValeurInformation.SuffixeNumero"
                                            placeholder="Enter Suffixe Numéro"
                                            ></b-form-input>
                                        </b-form-group>   

                                    </b-col>
                                </b-row> <!--fin v-if SuffixeNumero -->

                                <b-row class="my-1" v-if=" composant.Type == 'Numéro' " > <!--Repetition -->
                                    <b-col sm="4">
                                        <label for="input-small">Repetition:</label>
                                    </b-col>
                                    <b-col sm="8">

                                        <b-form-group id="Repetition-input" label-for="composantadresse-Repetition-input">
                                            <b-form-input
                                            id="Repetition-input"
                                            name="composantadresse-Repetition-input"
                                            type="text"
                                            size="sm"
                                            v-model="composant.ValeurInformation.Repetition"
                                            placeholder="Enter Repetition"
                                            ></b-form-input>
                                        </b-form-group>   

                                    </b-col>
                                </b-row> <!--fin v-if Repetition -->

                             <!--fin v-if Numéro -->



                            <!--v-if TypeLieu-dit --> 
                                <b-row class="my-1" v-if=" composant.Type == 'Nom de Lieu-dit' "> <!--v-if TypeLieudit -->
                                    <b-col sm="4">
                                        <label for="input-small">Type Lieu-dit:</label>
                                    </b-col>
                                    <b-col sm="8">

                                        <b-form-group size="sm" id="TypeLieudit-select" label-for="TypeComposantAdresse-TypeLieudit-select">
                                            <b-form-select
                                            id="TypeLieudit-select"
                                            name="TypeComposantAdresse-TypeLieudit-select"
                                            size="sm"
                                            v-model="composant.ValeurInformation.TypeLieudit"
                                            placeholder="choose"
                                            required
                                            :options="TypeLieudit"
                                            ></b-form-select>
                                        </b-form-group>

                                    </b-col>
                                </b-row>  <!-- fin v-if TypeLieudit --> 

                                <b-row class="my-1" v-if=" composant.Type == 'Nom de Lieu-dit' " > <!--ValeurLieudit -->
                                    <b-col sm="4">
                                        <label for="input-small">Valeur Lieu-dit:</label>
                                    </b-col>
                                    <b-col sm="8">

                                        <b-form-group id="ValeurLieudit-input" label-for="adresse-ValeurLieudit-input">
                                            <b-form-input
                                            id="ValeurLieudit-input"
                                            name="TypeComposantAdresse-ValeurLieudit-input"
                                            type="text"
                                            size="sm"
                                            v-model="composant.ValeurInformation.ValeurLieudit"
                                            required
                                            placeholder="Enter Valeur Lieu-dit"
                                            ></b-form-input>
                                        </b-form-group>   

                                    </b-col>
                                </b-row> <!--fin v-if ValeurLieudit -->

                                <!--fin v-if TypeLieu-dit --> 



                                <!--v-if Localite --> 
                                <b-row class="my-1" v-if=" composant.Type == 'Localité' " > <!--Commune -->
                                    <b-col sm="4">
                                        <label for="input-small">Commune:</label>
                                    </b-col>
                                    <b-col sm="8">

                                        <b-form-group id="Commune-input" label-for="TypeComposantAdresse-Commune-input">
                                            <b-form-input
                                            id="Commune-input"
                                            name="TypeComposantAdresse-Commune-input"
                                            type="text"
                                            size="sm"
                                            v-model="composant.ValeurInformation.Commune"
                                            required
                                            placeholder="Enter Commune"
                                            ></b-form-input>
                                        </b-form-group>   

                                    </b-col>
                                </b-row> <!--fin v-if Commune -->

                                <b-row class="my-1" v-if=" composant.Type == 'Localité' " > <!--CodePostal -->
                                    <b-col sm="4">
                                        <label for="input-small">Code Postal:</label>
                                    </b-col>
                                    <b-col sm="8">

                                        <b-form-group id="CodePostal-input" label-for="TypeComposantAdresse-CodePostal-input">
                                            <b-form-input
                                            id="CodePostal-input"
                                            name="TypeComposantAdresse-CodePostal-input"
                                            type="number"
                                            size="sm"
                                            v-model.number="composant.ValeurInformation.CodePostal"
                                            required
                                            placeholder="Enter Code Postal"
                                            ></b-form-input>
                                        </b-form-group>   

                                    </b-col>
                                </b-row> <!--fin v-if CodePostal -->

                                <b-row class="my-1" v-if=" composant.Type == 'Localité' "> <!--v-if Wilaya -->
                                    <b-col sm="4">
                                        <label for="input-small">Wilaya:</label>
                                    </b-col>
                                    <b-col sm="8">

                                        <b-form-group size="sm" id="Wilaya-select" label-for="TypeComposantAdresse-Wilaya-select">
                                            <b-form-select
                                            id="Wilaya-select"
                                            name="TypeComposantAdresse-Wilaya-select"
                                            size="sm"
                                            v-model="composant.ValeurInformation.Wilaya"
                                            placeholder="choose"
                                            required
                                            :options="ListWilaya"
                                            ></b-form-select>
                                        </b-form-group>

                                    </b-col>
                                </b-row>  <!-- fin v-if Wilaya --> 
                              
                                <!--fin v-if Localite --> 



                                <!--v-if  Boite Postale -->

                                <b-row class="my-1" v-if=" composant.Type == 'Boite postale' " > <!--NumeroBoitePostale -->
                                    <b-col sm="4">
                                        <label for="input-small">Boite Postale:</label>
                                    </b-col>
                                    <b-col sm="8">

                                        <b-form-group id="NumeroBoitePostale-input" label-for="composantadresse-NumeroBoitePostale-input">
                                            <b-form-input
                                            id="NumeroBoitePostale-input"
                                            name="composantadresse-NumeroBoitePostale-input"
                                            type="number"
                                            size="sm"
                                            v-model.number="composant.ValeurInformation.NumeroBoitePostale"
                                            required
                                            placeholder="Enter Numéro Boite Postale"
                                            ></b-form-input>
                                        </b-form-group>   

                                    </b-col>
                                </b-row> <!--fin v-if NumeroBoitePostale -->
                                
                             <!--fin v-if Boite Postale -->



                            <!--v-if Voie --> 
                                <b-row class="my-1" v-if=" composant.Type == 'Voie' "> <!--v-if TypeVoie -->
                                    <b-col sm="4">
                                        <label for="input-small">Type Voie:</label>
                                    </b-col>
                                    <b-col sm="8">

                                        <b-form-group size="sm" id="TypeVoie-select" label-for="TypeComposantAdresse-TypeVoie-select">
                                            <b-form-select
                                            id="TypeVoie-select"
                                            name="TypeComposantAdresse-TypeVoie-select"
                                            size="sm"
                                            v-model="composant.ValeurInformation.TypeVoie"
                                            placeholder="choose"
                                            required
                                            :options="TypeVoie"
                                            ></b-form-select>
                                        </b-form-group>

                                    </b-col>
                                </b-row>  <!-- fin v-if TypeVoie --> 

                                <b-row class="my-1" v-if=" composant.Type == 'Voie' " > <!--NomVoie -->
                                    <b-col sm="4">
                                        <label for="input-small">Nom Voie:</label>
                                    </b-col>
                                    <b-col sm="8">

                                        <b-form-group id="NomVoie-input" label-for="adresse-NomVoie-input">
                                            <b-form-input
                                            id="NomVoie-input"
                                            name="TypeComposantAdresse-NomVoie-input"
                                            type="text"
                                            size="sm"
                                            v-model="composant.ValeurInformation.NomVoie"
                                            required
                                            placeholder="Enter Nom Voie"
                                            ></b-form-input>
                                        </b-form-group>   

                                    </b-col>
                                </b-row> <!--fin v-if NomVoie -->

                                <!--fin v-if Voie -->                             



                                <!--v-if zone -->
                                <b-row class="my-1" v-if=" composant.Type == 'Zone' "> <!--v-if Typezone -->
                                    <b-col sm="4">
                                        <label for="input-small">Type Zone:</label>
                                    </b-col>
                                    <b-col sm="8">

                                        <b-form-group size="sm" id="Typezone-select" label-for="TypeComposantAdresse-Typezone-select">
                                            <b-form-select
                                            id="Typezone-select"
                                            name="TypeComposantAdresse-Typezone-select"
                                            size="sm"
                                            v-model="composant.ValeurInformation.Typezone"
                                            placeholder="choose"
                                            required
                                            :options="Typezone"
                                            ></b-form-select>
                                        </b-form-group>

                                    </b-col>
                                </b-row>  <!-- fin v-if Typezone --> 

                                <b-row class="my-1" v-if=" composant.Type == 'Zone' " > <!--Valeurzone -->
                                    <b-col sm="4">
                                        <label for="input-small">Valeur Zone:</label>
                                    </b-col>
                                    <b-col sm="8">

                                        <b-form-group id="Valeurzone-input" label-for="TypeComposantAdresse-Valeurzone-input">
                                            <b-form-input
                                            id="Valeurzone-input"
                                            name="TypeComposantAdresse-Valeurzone-input"
                                            type="text"
                                            size="sm"
                                            v-model="composant.ValeurInformation.Valeurzone"
                                            required
                                            placeholder="Enter Valeur Zone"
                                            ></b-form-input>
                                        </b-form-group>   

                                    </b-col>
                                </b-row> <!--fin v-if Valeurzone -->

                                <!--fin v-if Zone -->
                            



                                <!--v-if Unité de bâtiment -->
                                <b-row class="my-1" v-if=" composant.Type == 'Unité de bâtiment' "> <!--v-if TypeBatiment -->
                                    <b-col sm="4">
                                        <label for="input-small">Type Batiment:</label>
                                    </b-col>
                                    <b-col sm="8">

                                        <b-form-group size="sm" id="TypeBatiment-select" label-for="TypeComposantAdresse-TypeBatiment-select">
                                            <b-form-select
                                            id="TypeBatiment-select"
                                            name="TypeComposantAdresse-TypeBatiment-select"
                                            size="sm"
                                            v-model="composant.ValeurInformation.TypeBatiment"
                                            placeholder="choose"
                                            required
                                            :options="TypeBatiment"
                                            ></b-form-select>
                                        </b-form-group>

                                    </b-col>
                                </b-row>  <!-- fin v-if TypeBatiment --> 

                                <b-row class="my-1" v-if=" composant.Type == 'Unité de bâtiment' " > <!--NumeroBatiment -->
                                    <b-col sm="4">
                                        <label for="input-small">Numéro Batiment:</label>
                                    </b-col>
                                    <b-col sm="8">

                                        <b-form-group id="NumeroBatiment-input" label-for="TypeComposantAdresse-NumeroBatiment-input">
                                            <b-form-input
                                            id="NumeroBatiment-input"
                                            name="TypeComposantAdresse-NumeroBatiment-input"
                                            type="text"
                                            size="sm"
                                            v-model="composant.ValeurInformation.NumeroBatiment"
                                            placeholder="Enter Numéro Batiment"
                                            ></b-form-input>
                                        </b-form-group>   

                                    </b-col>
                                </b-row> <!--fin v-if NumeroBatiment -->

                                <b-row class="my-1" v-if=" composant.Type == 'Unité de bâtiment' "> <!--v-if TypeUnite -->
                                    <b-col sm="4">
                                        <label for="input-small">Type Unite:</label>
                                    </b-col>
                                    <b-col sm="8">

                                        <b-form-group size="sm" id="TypeUnite-select" label-for="TypeComposantAdresse-TypeUnite-select">
                                            <b-form-select
                                            id="TypeUnite-select"
                                            name="TypeComposantAdresse-TypeUnite-select"
                                            size="sm"
                                            v-model="composant.ValeurInformation.TypeUnite"
                                            placeholder="choose"
                                            required
                                            :options="TypeUnite"
                                            ></b-form-select>
                                        </b-form-group>

                                    </b-col>
                                </b-row>  <!-- fin v-if TypeUnite --> 

                                <b-row class="my-1" v-if=" composant.Type == 'Unité de bâtiment' " > <!--Valeurzone -->
                                    <b-col sm="4">
                                        <label for="input-small">Numéro Unite:</label>
                                    </b-col>
                                    <b-col sm="8">

                                        <b-form-group id="NumeroUnite-input" label-for="TypeComposantAdresse-NumeroUnite-input">
                                            <b-form-input
                                            id="NumeroUnite-input"
                                            name="TypeComposantAdresse-NumeroUnite-input"
                                            type="text"
                                            size="sm"
                                            v-model="composant.ValeurInformation.NumeroUnite"
                                            placeholder="Enter Numéro Unite"
                                            ></b-form-input>
                                        </b-form-group>   

                                    </b-col>
                                </b-row> <!--fin v-if NuméroUnite -->

                                <b-row class="my-1" v-if=" composant.Type == 'Unité de bâtiment' " > <!--Niveau -->
                                    <b-col sm="4">
                                        <label for="input-small">Niveau:</label>
                                    </b-col>
                                    <b-col sm="8">

                                        <b-form-group id="Niveau-input" label-for="TypeComposantAdresse-Niveau-input">
                                            <b-form-input
                                            id="Niveau-input"
                                            name="TypeComposantAdresse-Niveau-input"
                                            type="text"
                                            size="sm"
                                            v-model="composant.ValeurInformation.Niveau"
                                            placeholder="Enter Niveau"
                                            ></b-form-input>
                                        </b-form-group>   

                                    </b-col>
                                </b-row> <!--fin v-if Valeurzone -->

                                <!--fin v-if Unité de bâtiment  -->


                                <!--v-if Organisme -->
                                <b-row class="my-1" v-if=" composant.Type == 'Organisme' "> <!--v-if TypeOrganisme -->
                                    <b-col sm="4">
                                        <label for="input-small">Type Organisme:</label>
                                    </b-col>
                                    <b-col sm="8">

                                        <b-form-group size="sm" id="TypeOrganisme-select" label-for="TypeComposantAdresse-TypeOrganisme-select">
                                            <b-form-select
                                            id="TypeOrganisme-select"
                                            name="TypeComposantAdresse-TypeOrganisme-select"
                                            size="sm"
                                            v-model="composant.ValeurInformation.TypeOrganisme"
                                            required
                                            :options="TypeOrganisme"
                                            ></b-form-select>
                                        </b-form-group>

                                    </b-col>
                                </b-row>  <!-- fin v-if TypeOrganisme --> 

                                <b-row class="my-1" v-if=" composant.Type == 'Organisme' " > <!--ValeurOrganisme -->
                                    <b-col sm="4">
                                        <label for="input-small">Valeur Organisme:</label>
                                    </b-col>
                                    <b-col sm="8">

                                        <b-form-group id="ValeurOrganisme-input" label-for="TypeComposantAdresse-ValeurOrganisme-input">
                                            <b-form-input
                                            id="Valeurzone-input"
                                            name="TypeComposantAdresse-ValeurOrganisme-input"
                                            type="text"
                                            size="sm"
                                            v-model="composant.ValeurInformation.ValeurOrganisme"
                                            required
                                            placeholder="Enter Valeur Organisme"
                                            ></b-form-input>
                                        </b-form-group>   

                                    </b-col>
                                </b-row> <!--fin v-if ValeurOrganisme -->

                                <!--fin v-if Organisme -->


                        </div> <!--fin composant address part doc -->




                        <!-- alert successfull -->

                        <b-modal id="bv-modal-example" hide-footer :header-bg-variant="'success'">
                            <template v-slot:modal-title> Success! </template>
                            <div class="d-block text-center">
                            <h5>{{successMsg}}</h5> <br>
                            </div>
                            
                            <b-button size="sm" class="float-right" variant="outline-danger" @click="$bvModal.hide('bv-modal-example')">Close</b-button>
                        </b-modal>


                        <!-- fin alert successfull -->

                        <br>
                        <b-button size="sm" type="submit" variant="primary">Submit</b-button>
                        <b-button size="sm" type="reset" variant="danger">Reset</b-button>
                        
                    </b-form>
                    
                </b-col> <!-- end form serction -->



<!-- ------------------------------------------------------------------------------------------------------------------------------ -->




                <b-col sm="5"> <!-- Handling Forms section -->
                  
                    <b-card class="mt-4 sm" header="Form Data Result">
                        <pre class="m-0">New Address:</pre>
                        <pre class="m-0">{{ form }}</pre>
                    </b-card>

                </b-col>  <!-- End Handling Forms section -->
            </b-row>

        </b-container>      



    </div>

</template>


<script>
import axios from 'axios';
import Navbar from '../components/Navbar';
export default {
    
    name: "AddNewAddress",
    components: {
      Navbar
    },
    data: function() {
        return {
            
            successMsg: null,
            adresse: null,
            idCounter: 2,
            show: true,
            //data address section
            Classe: [{ text: "Choose Classe adresse...", value: null }, "Adresse sur voie", "Adresse zonale", "Adresse point d’intérêt", "Adresse postale", "Adresse rurale"],
            PhaseCycle: [{ text: "Choose Phase Cycle Vie...", value: null }, "Actuel", "Proposé", "Refusé", "Réservé", "Retiré", "Inconnu"],
            StatutAdresse: [{ text: "Choose Statut Adresse..." , value: null }, "Officiel", "Non officiel", "Inconnu"],
            TypeLangue: [{ text: "Choose Langue Adresse...", value: null }, "Arabe", "Français", "Anglais", "Tamazight"],
            
            //data ObjetAdressable section
            TypeObjetAdressable: [{ text: "Choose Type Objet Adressable...", value: null }, "Bâtiment", "Parcelle", "Maison", "Monument", "Equipement", "Appartement", "Complexe", "Immobilier", "Forêt", "Jardin", "Public", "Place", "Placette", "Parc", "Autre"],
            TypePositionAdresse: [{ text: "Choose Type Position Adresse..." , value: null }, "Centroïde", "Accès sur voie", "Approximative"],
            TypeAcces: [{ text: "Choose Type Access..." , value: null }, "Principal", "Secondaire", "Activité", "Garage", "Secours", "Autre"],
 
            //data composantadresse section
            types: [{ text: "Choose Type Composant Adresse...", value: null }, { value: "Numéro", text: "Numéro", disabled: false}, { value: "Nom de Lieu-dit", text: "Nom de Lieu-dit", disabled: false}, { value: "Localité", text: "Localité", disabled: false}, { value: "Boite postale", text: "Boite postale", disabled: false}, { value: "Voie", text: "Voie", disabled: false}, { value: "Zone", text: "Zone", disabled: false}, { value: "Unité de bâtiment", text: "Unité de bâtiment", disabled: false}, { value: "Organisme", text: "Organisme", disabled: false}],
            typess :[ "Numéro", "Nom de Lieu-dit", "Localité", "Boite postale", "Voie", "Zone", "Unité de bâtiment", "Organisme"],

            // data type composant adresse 
            Typezone: [{ text: "Choose Type Zone...", value: null },"Cité", "Groupement", "Lotissement", "Coopérative", "Résidence", "Complexe", "Zone Industrielle", "Autre"],
            TypeLieudit: [{ text: "Choose Type Lieu-dit...", value: null },"Placette", "Place", "Monument", "Lieu-dit", "Autre"],
            ListWilaya: [{ text: "Choose Wilaya...", value: null },"Adrar", "Chlef","Laghouat","Oum El Bouaghi","Batna","Béjaïa","Biskra","Béchar","Blida","Bouira","Tamanrasset","Tébessa","Tlemcen","Tiaret","Tizi Ouzou","Alger","Djelfa","Jijel","Sétif","Saïda","Skikda","Sidi Bel Abbès","Annaba","Guelma","Constantine","Médéa","Mostaganem","M'Sila","Mascara","Ouargla","Oran","El Bayadh","Illizi","Bordj Bou Arreridj","Boumerdès","El Tarf","Tindouf","Tissemsilt","El Oued","Khenchela","Souk Ahras","Tipaza","Mila","Aïn Defla","Naâma","Aïn Témouchent","Ghardaïa","Relizane"],
            TypeVoie: [{ text: "Choose Type Voie...", value: null },"Boulevard", "Rue", "Avenue", "Passage", "Chemin", "Allée", "Impasse", "Route Nationale", "Chemin Wilaya", "Chemin Communal", "Autre" ],
            TypeBatiment: [{ text: "Choose Type Batiment...", value: null },"Ilot", "Bâtiment", "Résidence", "Villa", "Autre"],
            TypeUnite: [{ text: "Choose Type Unite...", value: null },"Logement", "Bureau", "Local"],
            TypeOrganisme: [{ text: "Choose Type Organisme...", value: null },"Sécurité et Protection", "Justice", "Santé", "Sport", "Education/Enseignement", "Service", "Administration", "Hotel", "Restauration", "Banque", "Mosquée", "Autre"],

            form: {
                Id: 1,
                Classe: null,
                NiveauPreference: null,
                PhaseCycle: null,
                StatutAdresse: null,
                LangueAdresse: null,

                Composants:[
                    { id: 1, Type: null, ValeurInformation:{  }, LangueComposantAdresse: null }
                ],

                ObjetAdressable:{
                    Id: 1,
                    TypeObjetAdressable: null,
                    PositionAdresse:{
                        Geometrie:{
                            type: "Point",
                            coordinates:[null, null]
                        },
                        TypePositionAdresse: null,
                        TypeAcces: null
                    }
                }
            }
        }

    }, //data 
    mounted() {
        
        this.$nextTick(() => {


        });

    }, //mounted

    watch:{

        /*adresse: function(){
            for (let i = 0; i < this.form.Composants; i++) {
                if(this.form.Composants[i].Type )
            }
        }*/

    }, //watch

    methods: {
        
        typeCompAdr_classAdr() {
            if (this.form.Classe == 'Adresse sur voie' || this.form.Classe == 'Adresse Zonale'){
                for (let i = 0; i < this.types.length; i++) {
                    this.types[i].disabled = false;
                }   
            }

            if (this.form.Classe == 'Adresse point d’intérêt'){
                for (let i = 0; i < this.types.length; i++) {
                    if (this.types[i].value == 'Numéro' || this.types[i].value == 'Voie' || this.types[i].value == 'Zone'|| this.types[i].value == 'Unité de bâtiment' ) {
                        this.types[i].disabled = true;
                    }else{
                        this.types[i].disabled = false;
                    }
                }   
            }

            if (this.form.Classe == 'Adresse postale'){
                for (let i = 0; i < this.types.length; i++) {
                    if (this.types[i].value == 'Numéro' || this.types[i].value == 'Voie' || this.types[i].value == 'Unité de bâtiment' ) {
                        this.types[i].disabled = true;
                    }else{
                        this.types[i].disabled = false;
                    }
                }   
            }
            
            if (this.form.Classe == 'Adresse rurale'){
                for (let i = 0; i < this.types.length; i++) {
                    if (this.types[i].value == 'Numéro' || this.types[i].value == 'Boite postale' || this.types[i].value == 'Voie' || this.types[i].value == 'Zone' || this.types[i].value == 'Unité de bâtiment' || this.types[i].value == 'Organisme'  ) {
                        this.types[i].disabled = true;
                    }else{
                        this.types[i].disabled = false;
                    }
                }   
            }
        },

        resetDataType(composant) {

            if (this.form.Classe == 'Adresse point d’intérêt' ){
                if(composant.Type == 'Nom de Lieu-dit'){
                    this.types[8].disabled = true;
                }else if(composant.Type == 'Organisme')  {
                    this.types[2].disabled = true;
                }     
            }

            if (this.form.Classe == 'Adresse sur voie' || this.form.Classe == 'Adresse Zonale'){
                if(composant.Type == 'Numéro'){
                    this.types[7].disabled = true;
                }else if(composant.Type == 'Unité de bâtiment') {
                    this.types[1].disabled = true;
                }     
            }

            composant.ValeurInformation = {};

            if( composant.Type == 'Boite postale'){composant.ValeurInformation = {ValeurBoitePostale: "BP", NumeroBoitePostale: null }}
            if( composant.Type == 'Numéro'){composant.ValeurInformation = {PrefixeNumero: "", ValeurNumero: null, SuffixeNumero: "", Repetition: "" }}
            if( composant.Type == 'Nom de Lieu-dit'){composant.ValeurInformation = {TypeLieudit: null, ValeurLieudit: ""}}
            if( composant.Type == 'Localité'){composant.ValeurInformation = {Commune: "", CodePostal: null, Wilaya: null, Pays: "Algerie" }}
            if( composant.Type == 'Unité de bâtiment'){composant.ValeurInformation = {TypeBatiment: null, NumeroBatiment: "", TypeUnite: null, NumeroUnite: "", Niveau: "" }}
            if( composant.Type == 'Voie'){composant.ValeurInformation = {TypeVoie: null, NomVoie: "" }}
            if( composant.Type == 'Zone'){composant.ValeurInformation = {Typezone: null, Valeurzone: "" }}
            if( composant.Type == 'Organisme'){composant.ValeurInformation = {TypeOrganisme: null, ValeurOrganisme: "" }}
            
        },

        closeComposant(index, composant) {

            if (this.form.Classe == 'Adresse point d’intérêt' ){
                if(composant.Type == 'Nom de Lieu-dit'){
                    this.types[8].disabled = false;
                }else if(composant.Type == 'Organisme')  {
                    this.types[2].disabled = false;
                }     
            }

            if (this.form.Classe == 'Adresse sur voie' || this.form.Classe == 'Adresse Zonale'){
                if(composant.Type == 'Numéro'){
                    this.types[7].disabled = false;
                }else if(composant.Type == 'Unité de bâtiment')  {
                    this.types[1].disabled = false;
                }     
            }

            if (this.form.Composants.length == 1) {
                this.form.Composants = [{ id: 1, Type: null, ValeurInformation:{  }, LangueComposantAdresse: null }]
            }else{
                this.form.Composants.splice(index, 1);
                this.idCounter--
            }
        },

        addComposant(composant) {

            /*for (let i = 0; i < this.form.Composants.length; i++) {
                if(Object.values(this.typess).includes(this.form.Composants[i].Type) === true ){
                    var ind = this.typess.indexOf(this.form.Composants[i].Type);
                    this.types[ind+1].disabled = true
                }
            }*/

            this.form.Composants.push({ id: (this.idCounter+=2), Type: null, ValeurInformation:{  }, LangueComposantAdresse: null });

            if (this.form.Classe == 'Adresse point d’intérêt' ){
                if(composant.Type == 'Nom de Lieu-dit'){
                    this.types[8].disabled = true;
                }else if(composant.Type == 'Organisme')  {
                    this.types[2].disabled = true;
                }     
            }

            if (this.form.Classe == 'Adresse sur voie' || this.form.Classe == 'Adresse Zonale'){
                if(composant.Type == 'Numéro'){
                    this.types[7].disabled = true;
                }else if(composant.Type == 'Unité de bâtiment')  {
                    this.types[1].disabled = true;
                }     
            }
        },

        isNumber(){
            var myVar_1 = this.form.ObjetAdressable.PositionAdresse.Geometrie.coordinates[0]
            var myVar_2 = this.form.ObjetAdressable.PositionAdresse.Geometrie.coordinates[1]
            var myLat = +myVar_1; var myLng = +myVar_2;
            if (isNaN(myLat) || isNaN(myLng)) {
                //string
                return false;
            } else{
                this.form.ObjetAdressable.PositionAdresse.Geometrie.coordinates[0] = parseFloat(myVar_1);
                this.form.ObjetAdressable.PositionAdresse.Geometrie.coordinates[1] = parseFloat(myVar_2);
                return true;
            }
        },

        onSubmit(evt) {
            if (this.isNumber()){
                evt.preventDefault()

                for (let i = 0; i < this.form.Composants.length; i++) {
                    if(Object.values(this.typess).includes(this.form.Composants[i].Type) === true ){
                        var ind = this.typess.indexOf(this.form.Composants[i].Type);
                        this.types[ind+1].disabled = true
                    }
                }
                //console.log(this.form);
                //alert(JSON.stringify(this.form))
                axios({
                method: 'post',
                url:'http://127.0.0.1:5000/insertion?',
                params:{form: this.form}
                })
                .then((response) => {
                    //console.log(response.data);
                    this.successMsg = response.data;
                    this.$bvModal.show('bv-modal-example') //alert successful
                })
                .catch( (error) => {
                    console.log(error);
                    console.log('Network Error: from locale server!\n>> http://127.0.0.1:5000/insertion');
                });
                

            }else{
                alert('Invalid Coordinates: Something wrong with coordinates')
            }
        },

        onReset(evt) {
            evt.preventDefault()
            // Reset our form values
            this.form.Classe = null
            this.form.NiveauPreference = null
            this.form.PhaseCycle = null
            this.form.StatutAdresse = null
            this.form.LangueAdresse = null 
            this.form.ObjetAdressable.TypeObjetAdressable = null
            this.form.ObjetAdressable.PositionAdresse.TypePositionAdresse = null
            this.form.ObjetAdressable.PositionAdresse.TypeAcces = null
            this.form.ObjetAdressable.PositionAdresse.Geometrie.coordinates = [null, null]
            this.form.Composants = [{ id: 1, Type: null, ValeurInformation:{  }, LangueComposantAdresse: null }]
            // Trick to reset/clear native browser form validation state
            this.show = false
            this.$nextTick(() => {
            this.show = true
            })
        }    

    }//methods

} //export default  http://localhost:8080/Add-New-Address
</script>





<style >

.h3{
    color: brown;
    text-align: center;
}

.breadcrumb{
    background-color: darkcyan;
    border-radius: 0;
}
.breadcrumb-item.active {
    color: darkgray;
}
h3.title {
    
    text-align: center;
    font-size: 1.70rem;
    color: #f7f7f7;
    background-color: darkgray;
}
#title{
    margin-bottom: 0rem;
    margin-top: 1rem;
}
.row .my-1{
    margin-bottom: -0.75rem !important;
    padding-right: 10px;
    padding-left: 10px;
}
.address{
    border: 1px solid rgb(185, 178, 178);
    border-radius: 8px;
    padding: 8px;
}
.title-address{
    margin: 0rem;
    position: relative;
    z-index: 1;
    top: 10px;
    background: white;
    left: 10px;
    color: grey;
    font-size: small;
}
#coords-input{
    margin-bottom: 1rem !important;
}
#b{
    color: grey;
}
.nav-tabs .nav-link {
    border: 1px solid darkgray;
    border-bottom-color: transparent;
    border-top-left-radius: 0.25rem;
    border-top-right-radius: 0.25rem;
    color: #818182;
}
.iconDel{
    margin-top: -5px;
    right: -2px;
    top: -6px;
    padding: 0;
}
.card {
    height: 80%;
}
.card-body {
    padding: 0.75rem;
    overflow-y: scroll;
}
.btn{
    margin-right: 3px;
}
</style>

