<template>
    <div>
    <b-navbar toggleable="lg" :type="color" :variant="color" class="shadow-sm">
        <b-navbar-brand href="">
            <img src="../images/path.png" class="d-inline-block align-top" alt="Kitten">
            Route Planner 
           
        </b-navbar-brand>

        <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

        <b-collapse id="nav-collapse" is-nav>
        <b-navbar-nav>
            <b-nav-item href="#"> <router-link id="routerHome" to="/" > Home </router-link> </b-nav-item>
            <b-nav-item href="#"> <router-link id="routerDemo" to="/Demo-Map" > Demo </router-link> </b-nav-item>
            <b-nav-item v-if="flag" href="#"> <router-link id="routerDemo" to="/Add-New-Address" > Add-New-Address </router-link> </b-nav-item>
        </b-navbar-nav>

        <!-- Right aligned nav items -->
        <b-navbar-nav class="ml-auto">
            <b-nav-form>
            <b-form-input size="sm" class="mr-sm-2" placeholder="Search"></b-form-input>
            <b-button :variant="btnColor" size="sm" class="my-2 my-sm-0" type="submit">Search</b-button>
            </b-nav-form>

            <b-nav-item-dropdown text="Lang" right>
            <b-dropdown-item href="#">EN</b-dropdown-item>
            <b-dropdown-item href="#">AR</b-dropdown-item>
            <b-dropdown-item href="#">FR</b-dropdown-item>
            </b-nav-item-dropdown>

            <b-nav-item-dropdown right>
            <!-- Using 'button-content' slot -->
            <template v-slot:button-content>
                <em>User</em>
            </template>
            <b-dropdown-item href="#">Profile</b-dropdown-item>
            <b-dropdown-item href="#">Sign Out</b-dropdown-item>
            </b-nav-item-dropdown>
        </b-navbar-nav>
        </b-collapse>
    </b-navbar>
    </div>
</template>

<script>
export default {
    name: "Navbar",
    props:{
        color: String,
        btnColor: String,
        flag: Boolean
    },
    data: function() {
        return {
            
        }
    }
}
</script>

<style lang="scss">

.navbar-expand-lg{
//border-bottom: 0.1px solid #484646;
}
#routerHome{
    color: grey;
    &:hover {
      color: darkgrey;
    }
}
#routerDemo{
    color: grey;
    &:hover {
      color: darkgrey;
    }
}
</style>