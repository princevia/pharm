<template>
  <div class="home">
    <section class="hero is-small is-info mb-6">
      <div class="hero-body has-text-to-the-right">
        <h1 class="title mb-3">Welcome to NELLERICH-Pharmacy</h1>
        <h4 class="subtitle">the best pharmacy store online.........</h4>
      </div>
      
    </section>
    
    <div class="columns is multiline">
      <div class="column is-12">
        <p class="har has-text-centered color is-teal">Ask Mrs. Pharmacist & crew</p>
        <h2 class="phar has-text-centered">Ask your Pharmacist,</h2>
        <h2 class="phar has-text-centered">not the internet.</h2>
        <a id="call" href="tel:+2347030395587" target="_blank" class="button is-info border-sm-round">+2347030395587</a>
        <a id="call" href="" target="_blank" class="button is-info border-sm-round">Message via whatsapp</a>
      </div>
    </div>
    
      <div class="med has-text-to-the-right">
        <h2 class="title mb-3">Have a Health Emergency?</h2>
        <p class="subtitle mt-3">Request for help by letting us know your emergency and get a quick response.</p>
        <ul>
          <li>Medical Emergencies</li>
          <li>Quick Emergency Response</li>
          <li>Ambulance Service Available</li>
          <li>Nurses and Medical Dispatcher on-site</li>
        </ul>
        <a href="">
        <buttons id="push" class="button is-danger">Request Help</buttons>
        </a>
      <figure>
        <img class="emer" src="" alt="">
      </figure>
      </div>
 
      <h1 class="title has-text-centered mt-6 mb-3">Shop our Latest-selling Categories</h1>
      <p class="subtitle has-text-centered mt-3">Over the months, people like you visit our platform to get quality medications in these categories</p>

        <div class="columns is-multiline is-mobile">
  <div class="column is-one-quarter">
    <figure class="image is-4by3">
      <img src="https://images.pexels.com/photos/1222271/pexels-photo-1222271.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1" alt="Placeholder image">
    
    
      <router-link to="/his-health" class="navbar-item">
        <p class="title is-4">His Health</p>
      </router-link>
      </figure>
  </div>
  <div class="column is-one-quarter">
    <figure class="image is-4by3">
      <img src="https://images.pexels.com/photos/5502813/pexels-photo-5502813.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1" alt="Placeholder image">
    </figure>
      <router-link to="/her-health" class="navbar-item">
        <p class="title is-4">Her Health</p>
      </router-link>
  </div>
  <div class="column is-one-quarter">
    <figure class="image is-4by3">
      <img src="https://images.pexels.com/photos/806427/pexels-photo-806427.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1" alt="Placeholder image">
    </figure>
      <router-link to="/kids-health" class="navbar-item">
        <p class="title is-4">Kids Health</p>
      </router-link>
  </div>
  <div class="column is-one-quarter">
    <figure class="image is-4by3">
      <img src="https://images.pexels.com/photos/806427/pexels-photo-806427.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1" alt="Placeholder image">
    </figure>
      <router-link to="/sexual-health" class="navbar-item">
        <p class="title is-4">Sexual Health</p>
      </router-link>
  </div>
  <div class="column is-one-quarter">
    <figure class="image is-4by3">
      <img src="https://images.pexels.com/photos/7460060/pexels-photo-7460060.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1" alt="Placeholder image">
    </figure>
      <router-link to="/multivitamins" class="navbar-item">
        <p class="title is-4">Multivitamins</p>
      </router-link>
  </div>
</div>  
        
    <div class="columns is-multiline">
      <div class="column is-12">
        <h2 class="is-size-2 has-text-centered">Latest Products</h2>
      </div>
      <ProductBox
        v-bind:product="product"
        v-for="product in latestProducts"
        v-bind:key="product.id"
      />
    </div>
  </div>
</template>

<script>
import axios from 'axios'

import ProductBox from '@/components/ProductBox'
export default {
  name: 'Home',

  data() {
    return {
      latestProducts: []
    }
  },
  components: {
    ProductBox 
  },
  mounted() {
    this.getLatestProduct();
    document.title = "Home | NELLERICHPharmacy";
  },
  methods: {
    async getLatestProduct() {
      this.$store.commit('setIsLoading', true)

      await axios
        .get('/api/v1/latest-products/')
        .then(response => {
          this.latestProducts = response.data
          console.log(response.data)
        })
        .catch(error => {
          console.error(error)
        })

      this.$store.commit('setIsLoading', false)
    }
  }
}
</script>

<style scoped>
body {
	background: linear-gradient(-45deg, #464bee, #7bb2e9, #23a6d5, #10889d);
	background-size: 400% 400%;
	animation: gradient 15s ease infinite;
	height: 100%;

}

@keyframes gradient {
	0% {
		background-position: 0% 50%;
	}
	50% {
		background-position: 100% 50%;
	}
	100% {
		background-position: 0% 50%;
	}
}

#call{
  margin-right: 10px;
  margin-left: 10px;
  left: 35%;
  color: #10889d;
}
.phar{
  font-family: Arial, Helvetica, sans-serif;
  font-size: 2rem;
  font-style: normal;
  font-weight: bold;
  color: #10889d;
  letter-spacing: 1px;
}
.hero-body {
  height: 100%;
  width: 100%;
  background: linear-gradient(rgb(2, 211, 248), lightblue);
  clip-path: polygon(100% 36%, 100% 100%, 56% 100%, 0 76%, 0 0, 53% 0);
}

.hero-body > h1 {
  font-size: 30px;
  font-family: monospace;
  font-weight: bold;
  letter-spacing: 7px;
  color: hsl(0, 0%, 30%);
  cursor: pointer;
  text-transform: uppercase;
  background: linear-gradient(to right, 
  hsl(0,0%,30%) 0, 
  hsl(0,0%,100%) 10%, 
  hsl(0,0%,30%) 20%);
  background-clip: text;
  -webkit-text-fill-color: transparent;
  animation: shine 3s infinite linear;
}
@keyframes shine{
0% {
  background-position: 0;
}
60% {
  background-position: 1800px;
}
100% {
  background-position: 2000px;
}
}
#push {
  color: hsl(0, 0%, 30%);
  left: 70%;
  top: 80%;
  position: relative;
}
.med {
  background-color: lightblue;
  padding-left: 1.5rem;
  padding-top: 1.5rem;
  padding-bottom: 1.5rem;
  
}
.hero-body > h2 {
  padding-bottom: 20px;
  
}

.hero-body > h4 {
  font-size: 20px;
  font-family: "Anonymous Pro" monospace;
  font-weight: bold;
  letter-spacing: 7px;
  color: hsl(0, 0%, 70%);
  cursor: pointer;
  border-right: 2px solid hsl(0, 0%, 80%);
  animation: typewriter 4s steps(44) normal, blinkTextCursor 0.5s infinite;
  white-space: nowrap;
  overflow: hidden;
}
@keyframes typewriter {
from {
  width: 0;
}
to {
  width: 711px;
}
}
@keyframes blinkTextCursor {
from {
  border-right-color: hsl(0, 0%, 80%);
}
to {
  border-right-color: transparent;
}

}



</style>