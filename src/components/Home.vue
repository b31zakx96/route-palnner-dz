<template>

  <div class="wrapper" >

  <Navbar :btnColor="'secondary'" :color="'dark'"/>
  
  <b-jumbotron bg-variant="dark" text-variant="white">
    
    <template v-slot:header >
      Route Planner 
      <p></p>
    </template>

    <template v-slot:lead>
      <b-row class="my-1"> 
          <b-col sm="5" >
            This is a simple website that uses OpenStreetMap road networks and Algeria specific addresses to provide offline route planners, combining existing services like OSRM routing engine and Leaflet slippy map interface. 
            Routes can be calculated for either car or foot.
          </b-col>
          <b-col sm="1" ></b-col>     
          <b-col sm="6" id="col-img">
            <img src="../images/map.png" class="img float-right" height="350px" >
          </b-col>
      </b-row>

    </template>

    <hr class="my-4">
    <b-col sm="10" id="col10"> <p>
      Use Route Planner to get directions. Find routes from a street, postcode, town, city or landmark to your destination. With maps, times and distance.
      Press the botton to get started.
    </p></b-col> 
    
    <b-button class="mb-2" variant="outline-light" >
        <router-link to="/Demo-Map" >View Demo </router-link>
    </b-button>

    <p> <br><br> <br> <br><br></p>

    <footer class="bg-dark ">
        
          <div class="small text-center text-muted"> This work is a graduation project for obtaining the engineering diploma. </div>
          <div class="small text-center text-muted">Copyright © 2020 - Route Planner </div>
          
          
    </footer>
  </b-jumbotron>

  <!-- Footer-->
       
</div>
</template>


<script>
import Navbar from '../components/Navbar';
export default {
    
    name: "Home",
    
    data: function() {
        return {


        }

    }, //data

    components:{

      Navbar

    }, //components

    mounted() {

        this.$nextTick(() => {
            console.log('hello from mounted Home!');
            
        });

    }, //mounted

} //export default   http://localhost:8080
</script>




<style >
.jumbotron{
  border-radius: 0px;
  padding: 2rem 2rem;
}
.img{
  opacity: 0.85;
  width: 100%;
  padding: 0px;
  height: 100%;
}
a {
  color: white;
}
.a:link, a:hover{
  text-decoration: none;
  color: black;
}
#col10{
  padding: 0px;
}
#col-img{
  padding-right: 2rem;
  margin-top: -60px
}
</style>



