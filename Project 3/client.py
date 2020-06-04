import socket
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto import Random

# constants
IPv4 = socket.AF_INET
TCP = socket.SOCK_STREAM
HOST = 'localhost'
PORT = 1234

BYE = 'Good Bye'

# rnadom generator
rnd_gen = Random.new().read


# client keys
private_key = RSA.generate(1024,rnd_gen)
public_key = private_key.publickey()
private_dec = PKCS1_OAEP.new(private_key)

try:
    s = socket.socket(IPv4,TCP)
except :
    print('sorry, unable to create socket')
else:
    try:
        s.connect((HOST,PORT))
        print('----------- Connection Established! -------------')
    except ConnectionRefusedError:
        print('>> Are you sure any server is listening on defined host or port?!')
    except :
        print('>> sorry something bad happend!')
    else:
        try:
            s.send(public_key.export_key())
            server_key = s.recv(2048)
            server_key = RSA.import_key(server_key)
            server_enc = PKCS1_OAEP.new(server_key)

            while True:
                try:
                    data = input()
                    enc = server_enc.encrypt(data.encode())
                    s.send(enc)
                    if data == BYE:
                        s.close()
                        break
                except ValueError as ve:
                    print(ve)
                    print('>> send again:')
                    continue
                except KeyboardInterrupt as kbi:
                    print('>> next time close the program by sending "Good Bye" :(')
                    break
                except :
                    print('>> sorry something bad happend!')
                    break
                i_data = s.recv(1024)
                i_data = private_dec.decrypt(i_data).decode()
                print(i_data)
                if i_data == BYE:
                    s.close()
                    break
        except KeyboardInterrupt as kbi:
            print('>> next time close the program by sending "Good Bye" :(')
        except :
            print('>> Unfortunately connection closed!')
            

    
