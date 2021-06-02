from math import gcd as gcd
PT = input('Enter plaintext:')
lst = []
p = 11
q = 17
n = p*q
EF = (p-1)*(q-1)
for i in range(1,EF):
    if gcd(EF, i+1) == 1:
        lst.append(i+1)
print(lst)
public_key = lst[1]
for i in range(1,EF):
    if i*public_key % EF == 1:
        private_key = i
print("Public Key is",'(',public_key,n,')')
print("Private Key is",'(',private_key,n,')')
CT = (int(PT)**public_key) % n
print("Cipher Text is",str(CT))
decrypt = (CT**private_key) % n
print("Decrypted Text is",str(decrypt))
