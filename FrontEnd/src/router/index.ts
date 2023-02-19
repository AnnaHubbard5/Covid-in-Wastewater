import { createRouter, createWebHistory, RouteRecordRaw } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import AboutView from '../views/AboutView.vue'
import NotifyView from '../views/NotifyView.vue'

const routes: RouteRecordRaw[] = [
  {
    path: '/',
    name: 'home',
    component: HomeView,
  },

  {
    path: '/about',
    name: 'about',
    component: AboutView,
  },
  {
    path: '/notify',
    name: 'notify',
    component: NotifyView,
  },
]
const router = createRouter({
  history: createWebHistory(),
  routes,
})

export default router
