import socket
from server_socket import ServerSocket

class Server(object):
    """服务器核心类"""

    def __init__(self):
        #创建服务器套接字
        self.server_socket=ServerSocket()

    def startup(self):
        """获取客户端连接，并提供服务"""
        #获取客户端连接
        print('正在获取客户端连接~~')
        soc,addr = self.server_socket.accept()
        print('获取到客户端连接~~')
        #收发消息
        recv_data=soc.recv(512)
        print(recv_data.decode('utf-8'))
        soc.send('成功连接到服务器~~'.encode('utf-8'))

        #关闭客户端套接字
        soc.close()

if __name__=='__main__':
    Server().startup()
