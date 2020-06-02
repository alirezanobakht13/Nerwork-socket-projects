import socket

S = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

S.connect(("127.0.0.1",12345))
num1 = 1
num2 = 2
data1 = str(num1).encode()
data2 = str(num2).encode()
S.send(data1)
S.recv(1024)
S.send(data2)
result =S.recv(1024)
print(result.decode())
S.close()