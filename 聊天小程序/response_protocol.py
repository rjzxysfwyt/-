from config import *

class ResponseProtocol(object):
    """响应拼接"""

    @staticmethod
    def response_login_result(result,nickname,username):

        """
        拼接登录响应，数据格式为 ：“响应编号|登录结果|用户昵称|用户名”
        result：0代表登陆失败，1代表登陆成功
        nickname：如登录失败，则为空字符
        username：如登录失败，则为空字符
        """
        return DELIMITER.join([RESPONSE_LOGIN_RESULT,result,nickname,username])

    def response_chat(nickname,messages):
        """
        拼接聊天响应，数据格式为 ：“响应编号|用户昵称|聊天信息”
       
        """

        return DELIMITER.join([REQUEST_CHAT,nickname,messages])

