import '@babel/polyfill'
import 'mutationobserver-shim'
import Vue from 'vue'
import './plugins/bootstrap-vue'
import App from './App.vue'
import router from './router'
import store from './store'
import './registerServiceWorker'
import axios from 'axios'
import VueAxios from 'vue-axios'
import BootstrapVue from 'bootstrap-vue'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

Vue.use(BootstrapVue)

Vue.config.productionTip = false

store.dispatch('loadDeck').then(() => {
  router.beforeEach((to, from, next) => {
    next()
  })  
})

new Vue({
  router,
  store,
  axios,
  VueAxios,
  render: h => h(App)
}).$mount('#app')
