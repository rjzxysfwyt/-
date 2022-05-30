import Vue from 'vue'
import router from './router'

import App from './App.vue'
//import axios from 'axios'
import ElementUI from 'element-ui';
Vue.use(ElementUI);
import 'element-ui/lib/theme-chalk/index.css';
//引入聊天框小组件
import Chat from 'vue-beautiful-chat'
Vue.use(Chat)

//引入另一个聊天组件
import JwChat from "jwchat"
//引入插件
Vue.use(JwChat)
//引入ajax请求
import './api'
// Vue.use(axios)

import vueResource from 'vue-resource'
//引入store
import store from './store/user'

import  'jquery'
//使用插件
Vue.use(vueResource)


Vue.config.productionTip = false

//全局配置
//Vue.prototype.$axios = axios
new Vue({
  render: h => h(App),
  router,
  store,
  beforeCreate() {
		Vue.prototype.$bus = this
	}
}).$mount('#app')
