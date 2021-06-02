plaintext = input("Enter the Plaintext:")
key = input("Enter the Key:")
Gkey = []
vig = []
plaintext = plaintext.upper()
if(len(plaintext)==len(key)):
    Fkey = key
    print("Key is ",key)
    Fkey = Fkey.upper()
    print(Fkey)
    for c in range(len(Fkey)):
        b = (ord(plaintext[c])+ord(Fkey[c])) % 26
        b +=ord('A')
        vig.append(chr(b))
    print("Vigenere Cipher is:"+"".join(vig))
else:
    for i in range(len(plaintext)):
        Gkey.append(key[i % len(key)])
    print(plaintext)
    Fkey = "".join(Gkey)
    Fkey = Fkey.upper()
    print(Fkey)
    for c in range(len(Fkey)):
        b = (ord(plaintext[c])+ord(Fkey[c])) % 26
        b +=ord('A')
        vig.append(chr(b))
    print("Vigenere Cipher is:"+"".join(vig))
