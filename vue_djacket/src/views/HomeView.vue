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

      <ProductBox
        v-for="product in LeatestProducts"
        :key="product.id"
        :product="product"
      />

    </div>
    
  </div>
</template>

<script>
import axios from 'axios'
import ProductBox from '@/components/ProductBox.vue'

export default {
  name: 'HomeView',
  data() {
    return {
      LeatestProducts: []
    }
  },
  components: {
    ProductBox
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

