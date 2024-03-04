const routes = [
  {
    path: '/',
    name: 'login',
    props: {
      template: 'login'
    },
    component: () => import('src/views/auth.vue'),
  },
  {
    path: '/register',
    name: 'register',
    props: {
      template: 'register'
    },
    component: () => import('src/views/auth.vue'),
  },
  {
    path: `/restaurant/:id`,
    name: 'restaurant',
    component: () => import('src/views/home.vue'),
  },
  {
    path: `/orders`,
    name: 'orders',
    component: () => import('src/views/orders.vue'),
  },
]

export default routes
