<template>
  <div style="margin:0 50px 0 50px">
    <el-row>
      <el-col :span="10">
        <el-input
        placeholder="请输入好友用户名或邮箱"
        v-model="input"
        clearable
        >
        </el-input>
      </el-col>
      
      <el-col :span="4">
        <el-button type="primary" icon="el-icon-search" @click="Search(input)">搜索</el-button>
      </el-col>
  </el-row>
  </div>
</template>

<script>
  export default {
    name:'FriendAdd',
    data(){
        return {
          input:'',
      }
    },
    methods:{
      Search(){
        console.log('xkk')
      }
    },
}
</script>

  <style scoped>
  div{
    margin-left: 10px;
  }
  button{
    margin-left: 10px;
  }
</style>