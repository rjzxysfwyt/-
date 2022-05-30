<template>
    <div class="Header">
        <!-- <h3 class="font1">一心一意，友你同行</h3> -->
       <img src="../assets/images/homeheader/headertext.png" style="width:70%">
       <!-- <img src="../assets/images/homeheader/headerbg.jpg" alt="头像"  class="touxiang_img"/>  -->
        <div class="xkk1">
            <el-link @click="dengLu" type="primary">登录</el-link>&nbsp;&nbsp;
            <el-link @click="zhuCe" type="primary">注册</el-link>
        </div>
   </div>
    
</template>

<!-- style="width: 100px; height: 100px" -->
<script>
export default {
    name:"HomeHeader",
    data() {
        return {
            //src:require('../assets/images/headerbg3.jpeg')
        }
    },
    methods: {
        dengLu(){
            this.$router.push('/login')
            //console.log(hhhhhhhhhhhhhhhhhhhhhhh)
        },
        zhuCe(){
            this.$router.push('./register')
        }
    },
}
</script>

<style scoped>
    
    .Header{
        height: 20vh;
        width:100%;
        background-image:url("../assets/images/homeheader/headerbg3.jpg");
        opacity: 0.7;
        filter: alpha(opacity=60);
        background-size: 100% 100%;
        border-radius: 4px
    }
    .touxiang_img {
        position: absolute;
        bottom: 30px;
        border-radius: 50%;
        height: 70px;
        /* float:left; */
        }
    .font1{
        font-family: "Helvetica Neue",Helvetica,"PingFang SC","Hiragino Sans GB","Microsoft YaHei","微软雅黑",Arial,sans-serif;
    }
    .xkk1{
       position:absolute;
       width:100px;
       height:50px;
       bottom:0;
       right: 0;
    }
</style>