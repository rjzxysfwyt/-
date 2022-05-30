import request from 'axios';

//获取一个uuid来绑定验证码
export const getUuid=(uuid)=>request({
    method:'get',
    url:'http://localhost:8080/api1/get_yzm',
    responseType: 'json', 
    params:{
      uuid
    }}).then(response => {
                  console.log('请求成功了',response.data)
              },
              error => {
                  console.log('请求失败了',error.message)
              }
          )

//获取邮箱验证码
export const getYzm=(email)=>request({
    method:'get',
    url:'http://localhost:8080/api1/register1',
    responseType: 'json', 
    params:{
        email
    }}).then(response => {
                    console.log('请求成功了',response.data)
                },
                error => {
                    console.log('请求失败了',error.message)
                }
            )

//校验邮箱验证码
export const checkYzm=(email,Yzm)=>request({
    method:'get',
    url:'http://localhost:8080/api1/check_email',
    responseType: 'json', 
    params:{
        email,
        Yzm
    }}).then(response => {
                    console.log('请求成功了',response.data)
                },
                error => {
                    console.log('请求失败了',error.message)
                }
            )
        

