# client.py
import socket

HOST = '192.168.100.15'
PORT = 34

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect((HOST, PORT))

socket.send('Hello world'.encode('utf-8'))
print(socket.recv(1024).decode('utf-8'))
