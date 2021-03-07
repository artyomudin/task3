import socket
from builtins import *

HOST = '127.0.0.1' #local host
PORT = 3000 #some port

server = socket.socket(
    socket.AF_INET, #cемья адресов
    socket.SOCK_DGRAM, #UDP протокол

)
server.bind((HOST, PORT))

while True:
    data, address = server.recvfrom(4096)
    print(str(data))
    message = ('hello, is anybody in there?').encode('utf-8')
    server.sendto(message, address)