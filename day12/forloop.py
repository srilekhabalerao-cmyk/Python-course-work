"""syntax for "for" loop
for var in seq:
    #stmts
------------------------
s="python programming"
for i in s:
    print(i)

l=[1,2,3,4,45]
for i in l:
    print(i)

prices=(12365,65648,5648,56425)
for price in prices:
    print(price)

names={"sree","lekha","sai","diya"}
for name in names:
    print(name)

d={1:2,2:4,3:6,4:8,5:10}
for i in d:
    print(i,d[i])

for i in range(1,11):
    print(i)

for i in range(2,21,2):
    print(i)

for i in range(5,101,5):
    print(i)


for i in range(5,0,-1):
    print(i)


for i in range(19,0,-2):
    print(i)

s="python programming language"
for i in range(len(s)):
    print(i,s[i])

s="java programming language"
for i in range(len(s)):
    print(i,s[i])

s=(456,4567,45678,5183)
for i in range(len(s)):
    print(i,s[i])

s=[6785,235,235,456]
for i in enumerate(s):
    print(i[0],i[1])

s=(6785,235,235,456)
for i in enumerate(s):
    print(i[0],i[1])

d={1:2,2:4,3:6,4:8}
for i in enumerate(d):
    print(i[0],i[1],d[i[1]])

for i in range(1,11):
    if i==5:
        break
    print(i)

for i in range(1,11):
    if i==5:
        continue
    print(i)

for i in range(1,11):
    if i==15:
        break
    print(i)
else:
    print("end of the loop")

l=[12,13,14,15,16,18,20]
n=16
for i in l:
    if i==n:
        print(n,"found")
        break
else:
    print(n,"not found")

pin=123
for i in range(5):
    epin=int(input("enter the pin: "))
    if epin==pin:
        print("unlocked phone")
        break
    else:
        print("invalid pin")
else:
    print("try after 30 seconds")

n=int(input("enter a number: "))
if n<=1:
    print("not a prime")
else:
    for i in range(2,n):
        if n%i==0:
            print("not a prime")
            break
    else:
        print("prime")
"""
n=int(input("enter a number: "))
for i in range(2,n//2+1):
        if n%i==0:
            print("not a prime")
            break
else:
    print("prime")
