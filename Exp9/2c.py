import socket

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect(('127.0.0.1',9090));
data = input("Enter the data to be sent in lowercase: ")
clientSocket.send(data.encode())
data = clientSocket.recv(1024).decode()
print(data)