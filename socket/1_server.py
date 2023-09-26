# server.py

import socket

# define host
# method 1
HOST = socket.gethostbyname(socket.gethostname())
print(HOST)
# method 2
HOST = '192.168.100.15' # or 'localhost'
# define port
PORT = 34

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
# listen to incoming connections
server.listen(5) # allow up to 5 connections

while True:
    communication_socket, address = server.accept()
    print(f"Connected to {address}")
    message = communication_socket.recv(1024).decode('utf-8') # 1024 bytes
    print(f"Message from client is: {message}")
    communication_socket.send(f"Got your message, thank you!".encode('utf-8'))
    communication_socket.close()
    print(f"Connection with {address} ended")
