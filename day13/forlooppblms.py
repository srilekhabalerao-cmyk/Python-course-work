'''
n=int(input("enter the number: "))
res=[]
for i in range(1,n+1):
    if n%i==0:
        res.append(i)
print(f"fators of {n} = {res}")

s='python programming'
d = {}
for i in s:
    if i in d:
         d[i] = d[i] + 1
    else:
         d[i] = 1
print(d)
'''

s = 'aaaaaaaaasssssssssssdddddddddddddffff'
result = ''
count = 1
for i in range(len(s)-1):
    if s[i] == s[i+1]:
        count = count + 1
    else:
        result = result + s[i] + str(count)
        count = 1

result = result + s[i] + str(count)
print(result)



