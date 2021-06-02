from random import randint
import hashlib
print("***Digital Signature Algorithm***")
p = 283
q = 47
g = 60

def modInverse(a, m):
    for x in range(1, m):
        if (((a%m) * (x%m)) % m == 1):
            return x
    return -1

k=randint(1,q)
x=randint(1,q)
r=(((g**k)%p)%q)
print("K =",k)
print("X =",x)
k1=modInverse(k,q)
message=input("Enter Message : ")
h = hashlib.sha512(message.encode())
h=int(str(h.hexdigest()),16)
s=(k1*(h+x*r))%q

y=(g**x)%p
print("R =",r)
print("S =",s)


#reciver
h = hashlib.sha512(message.encode())
h=int(str(h.hexdigest()),16)

w=(modInverse(s,q))%q
u1=(h*w)%q
u2=(r*w)%q

v=(((g**u1)*(y**u2))%p)%q

print("V =",v)

if v==r:
    print("Verified")
else:
    print("Not Verified")

