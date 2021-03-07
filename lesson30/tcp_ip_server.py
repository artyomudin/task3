import socket
from builtins import print

HOST = '127.0.0.1' #local host
PORT = 3000 #some port

server = socket.socket(
    socket.AF_INET, #cемья адресов
    socket.SOCK_STREAM, #TCP\IP протокол

) #создаем экземпляр класса сокет. отвечает за отправку и получение сообщений

server.bind((HOST, PORT)) #даем серверу адрес

server.listen(5)#разрешаем серверу получать данные, укзываем кол-во подключений
print('server is listening')

while True:
    user_socket,adress = server.accept()# принимаем входящее подключение, разделяем на адресс и собственный сокет
    print(f'user: {user_socket} connected!')
    user_socket.send('you are connected'.encode('utf-8'))#сообщаем клиенту, что он подключен
    data = user_socket.recv(2048)
    print(data.decode('utf-8'))

