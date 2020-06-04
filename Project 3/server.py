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

# create socket
try:
    s = socket.socket(IPv4,TCP)
    s.bind((HOST,PORT))
    s.listen(1)
except :
    print('sorry, socket can not be created :(')
else:

    # rnadom generator
    rnd_gen = Random.new().read


    client , addr = s.accept()
    print('----------- Connection Established! -------------')
    # key exchange

    try:
        private_key = RSA.generate(1024,rnd_gen)
        public_key = private_key.publickey()
        client_key = client.recv(2048)
        client.send(public_key.export_key())

        private_dec = PKCS1_OAEP.new(private_key)
        client_key = RSA.import_key(client_key)
        client_enc = PKCS1_OAEP.new(client_key)


        turn = False

        while True:
            if not turn:
                i_data = client.recv(1024)
                i_data = private_dec.decrypt(i_data)
                i_data = i_data.decode()
                print(i_data)
                if i_data == BYE:
                    client.close()
                    break
            

            try:
                data = input()
                data_enc = client_enc.encrypt(data.encode())
                client.send(data_enc)
                turn = False
                if data == BYE:
                    client.close()
                    break
            except ValueError as ve:
                print(ve)
                print('>> send again:')
                turn = True
            except KeyboardInterrupt as kbi:
                print('>> next time close the program by sending "Good Bye" :(')
                break
            except :
                print('>> sorry something bad happend!')
                break


    except KeyboardInterrupt:
        print('>> next time close the program by sending "Good Bye" :(')
    except :
        print('>> Unfortunately connection closed!')