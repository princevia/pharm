<template>
  <div class="page-category">
    <div class="columns is-multiline">
      <div class="column is-12">
        <h2 class="is-size-2 has-text-centered">{{ category.name }}</h2>
      </div>
      <ProductBox
        v-for="product in category.products"
        v-bind:product="product"
        v-bind:key="product.id"
      />
    </div>
  </div>
</template>

<script>
import axios from "axios"
import ProductBox from '@/components/ProductBox'
export default {
  nme: 'Category',
  components: {
    ProductBox
  },
  data() {
    return {
      category: {
        products: []
      }
    }
  },

  mounted() {
    this.getCategory();
  },

  watch: {
        $route(to, from) {
            if (to.name === 'Category') {
                this.getCategory()
            }
        }
    },

  methods: {
    async getCategory() {
      this.$store.commit('setIsLoading', true)

      const categorySlug = this.$route.params.category_slug

      await axios
        .get(`/api/v1/products/${categorySlug}/`)
        .then(response => {
          this.category = response.data
          document.title = this.category.name + " | Pharm";
        })
        .catch(error => {
          console.error(error)

        toast({
            message: 'Something went wrong. Please try again.',
            type: 'is-danger',
            dismissable: true,
            pauseOnHover: true,
            duration: 2000,
            position: 'bottom-right',

            })

        })
      this.$store.commit('setIsLoading', false)
    }
  }
}
</script>










