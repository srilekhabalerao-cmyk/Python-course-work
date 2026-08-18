'''fa=eval(input("Follows Account: "))
if fa:
    cf=eval(input("Close friend: "))
    if cf:
        print("story visible")
    else:
        print("not in close friends")
else:
    print("follow the account first ")

reg=eval(input("Registered: "))
if reg:
    fee=eval(input("fee paid :"))
    if fee:
        print("Registration confrimed ")
    else:
        print("need to pay the fee")
else:
    print("Registrstion required")


ls=eval(input("enter the status: "))
if ls:
    pg=eval(input("enter the premission: "))
    if pg:
        print("link accessed")
    else:
        print("access denied")
else:
    print("invalid link")
'''
data={
    'Sree':{'status':True,'python':90,'mysql':85,'flask':89},
    'sai':{'status':False ,'python':None,'mysql': None,'flask':None},
    'swathi':{'status':True,'python':70,'mysql':65,'flask':59},
    'Tanuja':{'status':True,'python':30,'mysql':25,'flask':39},
    'lekha':{'status':True,'python':100,'mysql':95,'flask':99}
}
name=input("enter the name: ")
if name in data:
    if data[name]['status']:
        sum=data[name]['python']+data[name]['mysql']+data[name]['flask']
        avg=sum/3
        print(f"hello {name}")
        print(f"Your avg score : {avg}")
        if avg>=90:
            print("outstanding")
        elif avg>=80:
            print("very good")
        elif avg>=60:
            print("work hard")
        else:
            print("better luck next time")
    else:
        print(f"{name} didnt write the exam")

else:
    print(f"{name} not found ")