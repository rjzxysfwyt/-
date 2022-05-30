//该文件用于创建Vuex中最为核心的store
import Vue from 'vue'
//引入Vuex
import Vuex from 'vuex'
//应用Vuex插件
Vue.use(Vuex)

//准备actions——用于响应组件中的动作
const actions = {
	
}
//准备mutations——用于操作数据（state）
const mutations = {
	//控制页面路由
    change(state,value){
        console.log(state,value)
        state.option=value
    }
}
//准备state——用于存储数据
const state = {
	option:1
}

//创建并暴露store
export default new Vuex.Store({
	actions,
	mutations,
	state,
})




// //引入请求
// import { reqGetCode, reqUserRegister, reqUserLogin, reqUserInfo,reqLogout } from "@/api";
// import { setToken, getToken, removeToken } from "@/utils/token";

// //登录注册的仓库
// const state = {
//     code: '',
//     token: getToken(),
//     userInfo: {},
// };
// const mutations = {
//     GETCODE(state, data) {
//         state.code = data;
//     },

//     USERLOGIN(state, data) {
//         state.token = data;
//     },

//     GETUSERINFO(state, data) {
//         state.userInfo = data;
//     },

//     //退出登录，清除数据（仓库和本地）
//     CLEAR(state, data){
//         state.token = '';
//         state.userInfo = {};
//         removeToken();
//     }
// };
// const actions = {
//     //获取验证码
//     async getCode({ commit }, phone) {
//         let result = await reqGetCode(phone);
//         if (result.code == 200) {
//             commit("GETCODE", result.data)
//             return 'ok'
//         } else {
//             return Promise.reject(new Error('faile'))
//         }
//     },

//     //用户注册
//     async userRegister({ commit }, user) {
//         let result = await reqUserRegister(user);
//         if (result.code == 200) {
//             return 'ok';
//         } else {
//             return Promise.reject(new Error('faile'))
//         }
//     },

//     //用户登录
//     async userLogin({ commit }, data) {
//         let result = await reqUserLogin(data);
//         if (result.code == 200) {
//             //token：令牌，用户的唯一标识
//             commit("USERLOGIN", result.data.token);
//             //持久化存储 token ==> 本地存储
//             setToken(result.data.token)
//             return 'ok'
//         } else {
//             return Promise.reject(new Error('faile'));
//         }
//     },

//     //用户登录成功，通过 token 获取用户信息
//     async getUserInfo({ commit }) {
//         let result = await reqUserInfo();

//         if (result.code == 200) {
//             //提交用户信息
//             commit("GETUSERINFO", result.data);
//             return 'ok';
//         }else{
//             return Promise.reject(new Error('faile'));
//         }
//     },


//     //退出登录
//     async userLogout({commit}){
//         //向服务器发请求，通知服务器清除 token
//         let result = await reqLogout();
//         if(result.code == 200){
//             //还需清除本地记录
//             commit("CLEAR");
//             return 'ok';
//         }else{
//             return Promise.reject(new Error('faile'));
//         }
//     }

// };
// const getters = {};
// export default {
//     state,
//     mutations,
//     actions,
//     getters,
// }
