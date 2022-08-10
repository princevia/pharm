<template>
  <div id="wrapper">
    <nav class="navbar is-lightgray">
      <div class="navbar-brand">
        <router-link to="/" class="navbar-item">
          <strong>NELLERICH-Pharmacy</strong>
        </router-link>

        <a
          aria-label="menu"
          aria-expanded="false"
          data-target="navbar-menu"
          class="navbar-burger"
          @click="showMobileMenu = !showMobileMenu"
        >
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span><span aria-hidden="true"></span
        ></a>
      </div>

      <div
        class="navbar-menu"
        id="navbar-menu"
        v-bind:class="{ 'is-active': showMobileMenu }"
      >
        <div class="navbar-start">
          <div class="navbar-item">
            <form action="/search" method="get">
              <div class="field has-addons">
                <div class="control">
                  <input
                    type="text"
                    name="query"
                    class="input"
                    placeholder="What are you looking for?"
                  />
                </div>
                <div class="control">
                  <button type="submit" class="button is-light">
                    <span class="icon"><i class="fas fa-search"></i></span>
                  </button>
                </div>
              </div>
            </form>
          </div>
        </div>
        <div class="navbar-end">
          <router-link to="/adults" class="navbar-item"> Adults </router-link>
          <router-link to="/children" class="navbar-item"> Children </router-link>

          <div class="navbar-item">
            <div class="buttons">
              <template v-if="$store.state.isAuthenticated">
                <router-link to="/my-account" class="button is-light">My Account</router-link>
              </template>
              <template v-else>
                <router-link to="/log-in" class="button is-light"
                  >Log In</router-link
                >
              </template>
              <router-link to="/cart" class="button is-success">
                <span class="cart"><i class="fas fa-shopping-cart"></i></span>
                <span>Cart ({{ cartTotalLength }}) </span>
              </router-link>
            </div>
          </div>
        </div>
      </div>
    </nav>
    <nav class="navbar is-info">
      <div class="navbar-brand">
        <router-link to="/his-health" class="navbar-item"> His Health </router-link>
        <router-link to="/her-health" class="navbar-item"> Her Health </router-link>
        <router-link to="/kids-health" class="navbar-item"> Kids Health </router-link>
        <router-link to="/sexual-health" class="navbar-item"> Sexual Health </router-link>
        <router-link to="/multivitamins" class="navbar-item"> Multivitamins </router-link>
        
      </div>

        
        <div class="navbar-start">
          <div class="navbar-item">
            
          </div>
        </div>
        <div class="navbar-end">
          <div class="navbar-item">
            <div class="buttons">
              
            </div>
          </div>
        
      </div>
    </nav>

    <div
      class="is-loading-bar has-text-centered"
      v-bind:class="{ 'is-loading': $store.state.isLoading }"
    >
      <div class="lds-dual-ring"></div>
    </div>
    <section class="section">
      <router-view />
    </section>

    <footer class="footer">
      <p class="has-text-centered">Copyright (c) 2022</p>
    </footer>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  data() {
    return {
      showMobileMenu: false,
      cart: {
        items: []
      }
    }
  },

  beforeCreate() {
    this.$store.commit("initializeStore")
    const token = this.$store.state.token

    if (token) {
      axios.defaults.headers.common["Authorization"] = "Token " + token
    } else {
      axios.defaults.headers.common["Authorization"] = ""
    }
  },

 mounted() {
    this.cart = this.$store.state.cart
  },

  computed: {
    cartTotalLength() {
      let totalLength = 0
      for (let  i=0; i < this.cart.items.length; i++) {
        totalLength += this.cart.items[i].quantity
      }

      return totalLength
    }
  }
}
</script>

<style lang="scss">
@import "../node_modules/bulma";

.lds-dual-ring {
  display: inline-block;
  width: 80px;
  height: 80px;
}
.lds-dual-ring:after {
  content: " ";
  display: block;
  width: 40px;
  height: 40px;
  margin: 8px;
  border-radius: 50%;
  border: 6px solid rgb(20, 17, 147);
  border-color: rgb(19, 12, 158) transparent #ccc transparent;
  animation: lds-dual-ring 1.2s linear infinite;
}
@keyframes lds-dual-ring {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(360deg);
  }
}
.is-loading-bar {
  height: 0;
  overflow: hidden;
  -webkit-transition: all 0.3s;
  transition: all 0.3s;
  &.is-loading {
    height: 80px;
  }
}
</style>
