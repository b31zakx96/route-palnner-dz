import Vuex from 'vuex'
import Vue from 'vue'

Vue.use(Vuex)

export default new Vuex.Store({
    state: {
        positions: [],
        waypoints: [],
        instructions: [],
        myPosition: null,
        tempAddressOn: null,
        tempAddressOff: null,
        suggSelected: null,
        input: null,
    },
    
    mutations: {
        getPosition(state, payload){
            state.positions.push(payload);
        },

        deletePosition(state, payload){
            state.positions.splice(payload, 1);
        },

        getMyPosition(state, payload){
            var flag = false;

            if ( state.positions.length == 0 ){
                state.positions.push(payload);
                flag = true;
            }else {
            for (var i=0; i < state.positions.length; i++){
                if ( payload.lat === state.positions[i].lat && payload.lng === state.positions[i].lng ){
                    state.positions.splice(i, 1, payload);
                    flag = true;
                }
            }
            }
            if ( flag == false ){ 
                state.positions.unshift(payload) 
            }
            state.myPosition = payload;
        },

        updatePosition(state, payload){
            state.positions.splice(payload.index, 1, payload.editingPosition);
        },

        getAddressOn(state, payload){
            state.tempAddressOn = payload;
        },

        getAddressOff(state, payload){
            state.tempAddressOff = payload;
        },

        getSelctedAddress(state, payload){
            state.suggSelected = payload;
        },

        getInput(state, payload){
            state.input = payload;
        },

        getWays(state, payload){
            state.waypoints = payload;
        },

        getInstructions(state, payload){
            state.instructions.push(payload);
        },

        clearWaypoints(state){
            state.waypoints = [];
            state.instructions = [];
        }

    },
    
})


