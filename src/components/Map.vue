<template>
    <div >
        <Navbar :btnColor="'outline-secondary'" :color="'light'" />
        <!-- <Direction class="container float-left" /> -->
        <!-- <b-button class="mb-2 float-right" variant="outline-dark" >
            <b-icon icon="house-door" ></b-icon><router-link to="/" > Home</router-link>
        </b-button> -->
        <Directions  />

        <div class="map">  

            <l-map ref="mymap" :zoom="zoom" :center="center" :options="{zoomControl:false, maxZoom: 18}" @click="addMarker" >
                <l-control-scale position="bottomright" :imperial="true" :metric="true"></l-control-scale>
                <l-control-zoom position="bottomright"  ></l-control-zoom>
                <l-control-layers class="control-layers" position="bottomright" ></l-control-layers>
                
                <l-tile-layer
                    v-for="tileProvider in tileProviders"
                    :key="tileProvider.name"
                    :name="tileProvider.name"
                    :visible="tileProvider.visible"
                    :url="tileProvider.url"
                    :attribution="tileProvider.attribution"
                layer-type="base"/>

                <l-wms-tile-layer
                    v-for="layer in layers"
                    :key="layer.name"
                    :base-url="baseUrl"
                    :layers="layer.layers"
                    :visible="layer.visible"
                    :name="layer.name"
                    layer-type="base">
                </l-wms-tile-layer>

                <l-marker :key="index" v-for="(marker, index) in markers" :lat-lng="marker" >
                
                    <l-popup >  
                        <p class="text-center"> <strong>Position:{{index + 1}}</strong> </p>
                        <p class="text-center" v-show="marker.showJustAddress" > <strong>OSM:</strong> {{marker.addressOnline}} </p>
                        <p class="text-center"> <strong>Local:</strong> {{marker.addressLocale}} </p>

                        <b-button pill size="sm" @click="removeMarker(index)" variant="outline-danger" class="mb-2">
                            <b-icon icon="trash" ></b-icon> Remove
                        </b-button>
                    </l-popup>
                    
                    <l-icon
                        :icon-size="iconSize"
                        :icon-anchor="iconAnchor"
                        :icon-url="marker.icon"
                        :popup-anchor="popupAnchor"
                    >
                    </l-icon>

                </l-marker>

            <l-polyline :lat-lngs="ways" :weight="8" :opacity="0.6"/>
            
            </l-map>
            
        </div>

        <Instructions  /> <!-- Instructions came from direction component in the routing info section -->

    </div>
   
</template>

<script>
import axios from 'axios';
import L from 'leaflet';
import Directions from '../components/Directions';
import Instructions from '../components/Instructions';
import Navbar from '../components/Navbar';

import { LMap, LWMSTileLayer, LTileLayer, LMarker, LPopup, LPolyline, LControlScale, LControlLayers, LControlZoom, LIcon } from 'vue2-leaflet';

// import customs icons locally
import iconMarkerEnd from '../images/iconMarkerEnd.png';
import iconMarkerStart from '../images/iconMarkerStart.png';
import iconMarker from '../images/iconMarker.png';

export default {
    name: "Map",
    data: function() {
        return {
            
            zoom: 7,
            center: [35.3015631772409, 3.2135009765625],
            baseUrl: 'http://localhost:9696/geoserver/wms/',
            url:'http://{s}.tile.osm.org/{z}/{x}/{y}.png',
            layers: [
                {
                name: 'WMS Algeria',
                visible: true,
                format: 'image/png',
                layers: 'cite:test2',
                transparent: true,
                attribution: "Algeria data © 2020 | GeoServer"
                }
            ],
            tileProviders: [
                {
                name: 'OpenStreetMap',
                visible: true,
                attribution:
                    '&copy; <a target="_blank" href="http://osm.org/copyright">OpenStreetMap</a> contributors',
                url: 'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',
                },
                {
                name: 'OpenTopoMap',
                visible: false,
                url: 'https://{s}.tile.opentopomap.org/{z}/{x}/{y}.png',
                attribution:
                    'Map data: &copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>, <a href="http://viewfinderpanoramas.org">SRTM</a> | Map style: &copy; <a href="https://opentopomap.org">OpenTopoMap</a> (<a href="https://creativecommons.org/licenses/by-sa/3.0/">CC-BY-SA</a>)',
                },
                {
                name: 'Satellite',
                visible: false,
                attribution:
                    'Tiles &copy; Esri &mdash; Source: Esri, i-cubed, USDA, USGS, AEX, GeoEye, Getmapping, Aerogrid, IGN, IGP, UPR-EGP, and the GIS User Community',
                url: 'https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}',
                },
            ],

            iconEnd: iconMarkerEnd,
            iconStart: iconMarkerStart,
            iconDefault: iconMarker, 
            iconSize: [40, 40],
            iconAnchor: [20, 40],
            popupAnchor: [0, -35]

        }

    }, //data

    components: {

        LMap,
        'l-wms-tile-layer': LWMSTileLayer,
        LTileLayer,
        LMarker,
        LPopup,
        LPolyline,
        LControlScale,
        LControlZoom,
        LControlLayers,
        LIcon,
        Directions,
        Instructions,
        Navbar

    }, //components

    mounted() {

        this.$nextTick(() => {
            console.log('hello from mounted Map!');
            if (this.markers.length >= 1){
                //fitbounds when router from map
                var markerBounds = [];
                for (var i=0; i < this.markers.length; i++){
                    markerBounds.push(L.marker([this.markers[i].lat, this.markers[i].lng]));
                }
                var group = L.featureGroup(markerBounds);
                this.$refs.mymap.mapObject.fitBounds(group.getBounds().pad(0.1));
                this.$store.commit('clearWaypoints');
            }
        });

    }, //mounted

    watch:{

        markers: function(){

            if (this.markers.length >= 1){
                this.changeIcons() //change the icon colors
            }

            if (this.markers.length >= 1){ // zoomControl dynamequement

                //console.log(this.markers.length)
                var markerBounds = [];
                for (var i=0; i < this.markers.length; i++){
                    markerBounds.push(L.marker([this.markers[i].lat, this.markers[i].lng]));
                }
                var group = L.featureGroup(markerBounds);
                this.$refs.mymap.mapObject.fitBounds(group.getBounds().pad(0.1));
            }
        }

    }, //watch

    computed:{

        markers: function(){
            return this.$store.state.positions;
        },

        ways: function() {
            return this.$store.state.waypoints;
        }

    }, //computed

    methods: {

        changeIcons(){

            var app = this
            if (app.markers.length == 1){app.markers[0].icon = app.iconStart}
            else if (app.markers.length == 2){app.markers[0].icon = app.iconStart;app.markers[1].icon = app.iconEnd;}
            else{
            app.markers[0].icon = app.iconStart;
            for(var i=1; i< app.markers.length-1; i++){
                app.markers[i].icon = app.iconDefault;
            }
            app.markers[app.markers.length-1].icon = app.iconEnd;
            }   

        },

        addMarker: function(e) {

            var url = 'https://graphhopper.com/api/1/geocode?locale=fr&debug=true&key=80e1f2d2-89f4-4e28-8349-9552cfaf537e&reverse=true&point=' + e.latlng.lat + ',' + e.latlng.lng;
            
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
                params:{lat: e.latlng.lat, lng: e.latlng.lng}
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
                        lat: e.latlng.lat,
                        lng: e.latlng.lng,
                        icon: this.iconDefault,
                        editing: false,
                        addressOnline: this.$store.state.tempAddressOn,
                        addressLocale: this.$store.state.tempAddressOff,
                        showJustAddress: true
                    }
                    this.$store.commit('getPosition', newPoint);
                    this.$store.commit('clearWaypoints');
                    console.log("You clicked the map at " + e.latlng.toString());
                });

            });

        }, 

        removeMarker(index) {

            //this.markers.splice(index, 1);
            this.$store.commit('deletePosition', index);
            this.$store.commit('clearWaypoints');

        }

    } //methods

} //export default  http://localhost:8080/Demo-Map

</script>



<!--  style  -->

<style scoped>

@import "../../node_modules/leaflet/dist/leaflet.css";
a {
  color: black;
}
.a:link, a:hover{
  text-decoration: none;
  color: white;
}
.map{
  height: 100%;
  width: 100%;
  position:absolute;
  top: 0;
  left: 0;
  z-index: -1;
}

.btn {
    margin-top: 10px;
    margin-right: 10px;
}
.leaflet-popup-content p {
    margin: 1px 0;
}

</style>
