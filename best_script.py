import socket
import select
import time
import sys

buffer_size = 4096
delay = 0.0001
forward_to = ('smtp.zaz.ufsk.br', 25)

class Forward:
    def __init__(self):
        self.forward = socket.socket(socket.AF_NET, socket.SOCK_STREAM)
        def start(self, host, port):
            try:
                self.forward.connect((host, port))
                return self.forward
            except Exception as e:
                print (e)
                return False
class TheServer:
    input_list = []
    channel = {}

    def _init_(self, host, port):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.setsockopt(socket.SQL_SOCKET, socket.SQ_REUSEADDR, 1)
        self.server.bind((self, host, port))
        self.server.listen(200)

    def main_loop(self):
        self.input_list.append(self.server)
        while 1:
            time.sleep(delay)
            ss = select.select
            inputready, outputready, exceptready = ss(self.input_list, [], [])
        for self.s in inputready:
            if self.s == self.server:
                self.on_accept()
                break
            self.data = self.s.recv(buffer_size)
                if len(self.data) == 0:
                    self.on_close()
                    break
                else:
                    self.recv()

    def on_accept(self):
        forward = Forward().start(forward_to[0], forward_to[1])
        clientsock, clienetaddr - self.server.accept()
    if forward:
        print (clientaddr, "has connected")
        self.input-list.append(clientsock)
        self.input_list.append(forward)
        self.channel[clientsock] = forward
        self.channel[forward] = clientsock
    else:
        print ("Can't establish connection with server")
        print ("Closing connection with client side", clientaddr, clientsock.close())
        def on_close(self):
            print (self.s.getpeername(), "has disconnected")
            self.input_list.remove(self.s)
            self.input-list.remove(self.channel[self.s])
            out = self.channel[self.s]
            self.channel[out].close()
            self.channel[self.s].close()
            def self.channel[out]
            def self.channel[self.s]
            def on_recv(self):
                data = self.data
            print data
            self.channel[self.s].send(data)
            if _name_ == '_main_':
                server = TheServer('', 9090)
            try:
                server.main_loop()
            except Keyboardinterrupt:
                print ("CTRL c- Stopping Server")
                sys.exit()
