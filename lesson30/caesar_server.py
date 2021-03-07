import socket
from builtins import *
from my_func import *



#    data = input('input a phrase here: ')
#    key = int(input('input a key here: '))


HOST = '127.0.0.1' #local host
PORT = 3000 #some port

server = socket.socket(
    socket.AF_INET, #cемья адресов
    socket.SOCK_STREAM, #TCP\IP протокол

) #создаем экземпляр класса сокет. отвечает за отправку и получение сообщений

server.bind((HOST, PORT)) #даем серверу адрес

server.listen(5)#разрешаем серверу получать данные, укзываем кол-во подключений
print('server is listening')


user_socket,adress = server.accept()# принимаем входящее подключение, разделяем на адресс и собственный сокет
try:
    print(f'user: {user_socket} connected!')
    while True:
        data = user_socket.recv(2048)
        data = caesar_alg(data)
        user_socket.send(data)
finally:
    user_socket.close()


