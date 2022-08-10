<template>
  <div class="column is-3">
    <div class="box">
      <figure class="image mb-4">
        <img :src="product.get_thumbnail">
      </figure>

      <h3 class="is-size-4">
        {{ product.name }}
      </h3>
        <p class="is-size-6 has-text-grey">&#x20A6;{{ product.price }}</p>

        <router-link
          class="button is-danger mt-4"
          v-bind:to="product.get_absolute_url"
        >
          Views Details</router-link
        >
      
    </div>
  </div>
</template>

<script>
export default {
    name: 'ProductBox',
    props: {
        product: Object
    }
}
</script>


<style scoped>
 .image {
   margin-top: -1.25rem;
   margin-left: -1.25rem;
   margin-right: -1.25rem;
  
 }
</style>






