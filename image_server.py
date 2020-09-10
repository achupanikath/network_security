from socket import socket, gethostbyname, AF_INET, SOCK_DGRAM
import sys
import re
import struct
from RSA import decrypt
import des


PORT_NUMBER = 5000
SIZE = 8192

#hostName = gethostbyname( '192.168.1.3' )
hostName = gethostbyname( 'DE1_SoC' )

mySocket = socket( AF_INET, SOCK_DGRAM )
mySocket.bind( (hostName, PORT_NUMBER) )

print ("Test server listening on port {0}\n".format(PORT_NUMBER))
client_public_key = ()
des_key = ""
coder = des.des()
while True:
        (data,addr) = mySocket.recvfrom(SIZE)
        data=data.decode()
        if data.find('public_key')!=-1: #client has sent their public key\
            ###################################your code goes here#####################################
            #retrieve public key and private key from the received message (message is a string!)
            test = data.split()
            public_key_e = int(test[1])
            public_key_n = int(test[2])
            client_public_key = (public_key_e, public_key_n)
            print('public key is : %d, %d'%(public_key_e, public_key_n))
        elif data.find('des_key')!=-1: #client has sent their DES key
            ###################################your code goes here####################
            #read the next 8 bytes for the DES key by running (data,addr) = mySocket.recvfrom(SIZE) 8 times and then decrypting with RSA
            DES_decoded = ""
            for i in range(0, 8):
                (data, addr) = mySocket.recvfrom(SIZE)
                DES_decoded += decrypt(client_public_key, int(data))
            #now we will receive the image from the client
            (data, addr) = mySocket.recvfrom(SIZE)
            #decrypt the image
            ###################################your code goes here####################
            #the received encoded image is in data
            #perform des decryption using des.py
            #the final output should be saved in a byte array called rr_byte
            rr_byte = bytearray()
            rr_byte = coder.decrypt(DES_decoded, data)
            #write to file to make sure it is okay
            file2 = open(r'penguin_decrypted.jpg', "wb")
            file2.write(bytes(rr_byte, "ISO-8859-1"))
            file2.close()
            print('decypting image completed')
            break
        else:
            continue
