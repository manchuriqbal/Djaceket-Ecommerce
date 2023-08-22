<template>
    <div class="page-my-account">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title">My account</h1>
            </div>

            <div class="column is-12">
                <button @click="logout()" class="button is-danger">Log out</button>

                <hr>

                <div class="column is-12">
                    <h2 class="subtitle">My orders</h2>

                    <OrderSummary
                    v-for="order in orders"
                    v-bind:key="order.id"
                    v-bind:order="order" />


                </div>
            </div>

        </div>
    </div>
</template>


<script>
import axios from 'axios'
import OrderSummary from '@/components/OrderSummary.vue'

export default {
    name: 'MyAccount',
    data() {
        return {
            orders: []
        }
    },
    components: {
        OrderSummary
    },
    mounted() {
        document.title = 'My Account'

        this.getMyOrders()
    },
    methods: {
        logout() {
            axios.defaults.headers.common['Authorization'] = ''

            localStorage.removeItem('token')
            localStorage.removeItem('username')
            localStorage.removeItem('userid')

            this.$store.commit('removeToken')

            this.$router.push('/')
        },
        async getMyOrders() {
            this.$store.commit('showLoadingBar', true);

        try {
            const response = await axios.get('/api/v1/orders/', {
            headers: {
                Authorization: `Bearer ${this.$store.state.cart.token}` // Replace with your state property path
            }
            });

            this.orders = response.data;
        } catch (error) {
            console.group(error);
        }

            this.$store.commit('showLoadingBar', false)

        }
    },
}
</script>