import socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1',9090))
data = input("Enter ping or pong: ")
client.send(data.encode())
data = client.recv(1024).decode()
print(data)