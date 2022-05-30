<template>
  <div>
        <!-- style="margin:0 50px 0 50px" -->
      
        <Right-band-top style="margin:0 50px 0 50px"></Right-band-top>
      
        <Right-band-mid style="margin:0 50px 0 50px"></Right-band-mid>
      
        <Right-band-bot style="margin:0 50px 0 50px"></Right-band-bot>
      
      <!-- <template>
        <el-backtop target=".page-component__scroll .el-scrollbar__wrap"></el-backtop>
      </template> -->
  </div>
</template>
<script>
import "../../../public/js/jquery.mousewheel"
// import "../../../public/js/"
import RightBandTop from './RightBandTop'
import RightBandBot from './RightBandBot'
import RightBandMid from './RightBandMid'
export default {
  name: 'webHome',
  data() {
    return {
    
    }
  },
  components: {
    RightBandTop,
    RightBandMid,
    RightBandBot,
  },
}
</script>
<!-- <style scoped>
  .rightBand {
    height: 100vh;
    width: 100%;
    position: relative;
    border-radius: 4px;
  }
  .rightBand img {
    height: 100%;
    width: 100%;
    position: abosulte;
    /* background-size: cover; */
    background-size: auto;
    opacity: 0.8;
    filter: alpha(opacity=60);
    border-radius: 4px
  } -->
</style>
