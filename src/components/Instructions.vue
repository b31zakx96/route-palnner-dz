<template>
   
    <div>
        
        <b-sidebar id="sidebar-right" width="360px" class="sidebarv2" title="INSTRUCTIONS" bg-variant="info" text-variant="light" right shadow>

            <div class="px-3 py-2">

                <!-- section info routing -->
                <li class="list-group-item clearfix" id="instructionInfo">
                    <div class="panel-info" >
                        <h4> Itinéraire </h4>  <h6> Profile: {{ instructions[0] }} </h6>
                        <h6 v-if="Math.round(instructions[1]).toString().length <= 3"> Distance: {{ Math.round(instructions[1]) }} m. Temps: {{convertSecondstoTime(instructions)}}. </h6>
                        <h6 v-if="Math.round(instructions[1]).toString().length  > 3"> Distance: {{ (instructions[1]/1000).toFixed(2)}} km. Temps: {{convertSecondstoTime(instructions)}}. </h6>
                    </div>
                </li>
                <!-- fin info routing -->  
                

                <!-- selector language -->
                
                    <b-row class="my-1"> 
                        <b-col sm="3" id="col3">
                            <label for="input-small">  <i id="italic">Language:</i>  </label>
                        </b-col>
                        <b-col sm="9" id="col9">
                            <b-form-select id="selector" v-model="language" :options="lanOptions" size="sm" class="mt-3"></b-form-select>                               
                        </b-col>
                    </b-row>     
                 
                <!-- fin selector language -->


                <!-- section instruction info list -->
                <div class="instruction-list" id="instruction-list">
                
                    <li class="list-group-item clearfix" id="li_instruction" :key="index" v-for="(instruction, index) in instructions[language]" >   
                        <b-col sm="10" class="float-left">
                            <label for="input-small" id="label_instruction"> {{instruction}} </label>
                        </b-col>
                        <b-col sm="2" class="float-right" id="col2">
                             <label v-if="instructions[3][index].toString().length <= 3" for="input-small" id="label_instruction"> {{ instructions[3][index] }} m </label>                             
                             <label v-if="instructions[3][index].toString().length > 3" for="input-small" id="label_instruction"> {{ (instructions[3][index]/1000).toFixed(1) }} km </label>                             
                        </b-col>
                    </li>
                </div>
                <!--fin  section of instruction info list -->

                
                
            </div>

        </b-sidebar>
  </div>

</template>

<script>


export default {
    
    name: "Instructions",
    data: function() {
        return {
            
            language: 5,
            lanOptions: [
            { value: 4, text: 'Arabic' },
            { value: 5, text: 'French' }
            ],

        }

    }, //data

    computed:{

        instructions: function() {
            return this.$store.state.instructions;
        }

    }, //computed

    methods:{

        convertSecondstoTime: function(instructions) { // converter time for routing info
    
            var dateObj = new Date(instructions[2] * 1000); 
            var hours = dateObj.getUTCHours(); 
            var minutes = dateObj.getUTCMinutes(); 
            var seconds = dateObj.getSeconds(); 

            return hours.toString().padStart(2, '0') 
            + ':' + minutes.toString().padStart(2, '0') 
            + ':' + seconds.toString().padStart(2, '0'); 

        },
    
    }, //methods   

} //export default

</script>



<!--  style  -->

<style lang="scss">

.sidebarv2{
    z-index:300;
    opacity: 0.92;
}

#instructionInfo{
  margin-bottom: 6px;
  background-color: #6c757d;
}

#instruction-list::-webkit-scrollbar {
  width: 6px;
  background-color: darkgrey;
} 

#instruction-list::-webkit-scrollbar-thumb {
  background-color: rgb(192, 189, 189)
}

#instruction-list::-webkit-scrollbar-track {
  -webkit-box-shadow: inset 0 0 6px rgba(141, 140, 140, 0.3);
  background-color: grey;
}

.instruction-list{
  margin-top: 0px;
  height: 58vh;
  overflow-y: scroll;
  
  #li_instruction{
    padding: 0.20rem 0rem;
    background-color: #6c757d;
    display: block;
    cursor: pointer;
    &:hover {
      background-color: grey;
    }
  }
  #label_instruction{
      margin-bottom: 0rem;
      font-size: small;
  }
}

#selector {
border: 1px solid rgba(0, 0, 0, 0.125);
background-color: #6c757d;
color: white;
}

#col2{
padding-right: 0rem;
}

#col3{
padding-left: 20px;
}

#col9{
margin-top: -16px;
padding-right: 15px;
}

#italic{ 
color: darkgrey;
}
</style>
