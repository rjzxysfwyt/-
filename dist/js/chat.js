/* 初始化右侧滚动条
   这个方法定义在scroll.js中*/
{$(function () {
  resetui()

  const ipt = document.querySelector('#ipt')
  /* 为发送按钮绑定鼠标点击事件*/
  const btnSend = document.querySelector('#btnSend')
  btnSend.addEventListener('click',function () {
      let text = ipt.value.trim()
      if (text.length <= 0) {
          ipt.value = ''
          return
      }
      /* 如果用户输入了聊天内容，则将聊天内容追加到页面上显示*/
      const talk_list = document.querySelector('#talk_list')
      talk_list.innerHTML += '<li class="right_word"><img src="img/person02.png" /> <span>' + text + '</span></li>'
      ipt.value = ''
      /* 重置滚动条的位置*/
      resetui()
      /* 发起请求，获取聊天内容*/
      getMsg(text)
  })

  /* 获取发送回来的消息*/
  function getMsg(text) {
    $.ajax({
      method: 'GET',
      /* 下面的url改改*/
      url: 'http://ajax.frontend.itheima.net:3006/api/robot',
      data: {
        spoken: text
      },
      success: function (res) {
        /* console.log(res)*/
        if (res.message === 'success') {
          /* 接收聊天消息*/
          let msg = res.data.info.text
          $('#talk_list').append('<li class="left_word"><img src="img/person01.png" /> <span>' + msg + '</span></li>')
          /* 重置滚动条的位置*/
          resetui()
        }
      }
    })
  }

  // 为文本框绑定 keyup 事件
    ipt.addEventListener('keyup', function (e) {
      if (e.keyCode === 13) {
          btnSend.click()
      }
  })
})()}