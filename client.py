import socket                   # Import socket module

s = socket.socket()             # Create a socket object
host = socket.gethostname()     # Get local machine name
port = 60015            # Reserve a port for your service.

s.connect((host, port))
s.send("Hello server!")
data=""
with open('received_file', 'wb') as f:
    print 'file opened'
    while True:
        print('receiving data...')
        data= s.recv(1024)
	
       # print('data=%s', (data))
        if not data:
            break
        # write data to a file
        #f.write(data)

#f.close()
	print('Successfully get the file')
	import  numpy
	k=list(data)
	#print(k)
	m=k.index("*")
	s1="".join(k[:m-1])
	key="".join(k[m+1:m+9])

	
	text=s1
	key=key
	
  

	n = 4
	cip_matrix = []
	v = 0
	u = 16
	#print("**********\n")
	#print(text)
	#print(key)
	#print("THE CORRESPONDING CIPHER MATRIX FOR THE CIPHERTEXT IS: ")
#	print(len(text))
	for j in range(len(text) // 16 ):
	    m = []
	    for i in range(v, u, n):
		#print(text[i:i + n])
		m.append(list(text[i:i + n]))
	   # print(m)
	    #for i in m:
		#print(i)
	    
	    v = u
	    u = u + 16
	    cip_matrix.append(m)
	   # print(m)
	#print(cip_matrix)
	##################################################################################
	#print("EQUIVALENT ASCII MATRIX FOR CIPHERTEXT IS:")
	ascii = [[[ord(ch) for ch in word] for word in words] for words in cip_matrix]
#	for i in ascii:
	 #   for j in i:
	 #      print(j)
#	    print("\n")
		
#	print(len(ascii))
	####################################################################################
#	print("encoded key is :")
#	print(key)
#	print("DECODED KEY : ")
	decodedkey=""
	for i in range(0, len(key)):
	    if (key[i] == "A"):
		decodedkey+= "00"
	    elif (key[i] == "G"):
		decodedkey += "01"
	    elif (key[i] == "C"):
		decodedkey += "10"
	    else:
		decodedkey += "11"
#	print(decodedkey)
	###################################################################################
#	print("KEY MATRIX :")
	key_matrix=[]
	p=0
	for i in range(0, 4):
	    m1 = []
	    for j in range(0, 4):
		m1.append(int(decodedkey[p]))
		p=p+1
#	    print(m1)
	    key_matrix.append(m1)
	#######################################################################################
#	print("VERTICAL ROTATION (COLUMN):")
	col_matrix=[]
	hor_trans=[]
	for i in ascii:
	    hor_trans.append(numpy.transpose(i).tolist())
	rot=[]
	k = 4
	for i in hor_trans:
	    l1 = []
	    k=4
	    for j in i:
		j1 = j[k:] + j[:k]
		l1.append(j1)
		k = k - 1
	    rot.append(l1)
	for i in rot:
	    col_matrix.append(numpy.transpose(i).tolist())
#	for i in col_matrix:
#	    for j in i:
#		print(j)
	#####################################################################################
#	print("ROW ROTATION HORIZONTAL: ")
	row_matrix=[]
	k = 4
	for i in col_matrix:
	    l1 = []
	    k=4
	    for j in i:
		j1 = j[k:] + j[:k]
		l1.append(j1)
		k = k - 1
	    row_matrix.append(l1)
#	for i in row_matrix:
#	    for j in i:
#		print(j)
#	print(len(row_matrix))
	########################################################################################
#	print("SUBTRACTION OF  KEY MATRIX AND ROW MATRIX :")
	sub_matrix=[]
	for p in row_matrix:
	    #print(p)
	    lp = []
	    #for i in range(len(ascii_trans)):
	    for j in range(4):
		ad = [(x1-x2) for (x1,x2) in zip(p[j], key_matrix[j])]
		#print(ad)
		lp.append(ad)
	    sub_matrix.append(lp)
#	for i in sub_matrix:
#	    for j in i:
#		print(j)
	#######################################################################################
#	print("TRANSPOSE OF THE RESULTING SUB MATRIX IS: ")
	ascii_trans = []
	for i in sub_matrix:
	    ascii_trans.append(numpy.transpose(i).tolist())
#	for i in ascii_trans:
#	    for j in i:
#		print(j)
	###############################################################################
#	print("CHARACTER MATRIX :")
	decip_matrix= [[[chr(ch) for ch in word] for word in words] for words in ascii_trans]
#	for i in decip_matrix:
#	    for j in i:
#		print(j)
	###############################################################################
#	print("THE DECIPHERED PLAINTEXT :")
#	print(decip_matrix)
	decip_plaintext=""
	for i in decip_matrix:
	    for j in i:
		for g in j:
		    decip_plaintext = decip_plaintext + str(g)

	#print(decip_plaintext)
	print('connection closed')

	print("Decrypted text is:"+decip_plaintext)
s.close()
