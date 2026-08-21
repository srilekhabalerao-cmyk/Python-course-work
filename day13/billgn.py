data={
    'rice':100,
    'dal':50,
    'sugar':60,
    'eggs':160,
    'salt':20,
    'oil':120,
    'chillioil':120

}
for i in data:
    print(i.ljust(20),data[i])
prod=input("enter products: ").split()
print(prod)
total = 0
for i in prod:
    if i in data:
        print(i.ljust(20), data[i])
        total = total + data[i]
print("Total".ljust(20), total)
