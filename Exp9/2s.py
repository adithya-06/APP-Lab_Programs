import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.1',9090))
server.listen()
while True:
    clientConn, clientAdd = server.accept()
    print("Accepted connection from %s %s" % (clientAdd[0], clientAdd[1]))
    data = clientConn.recv(1024).decode()
    print(data.upper())
    transform = data.upper()
    clientConn.send(transform.encode())
