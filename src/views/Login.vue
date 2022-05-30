<template>
  <div class="loginbody">
    <div class="logindata">
      <div class="logintext">
        <h2>友你同行</h2>
      </div>
      <div class="formdata">
        <el-form ref="form" :model="form" :rules="rules">
          <el-form-item prop="username">
            <!-- <i class="el-icon-user-solid"></i> -->
            <el-input
              v-model="form.username"
              clearable
              prefix-icon="el-icon-user-solid"
              placeholder="请输入账号"
            ></el-input>
          </el-form-item>
          <el-form-item prop="password">
            <el-input
              v-model="form.password"
              clearable
              prefix-icon="el-icon-unlock"
              placeholder="请输入密码"
              show-password
            ></el-input>
          </el-form-item>
        </el-form>
      </div>
      <div class="tool">
        <div>
          <el-checkbox v-model="checked" @change="remenber" style="color:black"
            >记住密码
          </el-checkbox>
        </div>
        <div>
          <span class="shou" @click="forgetpas" style="color:black">忘记密码？</span>
        </div>
      </div>
      <div class="butt">
        <!-- <el-button type="primary" @click.native.prevent="login('form')"
          >登录</el-button> -->
          <el-button type="primary" @click="onSubmit"
          >登录</el-button>
        <el-button class="shou" @click="register">注册</el-button>
      </div>
    </div>
  </div>
</template>

<script>
import { getUuid } from '@/api';
// import { login } from "@/api/login";
// import { setToken } from "@/request/auth";


export default {
  name: "Login",
  data() {
    return {
      form: {
        password: "",
        username: "",
      },
      checked: false,
      rules: {
        username: [
          { required: true, message: "请输入用户名", trigger: "blur" },
          { max: 10, message: "不能大于10个字符", trigger: "blur" },
        ],
        password: [
          { required: true, message: "请输入密码", trigger: "blur" },
          { max: 10, message: "不能大于10个字符", trigger: "blur" },
        ],
      },
    };
  },
  mounted() {
      if(localStorage.getItem("news")){
        this.form=JSON.parse(localStorage.getItem("news"))
        this.checked=true
      }
  },
  methods: {
    onSubmit() {
      getUuid(123)
      this.$router.push('/')
    },
    // login(form) {
    //   this.$refs[form].validate((valid) => {
    //     if (valid) {
    //       login(this.form)
    //         .then((res) => {
    //           if (res.code === 200) {
    //             setToken(res.data.token);
    //             localStorage.setItem("USERNAME", res.data.username);
    //             this.$message({
    //               message: "登录成功啦",
    //               type: "success",
    //               showClose: true,
    //             });
    //             this.$router.replace("/");
    //           } else {
    //             this.$message({
    //               message: "账户名或密码错误",
    //               type: "error",
    //               showClose: true,
    //             });
    //           }
    //         })
    //         .catch((err) => {
    //           this.$message({
    //             message: "账户名或密码错误",
    //             type: "error",
    //             showClose: true,
    //           });
    //         });
    //     } else {
    //       return false;
    //     }
    //   });
    // },
    remenber(data){
      this.checked=data
      if(this.checked){
          localStorage.setItem("news",JSON.stringify(this.form))
      }else{
        localStorage.removeItem("news")
      }
    },
    forgetpas() {
      this.$message({
        type:"info",
        message:"功能尚未开发额😥",
        showClose:true
      })
    },
    register() {
      this.$router.push('/register')
    },
  },
};
</script>

<style scoped>
.loginbody {
  width: 100%;
  height: 100%;
  min-width: 1000px;
  background-image: url("../assets/images/login/bg3.jpg");
  background-size: 100% 100%;
  background-position: center center;
  overflow: auto;
  background-repeat: no-repeat;
  position: fixed;
  line-height: 100%;
  padding-top: 150px;
}

.logintext {
  margin-bottom: 20px;
  line-height: 50px;
  text-align: center;
  font-size: 30px;
  font-weight: bolder;
  color: white;
  text-shadow: 2px 2px 4px #000000;
}

.logindata {
  width: 400px;
  height: 300px;
  transform: translate(-50%);
  margin-left: 50%;
}

.tool {
  display: flex;
  justify-content: space-between;
  color: #3535a7;
}

.butt {
  margin-top: 10px;
  text-align: center;
}

.shou {
  cursor: pointer;
  color: #a8abb1;
}

/*ui*/
/* /deep/ .el-form-item__label {
  font-weight: bolder;
  font-size: 15px;
  text-align: left;
}

/deep/ .el-button {
  width: 100%;
  margin-bottom: 10px;

} */
</style>

