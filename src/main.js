//import scss
import './scss/main.scss'

/// ESNext (original code, no pollyfills, single-file .vue component, css included)
import VueSimpleSuggest from 'vue-simple-suggest/lib';
Vue.component('vue-simple-suggest', VueSimpleSuggest)

import Vue from 'vue';
import App from './App.vue';

// import vuex 
import Vuex from 'vuex';
Vue.use(Vuex)

//import vue-router
import VueRouter from 'vue-router'
Vue.use(VueRouter);

// import store
import store from "./stores/store.js";

import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'
// Install BootstrapVue
Vue.use(BootstrapVue)
// Optionally install the BootstrapVue icon components plugin
Vue.use(IconsPlugin)
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

//import autocomplete and// Global registration
import VueBootstrapTypeahead from 'vue-bootstrap-typeahead'
Vue.component('vue-bootstrap-typeahead', VueBootstrapTypeahead)

// leaflet style
import 'leaflet/dist/leaflet.css';
Vue.config.productionTip = false;
// leaflet icon style
import { Icon } from 'leaflet';
delete Icon.Default.prototype._getIconUrl;
Icon.Default.mergeOptions({
  iconRetinaUrl: require('leaflet/dist/images/marker-icon-2x.png'),
  iconUrl: require('leaflet/dist/images/marker-icon.png'),
  shadowUrl: require('leaflet/dist/images/marker-shadow.png'),
});

// import for router links 
import Map from "./components/Map";
import AddNewAddress from "./components/AddNewAddress";
import Home from "./components/Home";

const router = new VueRouter({
  routes: [
    { path: '/', component: Home },
    { path: '/Demo-Map', component: Map },
    { path: '/Add-New-Address', component: AddNewAddress },

  ],
  mode: 'history'
})

new Vue({
  router,
  render: h => h(App),
  store,
}).$mount('#app')
