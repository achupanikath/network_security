from socket import socket, gethostbyname, AF_INET, SOCK_DGRAM
import sys
import re
from RSA import decrypt
PORT_NUMBER = 5000
SIZE = 1024

hostName = gethostbyname( 'DE1_SoC' )
#hostName = gethostbyname( 'DESKTOP-A30LB1P' )

mySocket = socket( AF_INET, SOCK_DGRAM )
mySocket.bind( (hostName, PORT_NUMBER) )

print ("Test server listening on port {0}\n".format(PORT_NUMBER))
client_public_key = ()
while True:
        (data, addr) = mySocket.recvfrom(SIZE)
        data = data.decode()
        if data.find('public_key')!=-1: #client has sent their public key\
            #retrieve public key and private key from the received message (message is a string!)
            test = data.split()
            public_key_e = int(test[1])
            public_key_n = int(test[2])
            client_public_key = (public_key_e,public_key_n)
            print('public key is : %d, %d' % (public_key_e, public_key_n))
        else:
            cipher = int(data)
            print(cipher)
            #print(str(cipher) + ':')
            data_decoded = decrypt(client_public_key, cipher)
            print(str(cipher) + ':' + data_decoded)

sys.ext()
#What could I be doing wrong?
