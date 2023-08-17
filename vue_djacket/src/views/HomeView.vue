<template>
  <div class="home">
    <section class="hero is-medium is-dark mb-d">
      <div class="hero-body has-text-centered">
        <p class="title mb-6">
          Welcome to Djacket
        </p>
        <p class="subtitle">
          The best jacket store online
        </p>
      </div>
    </section>

    <div class="columns is-multiline">
      <div class="column is-12">
        <h2 class="is-size-2 has-text-centered"> Leatest Products</h2>
      </div>

        <div class="column is-3" v-for="product in LeatestProducts" :key="product.id">
          <div class="box">
              <figure class="image mb-4 product-image">
                  <img :src="product.get_thumbnail" alt="Product Image">
              </figure>
              <h3 class="is-size-4">{{ product.name }}</h3>
              <p class="is-size-6 has-text-grey">${{ product.price }}</p>
              <router-link :to="product.get_absolute_url" class="button is-dark mt-4">View Details</router-link>
          </div>
        </div>


    </div>
    
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'HomeView',
  data() {
    return {
      LeatestProducts: []
    }
  },
  mounted() {
    this.getLeatestProducts(),
    document.title = 'Home | Djackets'
  },
  methods: {
    async getLeatestProducts () {
      this.$store.commit('showLoadingBar', true)
      await axios
        .get('/api/v1/leatest-products/')
        .then(response => {
          this.LeatestProducts = response.data
        })
        .catch(error => {
          console.group(error)
        })
        this.$store.commit('showLoadingBar', false)
    }
  },
}
</script>

<style scoped>
  .image{
    margin-top: -1.25rem;
    margin-left: -1.25rem;
    margin-right: -1.25rem;
  }
  .product-image {
    width: 100%;
    height: 0;
    padding-bottom: 100%; /* 1:1 aspect ratio */
    position: relative;
    overflow: hidden;
}

.product-image img {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    object-fit: cover; /* Maintain aspect ratio and cover the container */
}


</style>
