#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 文件名：client.py
import struct
import socket # 导入 socket 模块

class MyClient:
    def __init__(self):
        self.host = socket.gethostname() #获取本地主机名
        self.dhost = '172.18.5.30' #设置连接服务器的地址
        self.port = 12345 #设置端口好

    def startClient(self):
        s = socket.socket() #创建socket对象
        s.connect((self.dhost, self.port)) #创建连接
        while True:
            self.recvAndSendMessage(s)
        s.close()

    def recvAndSendMessage(self,sSocket):
        # print(sSocket.recv(1024).decode('gb2312')) #接收信息
        message=input('%s : ' % self.host) #输入聊天信息
        message=('%s : %s'%(self.host,message)).encode('gb2312') #生成带用户信息的聊天信息
        sSocket.send(message) #发送聊天信息

def main():
    startClinet=MyClient()
    startClinet.startClient()

if __name__=="__main__":
    main()

