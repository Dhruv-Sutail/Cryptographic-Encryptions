q = 23
lst = []
lst1 = []
primitive = []
for i in range(1, q):
    lst.append(i)
for x in range(len(lst)):
    lst1 = [(x**element) % q for element in lst]
    lst1.sort()
    #print(lst1)
    a = set(lst)
    b = set(lst1)
    if(a==b):
        primitive.append(x)
        lst1 = []
    else:
        lst1 = []
#print("Primitive Roots are ",primitive)
PK1 = int(input("Enter Private key 1:"))
PK2 = int(input("Enter Private key 2:"))
Y1 = (int(primitive[1])**PK1) % q
Y2 = (int(primitive[1])**PK2) % q
PUK1 = (Y2**PK1) % q
PUK2 = (Y1**PK2) % q
if(PUK1==PUK2):
    print("Success")
else:
    print("Fail")

print("\n1 for Public Elements\n2 for Secret Key A\n3 for Secret Key B")
ch = int(input("Enter choice:"))
if(ch==1):
    print("Alpha is",q)
    print("Primitive Root is",primitive[1])
    print("Public Key A is",Y1)
    print("Public Key B is",Y2)
elif(ch==2):
    print("Secret Key A is",PUK1)
elif(ch==3):
    print("Secret Key A is",PUK2)
else:
    print("Wrong Choice")
