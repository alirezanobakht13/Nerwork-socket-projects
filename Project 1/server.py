import socket
import threading

IPv4 = socket.AF_INET
IPv6 = socket.AF_INET6
TCP = socket.SOCK_STREAM
UDP = socket.SOCK_DGRAM

#Change configurations here
configs = {
    'IP_Address':'localhost',
    'IP_version':IPv4,
    'PORT':12346,
    'Transport_type':TCP,
    'Clients_limit':2,
    'timeout':2    #choose your timeout in second or None if you don't need timeout
}


S = socket.socket(configs['IP_version'],configs['Transport_type'])

S.bind((configs['IP_Address'],configs['PORT']))
S.listen(configs['Clients_limit']+2)

active_clients = 0

# Application Protocol between server and client
def protocol(client):
    global active_clients
    client.send(b'welcome')
    while True:
        try:
            num1 = client.recv(1024)
            client.send(b'num1 received')
            num2 = client.recv(1024)
            try:
                num3 = int(num1)+int(num2)
                print(num3)
                client.send(str(num3).encode())
            except:
                client.send(b'Invalid inputs')
        except:
            client.close()
            active_clients-=1



# mainloop
while True:
    client , addr = S.accept()
    if active_clients < configs['Clients_limit'] :
        active_clients+=1
        client.settimeout(configs['timeout'])
        t = threading.Thread(target=protocol,args=(client,))
        t.start()
    else:
        client.send(b'Server Is Busy')
        client.close()




