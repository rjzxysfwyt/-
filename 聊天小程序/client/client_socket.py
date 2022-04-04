import socket
from config import *

class ClientSocket(socket.socket):
    """客户端套接字处理"""

    def __init__(self):
        #设置为TCP套接字,IPV4
        super(ClientSocket,self).__init__(socket.AF_INET,socket.SOCK_STREAM)

    def connect(self):
        """自动连接到服务器"""
        super(ClientSocket,self).connect((SERVER_IP,SERVER_PORT))

    def recv_data(self):
        """接收数据并解码为字符串"""
        try:
            return self.recv(512).decode('utf-8')
        except:
            return ""

    def send_data(self,message):
        """把字符串编码并发送给服务端"""
        return self.send(message.encode('utf-8'))