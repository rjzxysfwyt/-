<template>
  <el-descriptions class="margin-top" title="带边框列表" :column="3" :size="size" border>
    <template slot="extra">
      <el-button type="primary" size="small">操作</el-button>
    </template>
    <el-descriptions-item>
      <template slot="label">
        <i class="el-icon-user"></i>
        用户名
      </template>
      kooriookami
    </el-descriptions-item>
    
    <el-descriptions-item>
      <template slot="label">
        <i class="el-icon-place"></i>
        年龄
      </template>
      20
    </el-descriptions-item>

    <el-descriptions-item>
      <template slot="label">
        <i class="el-icon-eleme"></i>
        生日
      </template>
      2020104111
    </el-descriptions-item>


    <el-descriptions-item>
      <template slot="label">
        <i class="el-icon-mobile-phone"></i>
        手机号
      </template>
      18100000000
    </el-descriptions-item>
    <el-descriptions-item>
      <template slot="label">
        <i class="el-icon-location-outline"></i>
        居住地
      </template>
      苏州市
    </el-descriptions-item>
    <el-descriptions-item>
      <template slot="label">
        <i class="el-icon-tickets"></i>
        备注
      </template>
      <el-tag size="small">学校</el-tag>
    </el-descriptions-item>
    <el-descriptions-item>
      <template slot="label">
        <i class="el-icon-office-building"></i>
        联系地址
      </template>
      <!-- 江苏省苏州市吴中区吴中大道 1188 号 -->
      xkk
    </el-descriptions-item>

    <el-descriptions-item>
      <template slot="label">
        <i class="el-icon-sunny"></i>
        兴趣爱好
      </template>
      打游戏
    </el-descriptions-item>

    <el-descriptions-item>
      <template slot="label">
        <i class="el-icon-chat-line-round"></i>
        交友想法
      </template>
      找个好朋友
    </el-descriptions-item>
  </el-descriptions>

  
</template>

<script>
export default {
    name:'PersonInfor'
}
</script>

<style>

</style>