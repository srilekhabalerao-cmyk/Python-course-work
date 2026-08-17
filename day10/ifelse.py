'''
username= input("user name : ")
password = input("password: ")
if username=='admin' and password=='admin123':
    print("login successful")
else:
    print("invlaid Credentials")

products=['laptop','mouse','bag']
search=input("enter the product: ")
if search in products:
    print(f'{search} is found')
else: 
    print(f'{search} is not found')
'''
bill= int(input("enter the bill :"))
if bill > 99:
    print("Total bill:", bill)
else:
    print("total bill:", bill+30)