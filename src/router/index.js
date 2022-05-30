
import Vue from "vue";
import VueRouter from "vue-router";
// import Home from "../views/Home.vue";
import Login from '../views/Login';
import Register from '../views/Register';
import index from '../views/Home.vue'
import FriendDynamic from '../components/friends/FriendDynamic';
import FriendLists from "../components/friends/FriendList";
import FriendMessage from "../components/friends/FriendMessage"
// import WebDirection from "../components/WebDirection"
import PersonHome from '../components/person/PersonHome'
import PersonInfor from '../components/person/PersonInfor'
import WebHome from '../components/webHome/WebHome'
import FriendAdd from '../components/friends/FriendAdd'
Vue.use(VueRouter);

const routes = [
  //这里需要将根目录默认为Home，方便实现用户在保持登录 状态下再次登录时直接跳转至主页面
  {
    path:'/',
    name:'index',
    component:index,
    children:[
      {
        path:'webHome',
        name:'webzhuye',
        component:WebHome
      },
      {
        path:'friendDynamic',
        name:'fdongtai',
        component:FriendDynamic
      },
      {
        path:'friendLists',
        name:'fliebiao',
        component:FriendLists
      },
      {
        path:'friendMessages',
        name:'fxiaoxi',
        component:FriendMessage
      },
      {
        path:'addFriend',
        name:'fadd',
        component:FriendAdd
      },
      {
        path:'personHome',
        name:'phome',
        component:PersonHome
      },
      {
        path:'personInfor',
        name:'pinfro',
        component:PersonInfor
      },
    ],
    
  },
  {
    path:'/login',
    name:'denglu',
    component:Login
  },
  {
    path:'/register',
    name:'zhuce',
    component:Register
  }
  
     ]
    // router.beforeEach((to,from,next)=>
    // {
    //   //登录及注册页面可以直接进入,而主页面需要分情况
    //   if(to.path=='/login')
    //   {
    //     next();
    //     //console.log(localStorage.s);
    //   }
    //   else if(to.path=='/register')
    //   {
    //     next();
    //   }
    //   else
    //   {
    //     if(from.path=="/login")//从登录页面可以直接通过登录进入主页面
    //     {
    //       next();
    //     }
    //     else{
    //       //从/进入,如果登录状态是true，则直接next进入主页面
    //         if(localStorage.s === "true")
    //         {
    //           next();
    //           //console.log(localStorage['s'])
    //         }
    //       else {//如果登录状态是false，那么跳转至登录页面,需要登录才能进入主页面
    //         // next('/login');
    //         // console.log("需要登录")
    //       }
    //     }
    //   }
    // })

const router = new VueRouter({
  routes
});

export default router;


// //配置路由的地方
// import store from "@/store/user/index"
// import Vue from 'vue';
// import VueRouter from 'vue-router';

// //引入路由配置文件
// //import routes from './routes'
// //使用插件
// Vue.use(VueRouter);



// //解决编程导航方式路由跳转方式不可重复提交相同参数的问题 ==> 重写 push 和 replace 方法
// //1.先把 VueRouter 原型对象的 push 保存一份
// let originPush = VueRouter.prototype.push;

// //重写 push | replace
// //第一个参数：跳转地址和参数
// VueRouter.prototype.push = function (location, resolve, reject) {
//     if (resolve && reject) {
//         originPush.call(this, location, resolve, reject);
//     } else {
//         originPush.call(this, location, () => { }, () => { });
//     }
// }




// //配置路由
// let router = new VueRouter({
//     //配置路由
//     //routes: routes,
//     scrollBehavior(to, from, savedPosition) {
//         // 始终滚动到顶部
//         return { y: 0 }
//       },
// })

// //全局守卫：前置守卫（路由跳转前进行判断）
// router.beforeEach(async (to,from,next)=>{
//     //next，放行
//     //仓库获取 token ，token 是登录与否的标志
//     let token = store.state.user.token;
    
//     let name  = store.state.user.userInfo.name;
    
    
//     //1、已登录
//     if(token){
//         //已登录想去login？==> 不能去login，放行( next )到首页
//         if(to.path == '/login'){
//             next('/home')
//         }else{
//         //已登录不去login
            
//             //仓库有用户数据 ==> 放行
//             if(name){next()}
//             else{
//             //发请求，获取 userInfo，再放行
//             try {
//                 //获取用户信息成功，放行
//                 await store.dispatch('getUserInfo');
//                 next();   
//             } catch (error) {
//                 //获取用户信息失败,说明 token 失效了，清除仓库token和本地token，要重新登录，跳转到 登录
//                 await store.dispatch('userLogout');
//                 next('/login');
//             } 
//             }
//         }
//     }else{
//         //2、未登录：不能去交易相关、支付相关、个人中心 页面
//         let toPath = to.path;
//         if(toPath.indexOf('/trade')!=-1 || toPath.indexOf('/pay')!=-1 || toPath.indexOf('/center')!=-1){
//             //跳转到登录，并保存 route 的 query 参数，确保登录完成后直接跳转到 本来想去的地址
//             next('/login?redirect='+toPath);
//         }else{
//             next()
//         }
//     }
// });


// export default router;
