plaintext = input("Enter Plaintext:")
key = input("Enter the Key:")
Gkey = []
vernam = []
lst1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
plaintext=plaintext.lower()
if(len(plaintext)==len(key)):
    print("Key is ",key)
    Fkey = key.lower()
    for f in range(len(Fkey)):
        b = lst1.index(plaintext[f]) + lst1.index(Fkey[f])
        if(b > 25):
            c = b-26
            vernam.append(lst1[c])
        else:
            vernam.append(lst1[b])
    print("Vernam Cipher is:"+"".join(vernam))
else:
    for i in range(len(plaintext)):
        Gkey.append(key[i % len(key)])
    print("Key is:"+"".join(Gkey))
    Fkey = "".join(Gkey)
    Fkey = Fkey.lower()
    for f in range(len(Fkey)):
        b = lst1.index(plaintext[f]) + lst1.index(Fkey[f])
        if(b > 25):
            c = b-26
            vernam.append(lst1[c])
        else:
            vernam.append(lst1[b])
    print("Vernam Cipher is:"+"".join(vernam))
