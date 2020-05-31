import Vue from 'vue'
import Router from 'vue-router'
//==================================================
import Home from '@/components/Home'
import Login from '@/components/Login'
import Register from '@/components/Register'
import Contact from '@/components/Contact'
import Category from '@/components/viewGrid/Category'
import Profile from '@/components/Profile'
import ProfileProduct from '@/components/ProfileProduct'
//========================================================
import ChatHome from '@/components/ChatRoom/ChatHome'
import Room from '@/components/ChatRoom/rooms/Room'
import Dialog from '@/components/ChatRoom/rooms/Dialog'


Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home
    },
    {
      path: '/login',
      name: 'login',
      component: Login
    },
    {
      path: '/contact',
      name: 'contact',
      component: Contact
    },
    {
      path: '/register',
      name: 'register',
      component: Register
    },
    {
      path: '/category',
      name: 'category',
      component: Category
    },
    {
      path: '/profile',
      name: 'profile',
      component: Profile
    },
    {
      path: '/profileproduct',
      name: 'profileproduct',
      component: ProfileProduct
    },
    {
      path: '/room',
      name: 'room',
      component: Room
  },
  {
      path: '/chathome',
      name: 'chathome',
      component: ChatHome
  },
  {
      path: '/dialog/:id',
      name: 'dialog',
      component: Dialog
  },
  ]
})
