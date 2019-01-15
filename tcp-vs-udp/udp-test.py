import socket
import sys

host = 'localhost'  
port = 8888
buffersize = 8
server_address = (host, port) 

def start_UDP_server():
    socket_UDP = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    socket_UDP.bind(server_address)

    print("UDP server is running...")

    while True:
        data, from_address = socket_UDP.recvfrom(buffersize)

        if not data:
            break
        socket_UDP.sendto(data, from_address)    
    socket_UDP.close()

def manage_UDP_client():
    pass
