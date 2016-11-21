import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = 'localhost'
port = 8080

s.bind((host, port))

s.listen(5)

while 1:
    c ,address = s.accept()
    print('get the connection from ',address)
    c.send('<h1>thanks for your connection</h1>')
    c.close()




