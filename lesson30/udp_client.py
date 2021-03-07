import socket
from builtins import *

HOST = '127.0.0.1' #local host
PORT = 3000 #some port

client = socket.socket(
    socket.AF_INET, #cемья адресов
    socket.SOCK_DGRAM, #UDP протокол

)
message = 'just nod if you can hear me'
client.sendto(message.encode('utf-8'), (HOST, PORT))
data, address = client.recvfrom(4096)
print('server says:')
print(str(data))
client.close()