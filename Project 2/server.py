import socket

IPv4 = socket.AF_INET
IPv6 = socket.AF_INET6
UDP = socket.SOCK_DGRAM

msgs = []

s= socket.socket(IPv4,UDP)
s.bind(('localhost',1234))

BYE = '<<--bye-->>'.encode()

while True:
    data , addr = s.recvfrom(1024)
    data = data.decode()
    if data == 'GET':
        for msg in msgs:
            s.sendto(msg.encode(),addr)
        s.sendto(BYE,addr)
    elif data[:4] == 'POST':
        if data[5:] != '<<--bye-->>':
            msgs.append(data[5:])

