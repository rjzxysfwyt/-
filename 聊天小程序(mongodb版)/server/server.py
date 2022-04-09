from http import client
import socket
from urllib import request
from matplotlib.style import use
from server_socket import ServerSocket
from socket_wrapper import SocketWrapper
from threading import Thread
from config import *
from response_protocol import *
from db import MyMongoDB

class Server(object):
    """服务器核心类"""

    def __init__(self):
        #创建服务器套接字
        self.server_socket=ServerSocket()

        #创建请求的id和方法关联字典
        self.request_handle_function={}
        self.register(REQUEST_LOGIN,self.request_login_handle)
        self.register(REQUEST_CHAT,self.requset_chat_handle)

        #创建保存当前用户的字典
        self.clients={}
        
        #创建数据库管理对象
        self.db=MyMongoDB('db1','user')


    def register(self,request_id,handle_function):
        """再次封装消息类型和处理函数"""
        self.request_handle_function[request_id]=handle_function
    def startup(self):
        """获取客户端连接，并提供服务"""
        while True:
            #获取客户端连接
            print('正在获取客户端连接~~')
            soc,addr = self.server_socket.accept()
            print('获取到客户端连接~~')
            #使用套接字生成包装对象
            client_soc=SocketWrapper(soc)
            #收发消息 
            Thread(target=lambda:self.request_handle(client_soc)).start( )

            #关闭客户端套接字
            #soc.close()

    def request_handle(self,client_soc):
        """处理客户端请求"""
        while True:
            #接受客户端数据
            recv_data=client_soc.recv_data()
            if not recv_data:
                #没有接收到数据客户端应该已经关闭
                self.remove_offline_user(client_soc)
                client_soc.close()
                break
            #解析数据
            parse_data=self.parse_request_text(recv_data)

            #分析请求类型，并根据请求类型调用相应的处理函数
           
            handle_function=self.request_handle_function.get(parse_data['request_id'])
            if handle_function:
                handle_function(client_soc,parse_data)
            #print(recv_data)
            #client_soc.send_data('服务器接收到的是：'+ recv_data)

    def remove_offline_user(self,client_soc):
        """客户端下线的处理"""
        print("有客户端下线了~~")
        for username,info in self.clients.items():
            if info['sock']==client_soc:
                #print(self.clients)
                del self.clients[username]
                #print(self.clients)
                break

 
    def parse_request_text(self,text):
        """
        解析客户端发送来的数据
        登录消息：0001|username|password
        聊天信息：0002|username|messages
        
        """
        print('解析客户端数据'+text)
        request_list=text.split(DELIMITER)
        #按照类型解析数据
        request_data={}
        request_data['request_id']=request_list[0]

        if request_data['request_id']==REQUEST_LOGIN:
            #用户请求登陆
            request_data['username']=request_list[1]
            request_data['password']=request_list[2]

        elif request_data['request_id']==REQUEST_CHAT:
            #用户请求聊天
            request_data['username']=request_list[1]
            request_data['messages']=request_list[2]

        return request_data

    def requset_chat_handle(self,client_soc,request_data):
        """处理聊天功能"""
        print('收到聊天信息~~准备处理~~',request_data)
        #获取消息内容
        username=request_data['username']
        messages=request_data['messages']
        nickname=self.clients[username]['nickname']
        #拼接发送给客户端的消息文本
        msg=ResponseProtocol.response_chat(nickname,messages)

        #转发消息给在线用户
        for u_name,info in self.clients.items():
            if username==u_name:
                continue
            info['sock'].send_data(msg)



    def request_login_handle(self,client_soc,request_data):
        """处理登录功能"""
        print('收到登录请求~~准备处理~~')
        #获取账号密码
        username=request_data['username']
        password=request_data['password']

        #检查是否能够登录
        ret,nickname,username=self.check_user_login(username,password)

        #登陆成功则需要保存当前用户
        if ret=='1':
            self.clients[username]={'sock':client_soc,'nickname':nickname}

        #拼接返回给客户端的消息
        response_text=ResponseProtocol.response_login_result(ret,nickname,username)
        #把消息发送给客户端
        client_soc.send_data(response_text)


    def check_user_login(self,email,password):
        """检查用户是否登陆成功，并返回检查结果（0/失败，1/成功），检查依据：用户的邮箱"""
        #从数据库查询用户信息
        result = self.db.find({'email':email})

        #用户不存在，登陆失败
        if not result:
            return '0','用户名不存在',email

        #密码错误，登陆失败
        if password !=result.get('pwd'):
            return '0','密码错误',email

        #否则登录成功
        return '1', result.get('name'), email


if __name__=='__main__':
    Server().startup()
