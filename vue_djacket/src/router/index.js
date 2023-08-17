import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import Product from '../views/Product.vue'
import About from '../views/AboutView.vue'
import Category from '../views/Category.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/:category_slug/:product_slug',
    name: 'Prodcut',
    component: Product
  },
  {
    path: '/about',
    name: 'about',
    component: About
  },
  {
    path: '/:category_slug',
    name: 'Category',
    component: Category
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
