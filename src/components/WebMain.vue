<template>
    <div>
            <!-- background-color="rgb(185, 205, 237)"
            text-color="#fff"
            active-text-color="#0e6af4" -->
    <el-row class="tac">
        <el-col :span="4">
            <el-menu
            default-active="2"
            class="el-menu-vertical-demo"
            @open="handleOpen"
            @close="handleClose"
            text-color="rgb(120, 100, 307)"
            >
            <el-menu-item index="1">
                <i class="el-icon-s-platform" ></i>
                <span slot="title">
                    <router-link class="list-group-item" active-class="active" :to="{name:'webzhuye'}" >
                         网站主页
                     </router-link>
                    </span>
            </el-menu-item>


            <el-submenu index="2">
                <template slot="title">
                    <i class="el-icon-s-custom"></i>
                    <span slot="title">好 友</span>
                </template>
                <el-menu-item-group>
                    <!-- <template slot="title">分组一</template> -->
                    <el-menu-item index="2-1" >
                        <router-link class="list-group-item" active-class="active" :to="{name:'fxiaoxi'}">
                             <i class="el-icon-chat-dot-round"></i>好友消息
                        </router-link>
                    </el-menu-item>
                    <el-menu-item index="2-2" >
                        <router-link class="list-group-item" active-class="active" :to="{name:'fdongtai'}">
                            <i class="el-icon-star-off"></i>好友动态
                        </router-link>
                    </el-menu-item>
                    <el-menu-item index="2-3" >
                        <router-link class="list-group-item" active-class="active" :to="{name:'fliebiao'}">
                            <i class="el-icon-s-order"></i>好友列表
                        </router-link>
                    </el-menu-item>
                    <el-menu-item index="2-4" >
                        <router-link class="list-group-item" active-class="active" :to="{name:'fadd'}">
                            <i class="el-icon-zoom-in"></i>添加好友
                        </router-link>
                    </el-menu-item>
                </el-menu-item-group>
            </el-submenu>
            <!-- <el-menu-item index="3" disabled>
                <i class="el-icon-document"></i>
                <span slot="title">导航三</span>
            </el-menu-item> -->
            <el-submenu index="3">
                <template slot="title">
                    <i class="el-icon-user-solid"></i>
                    <span slot="title">个 人</span>
                </template>
                <el-menu-item-group>
                    <!-- <template slot="title">分组一</template> -->
                    <el-menu-item index="3-1" >
                        <router-link class="list-group-item" active-class="active" :to="{name:'phome'}">
                        <i class="el-icon-s-home"></i>我的主页
                        </router-link>
                    </el-menu-item>
                    <el-menu-item index="3-2" >
                        <router-link class="list-group-item" active-class="active" :to="{name:'pinfro'}">
                        <i class="el-icon-document-copy"></i>个人信息
                        </router-link>
                        </el-menu-item>
                </el-menu-item-group>
            </el-submenu>
            

         </el-menu>
         </el-col>
       <!-- <el-col :span="1">4
        </el-col> -->
        <el-col :span="20">
            <router-view></router-view>
        </el-col>
    </el-row>
    <!-- <button @click="transform(5)">点我测试</button> -->
    <el-col/>
    

    
   </div>
</template>

<script>
    import {mapState,mapGetters,mapMutations,mapActions} from 'vuex';
    export default {
            name:'WebDirection',
            // computed:{
            //     ...mapState(['option'])
            // },
            methods: {
                handleOpen(key, keyPath) {
                    console.log(key, keyPath);
                },
                handleClose(key, keyPath) {
                    console.log(key, keyPath);
                },
                ...mapMutations({transform:'change'}),
            }
            

    }
</script>

<style scoped>
a {
  text-decoration: none;
}
 
.router-link-active {
  text-decoration: none;
}
</style>