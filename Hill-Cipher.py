import numpy as np
key = input("Enter the Key:")
plaintext = input("Enter the Plaintext:")
print("*****Encryption*****")
Gkey = []
Gkey1 = []
plain = []
plain1 = []
lst1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
if(len(key)==4 or len(key)==9 or len(key)==16):
    Gkey = list(key.strip())
    print(Gkey)
    if(len(key)==4):
        Gkey = np.array(Gkey)
        Gkey = np.reshape(Gkey,(2,2))
        print("Matrix Generated is:",Gkey)
        for i in range(len(key)):
            a = lst1.index(key[i])
            Gkey1.append(a)
        print("Indexing of alphabets:",Gkey1)
    elif(len(key)==9):
        Gkey = np.array(Gkey)
        Gkey = np.reshape(Gkey,(3,3))
        print("Matrix Generated is:",Gkey)
        for i in range(len(key)):
            a = lst1.index(key[i])
            Gkey1.append(a)
        print("Indexing of alphabets:",Gkey1)
    elif(len(key)==16):
        Gkey = np.array(Gkey)
        Gkey = np.reshape(Gkey,(4,4))
        print("Matrix Generated is:",Gkey)
        for i in range(len(key)):
            a = lst1.index(key[i])
            Gkey1.append(a)
        print("Indexing of alphabets:",Gkey1)
else:
    print("Key Not in Range!!")
if(len(plaintext)==4 or len(plaintext)==9 or len(plaintext)==16):
    plain = list(plaintext.strip())
    if(len(plaintext)==4):
        sum1 = Gkey1[0] * lst1.index(plain[0]) + Gkey1[1] * lst1.index(plain[1])
        sum1 = sum1 % 26
        plain1.append(lst1[sum1])
        sum2 = Gkey1[2] * lst1.index(plain[0]) + Gkey1[3] * lst1.index(plain[1])
        sum2 = sum2 % 26
        plain1.append(lst1[sum2])
        sum3 = Gkey1[0] * lst1.index(plain[2]) + Gkey1[1] * lst1.index(plain[3])
        sum3 = sum3 % 26
        plain1.append(lst1[sum3])
        sum4 = Gkey1[2] * lst1.index(plain[2]) + Gkey1[3] * lst1.index(plain[3])
        sum4 = sum4 % 26
        plain1.append(lst1[sum4])
        print("Hill Cipher is:"+"".join(plain1))
else:
    print("Plaintext Not in Range So no Encryption!!")
#Decryption
print("*****Decryption*****")
if(len(key)==4):
    #print(Gkey1)
    Gkey1[0], Gkey1[3] = Gkey1[3], Gkey1[0]
    Gkey1[1], Gkey1[2] = -Gkey1[1], -Gkey1[2]
    if(Gkey1[1]<0):
        Gkey1[1] = Gkey1[1] % 26
    if(Gkey1[2]<0):
        Gkey1[2] = Gkey1[2] % 26
    #print(Gkey1)
    det = Gkey1[0]*Gkey1[3] - Gkey1[1]*Gkey1[2]
    if(det<0):
        det = det % 26
        #print(det)
    else:
        print()
    det = pow(det, -1, mod=26)
    Gkey1 = [i * det for i in Gkey1]
    Gkey1 = [i % 26 for i in Gkey1]
    print("Final Key for Decryption:",Gkey1)
    encrypt = "".join(plain1)
    if(len(encrypt)==4):
        encrypt1 = []
        sum1 = Gkey1[0] * lst1.index(encrypt[0]) + Gkey1[1] * lst1.index(encrypt[1])
        sum1 = sum1 % 26
        encrypt1.append(lst1[sum1])
        sum2 = Gkey1[2] * lst1.index(encrypt[0]) + Gkey1[3] * lst1.index(encrypt[1])
        sum2 = sum2 % 26
        encrypt1.append(lst1[sum2])
        sum3 = Gkey1[0] * lst1.index(encrypt[2]) + Gkey1[1] * lst1.index(encrypt[3])
        sum3 = sum3 % 26
        encrypt1.append(lst1[sum3])
        sum4 = Gkey1[2] * lst1.index(encrypt[2]) + Gkey1[3] * lst1.index(encrypt[3])
        sum4 = sum4 % 26
        encrypt1.append(lst1[sum4])
        print("Decryption is "+"".join(encrypt1))

else:
    print("Not available for decryption!!")
