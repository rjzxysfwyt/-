from config import *


class RequestProtocol(object):
    """响应拼接"""

    @staticmethod
    def request_login_result(username,password):

        """0001|user1|111111         类型|账号|密码"""

        return DELIMITER.join([REQUEST_LOGIN,username,password])

    @staticmethod
    def request_chat(username,message):
        """
        拼接聊天响应，数据格式为 ：“0002|user1|msg”   类型|账号|消息
       
        """

        return DELIMITER.join([REQUEST_CHAT,username,message])

