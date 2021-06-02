print("*****Ceaser Cypher*****")
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

print("*****MonoAlphabetic Cipher*****")
lst1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
lst2 = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm']
text = input("Enter The Text:")
ls = []
ls1 = []
l1 = len(lst1)
for i in text:
    if(i in lst1):
        ls.append(i)
for a in range(len(ls)):
    ind = lst1.index(ls[a])
    ls1.append(lst2[ind])
MA = ''.join(map(str, ls1))
print("Monoalphabetic Cipher :",MA)

print("*****BruteForce Attack*****")
for l in range(1, 27):
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
	print("Plain text for Key" + str(l)+":", BFA.join(lst3))
