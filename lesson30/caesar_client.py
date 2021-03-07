import socket
from builtins import print, input

HOST = '127.0.0.1' #local host
PORT = 3000 #some port

"""client = socket.socket(
    socket.AF_INET, # устанавливаем те же протоколы,
    socket.SOCK_STREAM, # что и у сервера
)#создаем экземпляр класса сокет. отвечает за отправку и получение сообщений

client.connect((HOST, PORT))# даем клиенту адрес сервера, куда ему обращаться

while True:
    data = client.recv(2048)# получаем информацию от сервера, задаем размер пакета
    print(data.decode('utf-8'))#печатаем наши данные
    client.send(input(':::').encode('utf-8'))"""

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as f:
    f.connect((HOST, PORT))
    message = input("enter your test here: ")
    f.sendall(message.encode())
    data = f.recv(1024).decode()

print(f"result: {data}.")
