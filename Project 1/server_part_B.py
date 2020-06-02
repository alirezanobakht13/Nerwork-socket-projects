import socket
import threading

IPv4 = socket.AF_INET
IPv6 = socket.AF_INET6
TCP = socket.SOCK_STREAM
UDP = socket.SOCK_DGRAM

# Application Protocol between server and client
def protocol(client):
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

def accepter(sock):
    while True:
        client , addr = sock.accept()
        t = threading.Thread(target=protocol,args=(client,))
        t.start()

S1 = socket.socket(IPv4,TCP)
S1.bind(('localhost',12345))
S1.listen(4)
S2 = socket.socket(IPv4,TCP)
S2.bind(('localhost',12346))
S2.listen(4)

t1 = threading.Thread(target=accepter,args=(S1,))
t2 = threading.Thread(target=accepter,args=(S2,))
t1.start()
t2.start()
