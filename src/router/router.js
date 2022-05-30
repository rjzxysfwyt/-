// // //路由配置信息
// // ......
// // //引入二级路由组件
// // ......

// export default [
//     //home
//     {
//         path: "/home",
//         component: Home,
//         meta: {
//             showFooter: true
//         }
//     },
//     //center
//     {
//         path: "/center",
//         component: Center,
//         meta: {
//             showFooter: true
//         },
//         //注册二级路由
//         children: [
//             {
//                 path: "myOrder",
//                 component: MyOrder,
//             },
//             {
//                 path: "groupOrder",
//                 component: GroupOrder,
//             },
//             {
//                 path:'/center',
//                 //首次访问个人中心时，重定向到/center/myOrder
//                 redirect:'/center/myOrder'
//             }
//         ]

//     },
//     //paysuccess,只有pay才能进来
//     {
//         path: "/paysuccess",
//         component: PaySuccess,
//         meta: {
//             showFooter: true
//         },
//         //路由独享守卫
//         beforeEnter:(to,from,next)=>{
//             if(from.path == "/pay"){
//                 next()
//             }else{
//                 //从其他路由而来，不跳转，停留在当前
//                 next(false)
//             }
//         }
//     },

//     //pay，只有trade才能进来
//     {
//         path: "/pay",
//         component: Pay,
//         meta: {
//             showFooter: true
//         },
//         //路由独享守卫
//         beforeEnter:(to,from,next)=>{
//             if(from.path == "/trade"){
//                 next()
//             }else{
//                 //从其他路由而来，不跳转，停留在当前
//                 next(false)
//             }
//         }
//     },

//     //trade，只有购物车才能进来
//     {
//         path: "/trade",
//         component: Trade,
//         meta: {
//             showFooter: true
//         },
//         //路由独享守卫
//         beforeEnter:(to,from,next)=>{
//             if(from.path == "/shopCart"){
//                 next()
//             }else{
//                 //从其他路由而来，不跳转，停留在当前
//                 next(false)
//             }
//         }
//     },

	
//     //重定向，在项目跑起来的时候，访问/，立马定位到首页
//     {
//         path: '*',
//         redirect: "/home"
//     }
// ]
