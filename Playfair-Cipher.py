import numpy as np
PT = input("Enter Plain Text:")
k = input("Enter the Key:")
plaintext=list(PT.replace("j","i"))
key=list(k.replace("j","i"))
encrypt=""
matrix=[]
for i in key:
  if(i not in matrix):
    matrix.append(i)

alpha=97
for i in range(97,123):
  if(i==106):
    pass
  elif(chr(i) not in matrix):
    matrix.append(chr(i))
matrix=np.array(matrix)
matrix=np.reshape(matrix,(5,5))
print(matrix)

k=0
index=[]
while k+1<len(plaintext):
  if(plaintext[k]==plaintext[k+1]):
    index.append(k+1)
  k+=2
print("Intial List:",plaintext)

for i in range(len(index)):
  status=1
  for j in range(0,len(plaintext),2):
    if(j+1<len(plaintext)):
      if(plaintext[j]==plaintext[j+1]):
        status=0

  if(status!=1):
    plaintext.insert(index[i]+i,"x")


print("List after there are any repeated letters:",plaintext)
if(len(plaintext)%2!=0):
  plaintext.append("x")


for i in range(0,len(plaintext),2):
  first=[]
  second=[]
  for k in range(5):
    for j in range(5):
      if(matrix[k,j]==plaintext[i]):
        first=[k,j]
      if(matrix[k,j]==plaintext[i+1]):
        second=[k,j]
  if(first[0]==second[0]):
    encrypt+=matrix[first[0],(first[1]+1)%5]
    encrypt+=matrix[second[0],(second[1]+1)%5]
  elif(first[1]==second[1]):
    encrypt+=matrix[(first[0]+1)%5,first[1]]
    encrypt+=matrix[(second[0]+1)%5,second[1]]
  else:
    encrypt+=matrix[first[0],second[1]]
    encrypt+=matrix[second[0],first[1]]

print("PlayFair Cipher is", encrypt)
