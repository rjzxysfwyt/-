class SocketWrapper(object):
    """套接字包装类"""
    def __init__(self,sock):
        self.sock=sock

    def recv_data(self):
        """接收数据并解码为字符串"""
        try:
            return self.sock.recv(512).decode('utf-8')
        except:
            return ""

    def send_data(self,message):
        """把字符串编码并发送给客户端"""
        return self.sock.send(message.encode('utf-8'))

    def close(self):
        """关闭套接字"""
        self.sock.close()