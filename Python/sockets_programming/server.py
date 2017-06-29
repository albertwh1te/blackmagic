# -*- coding: utf-8 -*-
import socket
import time
import threading


def tcp_server(socket,addr):
    print('accept connection from {addr}').format(addr=addr)
    socket.send("hi i am mark's server")
    while 1:
        data = socket.recv(1024)
        # for human reason
        time.sleep(2)
        if data == "exit" or not data:
            break
        print('i head {}'.format(data))
        socket.send('the server head {}'.format(data))
    socket.close()
    print("this is end")


def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('127.0.0.1', 9999))
    # s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.listen(10)
    while 1:
        sock,addr = s.accept()
        t = threading.Thread(
            target=tcp_server,
            args=(sock,addr)
        )
        t.start()


if __name__ == '__main__':
    main()
