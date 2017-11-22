// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import VueRouter from 'vue-router'
import Routes from './routes'

Vue.config.productionTip = false

Vue.use(VueRouter);


const router = new VueRouter({
 routes: Routes,
 mode:'history' // default : hash
  /*
  如果使用hash,
  地址将会是 domain.com/#/routeName, 用history则没有#号
  */

});

export const bus = new Vue();
/* eslint-disable no-new */
new Vue({
  el: '#app',
  template: '<App/>',
  components: { App },
  router: router
})
