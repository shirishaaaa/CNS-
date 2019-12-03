import socket                   # Import socket module


import numpy
import random
#getting matrix
with open("doc" + ".txt", 'r') as myfile:
    FILE = myfile.read()
text=FILE
plaintext = text.replace(' ', '')
if(len(plaintext)<16):
    plaintext = plaintext + (16 - len(plaintext) ) * "."
g=len(plaintext)
if(g%16 != 0):
    plaintext=plaintext + (16-g%16)*"."
#print("THE PLAINTEXT IS: " + plaintext)
#print(len(plaintext))
###################################################################
n = 4
input_matrix = []
v = 0
u = 16
#print("THE CORRESPONDING INPUT MATRIX FOR THE PLAINTEXT IS: ")
for j in range(len(plaintext) // 16 ):
    m = []
    for i in range(v, u, n):
        m.append(list(plaintext[i:i + n]))
    #for i in m:
     #   print(i)
    v = u
    u = u + 16
    input_matrix.append(m)
##################################################################
#print(len(input_matrix))
#print(input_matrix)
# print(len(input_matrix))
# convert to # -*- coding: ascii
ascii = [[[ord(ch) for ch in word] for word in words] for words in input_matrix]
#print("THE EQUIVALENT ASCII MATRIX FOR PLAINTEXT IS: ")
#for i in ascii:
#    for j in i:
#       print(j)
#print(ascii)
#print(len(ascii))
##################################################################
# transpose of ascii matrix
ascii_trans = []
for i in ascii:
    ascii_trans.append(numpy.transpose(i).tolist())
#print("THE TRANSPOSE OF THE ASCII MATRIX IS : ")
#for i in ascii_trans:
#    for j in i:
#        print(j)
# print(ascii_trans)
#print(len(ascii_trans))
#######################################################################
# to generate the key matrix using random order in range(0,127)
key_matrix = []
#print("THE KEY MATRIX :")
for i in range(0, 4):
    m1 = []
    for j in range(0, 4):
        m1.append(random.randrange(0, 128))
#    print(m1)
    key_matrix.append(m1)

# print(key_matrix)
# to perform modular operation to implement dna sequencing
##################################################################
key_matrix_mod = [[k % 2 for k in row] for row in key_matrix]
#print("THE MODULAR KEY MATRIX :")
#for i in key_matrix_mod:
 #   print(i)
# print(key_matrix_mod)
######################################################################
# add input_matrix and key

added_matrix = []

for p in ascii_trans:
    #print(p)
    lp = []
    #for i in range(len(ascii_trans)):
    for j in range(4):
        ad = [sum(o) for o in zip(p[j], key_matrix_mod[j])]
        #print(ad)
        lp.append(ad)
    added_matrix.append(lp)
#print("ADDITION OF  MODULAR KEY MATRIX AND ASCII MATRIX :")
#for i in added_matrix:
#    for j in i:
#        print(j)
#print(added_matrix)
#print(len(added_matrix))
############################################################################
# row rotation horizontally
hor_matrix = []

k = 0
#print("check rowthing")
#print(len(added_matrix))
for i in added_matrix:
    l1 = []
    k=0
    for j in i:
        j1 = j[k:] + j[:k]
        l1.append(j1)
        k = k + 1
    hor_matrix.append(l1)
#print("ROW ROTATION HORIZONTAL:")
#for i in hor_matrix:
#    for j in i:
#        print(j)
# print(hor_matrix)
####################################################################
# row rotation vertically
hor_trans = []
for i in hor_matrix:
    hor_trans.append(numpy.transpose(i).tolist())
# print(hor_trans)
rotat_matrix = []
k = 0
for i in hor_trans:
    l1 = []
    k=0
    for j in i:
        j1 = j[k:] + j[:k]
        l1.append(j1)
        k = k + 1
    rotat_matrix.append(l1)
# print(rotat_matrix)
ver_trans = []
for i in rotat_matrix:
    ver_trans.append(numpy.transpose(i).tolist())
#print("VERTICAL ROTATION (COLUMN):")
#print(len(ver_trans))
#for i in ver_trans:
#    for j in i:
#        print(j)
# print(ver_trans)
####################################################################
# to compute cipher matrix
cipher_matrix = [[[chr(ch) for ch in word] for word in words] for words in ver_trans]
#print("CIPHER MATRIX :")
#for i in cipher_matrix:
 #   for j in i:
 #       print(j)
# print(cipher_matrix)
# CIPHER TEXT
ciphertxt = ""
for i in cipher_matrix:
    for j in i:
        for g in j:
            ciphertxt = ciphertxt + str(g)
#print("THE CIPHER TEXT IS :")
#print(ciphertxt)
###########################################################################33
# dna sequencing for the key matrix
binstr = ""
for i in key_matrix_mod:
    for j in i:
        binstr = binstr + str(j)
# print(binstr)
encryptedkey = ""
for i in range(0, len(binstr), 2):
    if (binstr[i:i + 2] == "00"):
        encryptedkey += "A"
    elif (binstr[i:i + 2] == "01"):
        encryptedkey += "G"
    elif (binstr[i:i + 2] == "10"):
        encryptedkey += "C"
    else:
        encryptedkey += "T"
#print("KEY ENCRYPTION IN THE FORM OF DNA SEQUENCE:")
#print(encryptedkey)
t=""
t+=ciphertxt
#cipherk="".join(list(map(str,cipherk)));
#print("Encrypted text is:"+cipherk)
t+="*"
t+=encryptedkey
port = 60015                  # Reserve a port for your service.
s = socket.socket()             # Create a socket object
host = socket.gethostname()     # Get local machine name
s.bind((host, port))            # Bind to the port
s.listen(5)                     # Now wait for client connection.

print 'Server listening....'

while True:
    conn, addr = s.accept()     # Establish connection with client.
    print 'Got connection from', addr
    data = conn.recv(1024)
    print('Server received', repr(data))

    '''filename='mytext.txt'
    f = open(filename,'rb')
    l = f.read(1024)
    while (l):
       conn.send(l)
       print('Sent ',repr(l))
       l = f.read(1024)
    f.close()
'''
    conn.send(t)
    print('Sent ',repr(t))
    print('Done sending')
   # conn.send('thank you')
    conn.close()
