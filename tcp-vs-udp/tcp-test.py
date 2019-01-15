import socket
import sys

host = 'localhost'  
port = 8888
buffersize = 8
server_address = (host, port) 

def start_TCP_server():
    socket_TCP = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket_TCP.bind(server_address)
    socket_TCP.listen(1)

    print("TCP server is running...")

    while True:    
        client, client_address = socket_TCP.accept()

        while True:
            data = client.recv(buffersize)
            if not data: break
            client.sendall(data)

        client.close()