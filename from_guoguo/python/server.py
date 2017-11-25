#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 文件名：server.py
import socket #导入 socket 模块
import select #导入select 模块
import sys

class MyServer:
    def __init__(self):
        self.host = socket.gethostname() #获取本地主机名
        self.port = 12345 #设置端口

    def startServer(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #创建socket对象
        s.bind((self.host, self.port)) #绑定端口
        s.listen(5) #等待客户端连接
        print('已启动聊天室')
        s_list = []
        # print(s_list)
        s_list.append(s)
        while True:
            # import ipdb;ipdb.set_trace()
            read_sockets, write_sockets, error_sockets = select.select(s_list , [], [])
            print(read_sockets,s_list)
            for sock in read_sockets:
                if sock == s:
                    c = self.createAccept(sock,write_sockets,s,s_list)
                    s_list.append(c)
                else:
                    try:                                            #对连接断开进行异常捕获
                       self.recvAndSendMessage(c)
                    except Exception as e:                          #异常处理
                        self.unconnectAccept()
                        s_list.remove(c)
                    # c.close() # 关闭连接

    def createAccept(self,sAccept,write_sockets,s,s_list):
        cAccept , addr = sAccept.accept() #建立客户端连接。
        # print('有一个用户连接进入聊天室了，连接地址：', sAccept) #提示连接用户的IP地址
        print('有一个用户连接进入聊天室了，连接地址：', addr) #提示连接用户的IP地址
        for fd in  s_list:
            if fd != s:
                message=('ni已经进入聊天室').encode('gb2312')       #连接提示信息
                fd.send(message)
        return cAccept

    def recvAndSendMessage(self,c):
        data = c.recv(1024).decode('gb2312')    #接收来自客户端的信息
        if data:
            print(data)
        # message=input('%s : ' % self.host)      #输入回复信息
        # message=('%s : %s'%(self.host,message)).encode('gb2312')#生成对服务器信息的信息，并转换为字节
        # c.send(message)                         #发送信息

    def unconnectAccept(self):
        print('%s 断开连接' % self.host)                 #打印异常信息

def main():
    myServer=MyServer()
    myServer.startServer()

if __name__=="__main__":
    main()


