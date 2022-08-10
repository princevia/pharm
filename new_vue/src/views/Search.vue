<template>
  <div class="page-search">
    <div class="columns is-multiline">
      <div class="is-12 column">
        <h1 class="title">Search</h1>
        <h2 class="is-size-5 has-text-centered">Search term: '{{ query }}'</h2>
      </div>

      <Productbox
        v-for="product in products"
        v-bind:product="product"
        v-bind:key="product.id"
      />
    </div>
  </div>
</template>

<script>
import axios from "axios";
import ProductBox from "@/components/ProductBox";
export default {
  name: "Search",

  data() {
    return {
      query: "",
      products: [],
    };
  },

  components: {
    ProductBox,
  },
  mounted() {
    document.title = 'Search | Pharmacy'

      let url = window.location.search.substring(1)
      let params = new URLSearchParams(url)

      if (params.get('query')) {
          this.query = params.get('query')
      }
    this.performSearch();
  },

  methods: {
    async performSearch() {
      this.query = this.$route.query.query
      this.$store.commit('setIsLoading', true)
      await axios
        .post('/api/v1/products/search', {
          query: this.query
        })
        .then(response => {
          this.products = response.data
        })
        .catch(error => {
          console.error(error)
        })
      this.$store.commit('setIsLoading', false)
    }
  }
}
</script>













