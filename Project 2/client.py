import socket

IPv4 = socket.AF_INET
IPv6 = socket.AF_INET6
UDP = socket.SOCK_DGRAM

s= socket.socket(IPv4,UDP)

dst = ('localhost',1234)
while True:
    data = input()
    s.sendto(data.encode(),dst)
    if data == 'GET':
        while True:
            d , addr = s.recvfrom(1024)
            d = d.decode()
            if d == '<<--bye-->>':
                break
            print(d)

