import { createRouter, createWebHistory } from 'vue-router'
import UserDashboard from '../views/UserDashboard.vue'
import LoginView from '../views/LoginView.vue'
import CustomerRegView from '../views/userview/CustomerRegView.vue'
import UserView from '../views/userview/UserView.vue'
import CustomersView from '../views/userview/CustomersView.vue'
import CustomerView from '../views/customerview/CustomerView.vue'
import CarView from '../views/customerview/CustomerCar.vue'
import OrderView from '../views/customerview/OrderView.vue'
import WorkerRegView from '../views/userview/WorkerRegView.vue'
import WorkersView from '../views/userview/WorkersView.vue'
import AllCarsView from '../views/userview/AllCarsView.vue'
import OrderCreateView from '../views/userview/OrderCreatView.vue'
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
        path: 'workerreg',
        component: WorkerRegView,
      },
      {
        path: 'customers',
        component: CustomersView,
      },
      {
        path: 'workers',
        component: WorkersView,
      },
      {
        path: 'cars',
        component: AllCarsView,
      },
      {
        path: 'customers/:id',
        component: CustomerView,
      },
      {
        path: '/:custid/car/:id',
        component: CarView,
      },
      {
        path: '/order/:id',
        component: OrderView,
      },
      {
        path: '/creadorder/:id',
        component: OrderCreateView,
      }
    ]
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})


router.beforeEach((to, form) => {

})

export default router
