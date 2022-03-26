from config import *
import socket

class ServerSocket(socket.socket):
    """初始化服务器套接字"""

    def __init__(self):
        #设置为TCP类型
        super(ServerSocket,self).__init__(socket.AF_INET,socket.SOCK_STREAM)

        #绑定地址和端口号
        self.bind((SERVER_IP,SERVER_PORT))
        #设置为监听模式
        self.listen(128)