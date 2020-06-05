import socket

IPv4 = socket.AF_INET
IPv6 = socket.AF_INET6
TCP = socket.SOCK_STREAM
UDP = socket.SOCK_DGRAM

configs = {
    'IP_Address':'localhost',
    'IP_version':IPv4,
    'PORT':12345,
    'Transport_type':TCP
}


S = socket.socket(configs['IP_version'],configs['Transport_type'])

S.connect((configs['IP_Address'],configs['PORT']))
info = S.recv(1024)
if info.decode() == 'welcome':
    print(info.decode())
    try:
        while True:
            data1=input()
            if data1 == 'Exit':
                S.close()
                break
            data1=data1.encode()
            data2=input().encode()
            S.send(data1)
            S.recv(1024)
            S.send(data2)
            result =S.recv(1024)
            print(result.decode())
    except:
        print('disconnected:(')
else:
    print(info.decode())
    S.close()