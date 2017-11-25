import socket               # Import socket module

s = socket.socket()         # Create a socket object
# host = 'localhost'
host = 'www.baidu.com'
# port = 8080
port = 80

s.connect((host, port))
print s.recv(1024)
s.close                     # Close the socket when done
