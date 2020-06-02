import socket

S = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

S.bind(("localhost",12345))
S.listen()


client , addr = S.accept()

num1 = client.recv(1024)
print("num1 "+num1.decode())
client.send(b'num1 received')
num2 = client.recv(1024)
print('num2 '+num2.decode())
num3 = int(num1)+int(num2)
print(num3)
client.send(str(num3).encode())
client.close()