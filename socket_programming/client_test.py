import socket               # Import socket module

s = socket.socket()         # Create a socket object
host = 'localhost'
port = 8080
s.connect((host, port))
print s.recv(1024)
s.close                     # Close the socket when done
