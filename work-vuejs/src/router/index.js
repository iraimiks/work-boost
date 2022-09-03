import { createRouter, createWebHistory } from 'vue-router'
import UserDashboard from '../views/UserDashboard.vue'
import LoginView from '../views/LoginView.vue'
const routes = [
  {
    path: '/',
    name: 'LoginView',
    component: LoginView
  },
  {
    path: '/user/:id/',
    redirect: to => {
      return 'dashboard'
    },
  },
  {
    path: '/dashboard',
    name: 'UserDashboard',
    component: UserDashboard
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
