<template>
  <div class="post-container" style="margin:0 50px 0 50px">
        <div class="header">
            <span>交友圈</span>
            <img src="@/assets/images/friendDongtai/person02.png" alt="头像">
            <div class="post">
                <a>发布</a>
            </div>
        </div>
<!--        动态发布区，点击头部右侧后有过渡效果显示出来-->
        <div class="publish-container">
            <div class="publish">
                <input type="button" value="发布">
                <textarea placeholder="发布点什么..." rows="5"  maxlength="200" οnchange="this.value=this.value.substring(0, 200)" οnkeydοwn="this.value=this.value.substring(0, 200)" οnkeyup="this.value=this.value.substring(0, 200)"></textarea>
            </div>
        </div>

<!--        动态列表-->
        <div class="content">
            <div class="msg">
                <div class="user">
                    <img src="@/assets/images/friendDongtai/person02.png" alt="头像">
                    <span>用户名</span>
                </div>
                <div class="content">
                    动态内容区动态内容区动态内容区动态内容区动态内容区动态内容区动态内容区动态内容区动态内容区动态内容区动态内容区动态内容区动态内容区动态内容区动态内容区动态内容区动态内容区动态内容区动态内容区动态内容区动态内容区
                </div>
                <div class="time">
                    <span>时间戳转时间</span>
                </div>
                <div class="comment-list">
                    <div class="post-comm">
                        <input type="text" placeholder="评论点什么吧..." class="input_txt">
                        <input type="button" value="发 送" class="input_sub"/>
                    </div>
                    <div class="comment">
                        <span>用户名</span>
                        <span>:</span>
                        <span>评论内容评论内容评论内容评论内容评论内容评论内容评论内容评论内容评论内容评论内容评论内容评论内容评论内容评论内容评论内容评论内容评论内容评论内容评论内容评论内容</span>
                    </div>
                    <div class="comment">
                        <span>用户名</span>
                        <span>:</span>
                        <span>评论内容评论内容评论内容评论内容评论内容评论内容评论内容评论内容评论内容评论内容评论内容评论内容评论内容评论内容评论内容评论内容评论内容评论内容评论内容评论内容</span>
                    </div>
                </div>
            </div>
            <div class="msg">
                <div class="user">
                    <img src="@/assets/images/friendDongtai/person02.png" alt="头像">
                    <span>用户名</span>
                </div>
                <div class="content">
                    动态内容区动态内容区动态内容区动态内容区动态内容区动态内容区动态内容区动态内容区动态内容区动态内容区动态内容区动态内容区动态内容区动态内容区动态内容区动态内容区动态内容区动态内容区动态内容区动态内容区动态内容区
                </div>
                <div class="time">
                    <span>时间戳转时间</span>
                </div>
                <div class="comment-list">
                    <div class="post-comm">
                        <input type="text" placeholder="评论点什么吧..." class="input_txt">
                        <input type="button" value="发 送" class="input_sub"/>
                    </div>
                    <div class="comment">
                        <span>用户名</span>
                        <span>:</span>
                        <span>评论内容评论内容评论内容评论内容评论内容评论内容评论内容评论内容评论内容评论内容评论内容评论内容评论内容评论内容评论内容评论内容评论内容评论内容评论内容评论内容</span>
                    </div>
                    <div class="comment">
                        <span>用户名</span>
                        <span>:</span>
                        <span>评论内容评论内容评论内容评论内容评论内容评论内容评论内容评论内容评论内容评论内容评论内容评论内容评论内容评论内容评论内容评论内容评论内容评论内容评论内容评论内容</span>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    
    export default {
        name:'FriendDynamic',
        mounted() {
            if(document) {const p_container = document.querySelector('.publish-container')
    const p = p_container.querySelector('.publish')
    const p_height = p.offsetHeight
    const show_p = document.querySelector('.header .post')
    let flag = false
    show_p.addEventListener('click', function () {
        flag = !flag
        if (flag) {
            p_container.style.height = p_height + 10 + 'px'
        } else if(!flag) {
            p_container.style.height = '0'
        }
    })
    }
    
        },
    }
    
    
</script>

<style>
    @import url("../../../public/css/reset.css");
    @import url("../../../public/css/friendPost.css");
</style>