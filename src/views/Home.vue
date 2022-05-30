<template>
  <div>
    <el-row>
        <HomeHeader/>
    </el-row>
    
    <el-row>
      <WebMain/>
    </el-row>
        
      
    <!-- <el-row>
      <el-col :span="4">
        <WebDirection/>
      </el-col>
      <el-col :span="20">
        <WebContent/>
      </el-col>
    </el-row> -->
  </div>
</template>
<script>
      import HomeHeader from '../components/HomeHeader';
      // import WebDirection from '../components/WebDirection.vue';
      // import WebContent from "@/components/WebContent.vue";
      import WebMain from '../components/WebMain.vue'
      //import webHome from '../components/webHome/webHome.vue'
      export default {
        name: 'Home',
        data() {
          return {}
        },
        components: {
          HomeHeader,
          WebMain
        },
      }
      </script>
<style scoped>
 .el-row {
    margin-bottom: 20px;
  }
</style>
