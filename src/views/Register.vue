<template>
  <div class="login clearfix">
    <div class="login-wrap">
      <el-steps :active="activeform" align-center>
          <el-step  title="注册账号" >注册账号</el-step>
          <el-step title="完善个人信息" >完善个人信息</el-step>
          <el-step title="完成注册">完成注册</el-step>
      </el-steps>
      

      <el-row type="flex" justify="center">
          <!-- <el-form ref="loginForm" :model="user" status-icon label-width="80px">
            ref="loginForm" :model="user" label-width="160px">
           <h3>注册</h3> -->
           <!--注册-->
        <el-form :model="user" 
          status-icon 
          :rules="rules" 
          ref="user" 
          label-width="100px" 
          class="demo-user" v-if="activeform==0">
          <!-- <hr> -->
            <el-form-item prop="username" label="用户名" label-width="100px" >
              <el-input v-model="user.userName" placeholder="请输入用户名" label-width="100px" 
              prefix-icon="el-icon-user-solid"></el-input>
            </el-form-item>

            <el-form-item prop="email" label="邮箱" label-width="100px">
              <el-input v-model="user.email" placeholder="请输入邮箱" label-width="100px"
              prefix-icon="el-icon-message"/>
              <el-button size="mini" round @click="sendMsg">发送验证码</el-button>
            </el-form-item>

              <el-form-item label="验证码" prop="code">
              <el-input v-model="ruleForm.code" />
            </el-form-item>

            
            <el-form-item label="密码" prop="pass" >
                <el-input type="password" v-model="user.pass" autocomplete="off" 
                show-password  prefix-icon="el-icon-unlock"></el-input>
              </el-form-item>
              <el-form-item label="确认密码" prop="checkPass" >
                <el-input type="password" v-model="user.checkPass" autocomplete="off" 
                show-password  prefix-icon="el-icon-lock"></el-input>
              </el-form-item>
            <!-- <el-form-item>
            </el-form-item> -->
          </el-form>


          <!--完善个人信息-->
          <el-form :model="ruleForm" 
          :rules="rules" ref="ruleForm" 
          label-width="100px" class="demo-ruleForm"
           v-if="activeform===1" >
                  <el-form-item label="姓名" prop="name">
                    <el-input v-model="ruleForm.name"></el-input>
                  </el-form-item>
                  <el-form-item label="性别" prop="sex">
                    <el-radio-group v-model="ruleForm.sex">
                      <el-radio label="男"></el-radio>
                      <el-radio label="女"></el-radio>
                    </el-radio-group>
                  </el-form-item>
                  <el-form-item label="生日" prop="birthday">
                      <el-date-picker type="date" placeholder="选择日期" v-model="ruleForm.birthday" style="width: 100%;">
                      </el-date-picker>
                  </el-form-item>

                  <el-form-item label="兴趣爱好" prop="like">
                    <el-input type="textarea" v-model="ruleForm.like"></el-input>
                  </el-form-item>

                  <el-form-item label="交友方向" prop="fLike">
                    <el-input type="textarea" v-model="ruleForm.fLike"></el-input>
                  </el-form-item>
                  <!-- <el-form-item>
                    <el-button type="primary" @click="onSubmit">立即创建</el-button>
                    <el-button>取消</el-button>
                  </el-form-item> -->
                  <!-- <el-button type="primary" @click="submitForm('ruleForm')">立即创建</el-button>
                      <el-button @click="resetForm('ruleForm')">重置</el-button>-->
                   </el-form> 

             <el-col :sm="12" :lg="6" v-if="activeform==2">
                <el-result icon="success" title="注册成功" >
                  <!-- <template slot="extra">
                    <el-button type="primary" size="medium">返回</el-button>
                  </template> -->
                </el-result>
              </el-col>

              <!-- <el-col :sm="12" :lg="6" v-if="activeform==2">
                <el-result icon="error" title="错误提示" subTitle="请根据提示进行操作">
                  <template slot="extra">
                    <el-button type="primary" size="medium">返回</el-button>
                  </template>
                </el-result>
              </el-col> -->

      </el-row>

      <el-row type="flex" justify="center" v-show="activeform==0">

            <el-button  type="primary"  @click="backform" >上一步</el-button>
            <el-button  type="primary"  @click="submitForm('user')">下一步</el-button>
      </el-row>

      <el-row type="flex" justify="center" v-show="activeform==1">

            <el-button  type="primary"  @click="backform" >上一步</el-button>
            <el-button  type="primary"  @click="nextform">下一步</el-button>
      </el-row>

      <el-row type="flex" justify="center" v-show="activeform==2">
            
            <el-button  type="primary"  @click="backform" >上一步</el-button>
            <el-button  type="primary" @click="dengLu">点击登录</el-button>
      </el-row>
      
      <!-- <el-button-group>
        <el-button  type="primary"  @click="backform">上一步</el-button>
        <el-button  type="primary"  @click="nextform">下一步</el-button>
      </el-button-group> -->
        
      
    </div>
  </div>
</template>
 
<script>
import axios from "axios";
import {getYzm,checkYzm} from '../api'
export default {
  name: "Login",
  data() {
      //密码校验
    var validatePass = (rule, value, callback) => {
        if (value === '' | value.length<5) {
          callback(new Error('请输入密码,长度不小于5'));
        } else {
          if (this.user.checkPass !== '' & this.user.checkPass.length >=5 ) {
            this.$refs.user.validateField('checkPass');
          }
          callback();
        }
      };
      var validatePass2 = (rule, value, callback) => {
        if (value === '') {
          callback(new Error('请再次输入密码'));
        } else if (value !== this.user.pass) {
          callback(new Error('两次输入密码不一致!'));
        } else {
          callback();
        }
      };
//邮箱校验
// var validateEmail = (rule, value, callback) => {
//         if (value === '') {
//           callback(new Error('请正确填写邮箱'));
//         } else {
//           if (value !== '') { 
//             var reg=/^[A-Za-z0-9\u4e00-\u9fa5]+@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)+$/;
//             if(!reg.test(value)){
//               callback(new Error('请输入有效的邮箱'));
//             }
//           }
//           callback();
//         }
//       };

    return {
      user: {
        userName: "",
        email: "",
        pass: "",
        checkPass:""
      },
      ruleForm: {
          name: '',
          sex:"",
          birthday: '',
          like: '',
          flike: '',
          code:''
        },
      rules: {
        email:
          [
            { required: true, message: '请输入邮箱地址', trigger: 'blur' },
            { type: 'email', message: '请输入正确的邮箱地址', trigger: ['blur', 'change'] }
          ],
          name: [
            { required: false, message: '请输入姓名', trigger: 'blur' },
            { min: 3, max: 5, message: '长度在 3 到 5 个字符', trigger: 'blur' }
          ],
          userName: [
            { required: false, message: '请输入姓名', trigger: 'blur' },
            { min: 1, max: 20, message: '长度在 1 到 20 个字符', trigger: 'blur' }
          ],
           pass: [
            { required: true,validator: validatePass, trigger: 'blur' }
          ],
          checkPass: [
            { required: true,validator: validatePass2, trigger: 'blur' }
          ],
          sex: [
            { required: true, message: '请选择性别', trigger: 'change' }
          ],
          birthday: [
            { type: 'date', required: false, message: '请选择日期', trigger: 'change' }
          ],
          like: [
            { required: true, message: '请填写您的兴趣爱好', trigger: 'blur' }
          ],
          fLike: [
            { required: true, message: '请填写您的交友方向', trigger: 'blur' }
          ]
      
      },
      activeform: 0
    }
    
  },
  methods: {
    dengLu(){
      this.$router.push('/login')
    },
    //控制上一步，下一步
    backform() {
        if (this.activeform-- < 1) this.activeform = 0;
      },
    nextform() {
        if (this.activeform++ > 2) this.activeform = 3;
      },

     submitForm(form) {
        this.$refs[form].validate((valid) => {
          if (valid) {
            this.nextform()
            //alert('submit!');
          } else {
            console.log('error submit!!');
            return false;
          }
        });
      },
      resetForm(formName) {
        this.$refs[formName].resetFields();
      },
      sendMsg(){
          this.$refs.user.validateField('email',(valid)=>{
              if(!valid){
                console.log('我已经向',this.user.email,'发了请求')
                getYzm(this.user.email)
              }
              else{
                console.log('输入不对',this.user.email)
              }
            })
      }
      // 模拟验证码发送
      // if (!namePass && !emailPass) {
      //   let count = 60
      //   self.statusMsg = `验证码已发送,剩余${count--}秒`
      //   self.timerid = setInterval(function() {
      //     self.statusMsg = `验证码已发送,剩余${count--}秒`
      //     if (count === 0) {
      //       clearInterval(self.timerid)
      //     }
      //   }, 1000)
      // }
    
    
  }
};
</script>
 
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.login {
  width: 100%;
  height: 740px;
  /* height: 100%; */
  /* background: url("../assets/images/bg7.jpg") no-repeat; */
  background-size: cover;
  overflow: hidden;
}
.login-wrap {
  /* background: url("../assets/images/bg1.jpg") no-repeat; */
  /* background-color: #fff; */
  background-size: cover;
  width: 800px;
  /* height: 300px; */
  height: auto;
  margin: 150px auto;
  overflow: hidden;
  padding-top: 10px;
  line-height: 20px;
}
 
h3 {
  color: #0babeab8;
  font-size: 24px;
}
hr {
  background-color: #444;
  margin: 20px auto;
}
 

</style>