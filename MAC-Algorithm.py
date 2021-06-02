import hashlib
print("First Level")
PT = input("Please Enter the Message:")
result = hashlib.sha512(PT.encode())
pt = result.hexdigest()
print("The hexadecimal equivalent of SHA512 is : ", result.hexdigest())
lst = []
lst.append(PT)
lst.append('XX')
lst.append(result.hexdigest())
print("Final Result is:"+"".join(lst))
RValue = input("Enter the Reciever Message:")
result1 = hashlib.sha512(RValue.encode())
rvalue = result1.hexdigest()
if(pt==rvalue):
    print("Same Message")
else:
    print("Value Errored!")
print("Ceaser Cipher Level")
plaintext = input("Enter plain Text:")
l = len(plaintext)
lst=[]
key = input("Enter the Key:")
if key.isdigit():
    for i in range(l):
        if(plaintext[i].islower()):
            tcs = ((ord(plaintext[i])+int(key)-97)%26)+97
            cs=chr(tcs)
            lst.append(cs)
        else:
            tcs = ((ord(plaintext[i])+int(key)-65)%26)+65
            cs=chr(tcs)
            lst.append(cs)

    CT = ''.join(map(str, lst))
    print("Ceaser Cyper Text:",CT)
else:
    k=ord(key)-96
    for i in range(l):
        if(plaintext[i].islower()):
            tcs = ((ord(plaintext[i])+int(k)-97)%26)+97
            cs=chr(tcs)
            lst.append(cs)
        else:
            tcs = ((ord(plaintext[i])+int(k)-65)%26)+65
            cs=chr(tcs)
            lst.append(cs)
    CT = ''.join(map(str, lst))
    print("Ceaser Cyper Text:",CT)
result2 = hashlib.sha512(plaintext.encode())
pt1 = result2.hexdigest()
print("The hexadecimal equivalent of SHA512 is : ", result2.hexdigest())
lst1 = []
lst2 = []
lst1.append(CT)
lst1.append('XX')
lst1.append(result2.hexdigest())
print("Final Result is:"+"".join(lst1))
l = int(input("Enter key for decryption:"))
lst3 = []
for i in CT:
	if i.islower():
		if(ord(i) - l < 97):
			lst3.append(chr(122 - (96 - (ord(i) - l))))
		else:
			lst3.append(chr((ord(i) - l)))
	elif i.isupper():
		if(ord(i) - l < 65):
			lst3.append(chr(90 - (64 - (ord(i) - l))))
		else:
			lst3.append(chr((ord(i) - l)))
	BFA = ''
print("Plain text for Key"+":", BFA.join(lst3))
dec = BFA.join(lst3)
result3 = hashlib.sha512(dec.encode())
hval = result3.hexdigest()
if(pt1==hval):
    print("Correct!!")
else:
    print("Value Altered!!")
