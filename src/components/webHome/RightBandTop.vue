<template>
  <div>
    <!-- <el-carousel :interval="4000" type="card" height="250px">
      <el-carousel-item v-for="item in 6" :key="item">
        
        <el-image :src="imgshow[0]" ></el-image>
      </el-carousel-item>
    </el-carousel> -->
      <el-carousel :interval="4000" type="card" >
      <el-carousel-item v-for="item in 6" :key="item">
        <!-- <el-image :src='imgShow[0]'></el-image> -->
        <el-image :src="imgShow[item-1]"></el-image>
      </el-carousel-item>
    </el-carousel>
  
  </div>
</template>
<script>
export default {
  name: "rightBandTop",
  data() {
      return {
       imgShow: [
        require('@/assets/images/homeshow/friend1.png'),
       require('@/assets/images/homeshow/friend2.jpg'),
       require('@/assets/images/homeshow/friend3.jpg'),
       require('@/assets/images/homeshow/friend4.jpg'),
       require('@/assets/images/homeshow/friend5.jpg'),
       require('@/assets/images/homeshow/friend6.jpg')]
      }
    }

};
</script>
<style scoped>

</style>
