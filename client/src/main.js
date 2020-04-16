import Vue from 'vue'
import App from './App.vue'
import VueGoogleCharts from 'vue-google-charts';
import router from './router'
import store from './store'

Vue.config.productionTip = false

// Plugins
import GlobalDirectives from './globalDirectives'

// Google charts plugin
Vue.use(VueGoogleCharts);
// clickaway
Vue.use(GlobalDirectives)

// MaterialDashboard plugin
// import MaterialDashboard from './material-dashboard'
// Vue.use(MaterialDashboard)

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
