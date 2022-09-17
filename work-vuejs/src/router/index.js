import { createRouter, createWebHistory } from 'vue-router'
import UserDashboard from '../views/UserDashboard.vue'
import LoginView from '../views/LoginView.vue'
import CustomerRegView from '../views/userview/CustomerRegView.vue'
import UserView from '../views/userview/UserView.vue'
import CustomersView from '../views/userview/CustomersView.vue'
const routes = [
  {
    path: '/',
    name: 'LoginView',
    component: LoginView
  },
  {
    path: '/user/:id/',
    redirect: to => {
      return { path: '/dashboard' }
    },
  },
  {
    path: '/dashboard',
    name: 'UserDashboard',
    component: UserDashboard,
    children: [
      {
        path: '',
        component: UserView,
      },
      {
        path: 'customerreg',
        component: CustomerRegView,
      },
      {
        path: 'customers',
        component: CustomersView,
      }
    ]
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})


router.beforeEach((to, form) => {

})

export default router
