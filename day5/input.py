Python 3.9.4 (tags/v3.9.4:1f2e308, Apr  6 2021, 13:40:21) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a=input()
codegnan
>>> a
'codegnan'
>>> a=input("enter a value: ")
enter a value: 40
>>> a
'40'
>>>  a=input("enter a value: ")
 
SyntaxError: unexpected indent
>>> a=input("enter a value: ")
enter a value: nckjeuifhiwe626548551525
>>> a
'nckjeuifhiwe626548551525'
>>> marks=int(input("enter marks:"))
enter marks:23
>>> marks
23'
>>> cgpa=int(input("enter cgpa"))
enter cgpa9.8
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    cgpa=int(input("enter cgpa"))
ValueError: invalid literal for int() with base 10: '9.8'
>>> cgpa=float(input("enter cgpa"))
enter cgpa9.2
>>> cgpa
9.2
>>> names.split()
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    names.split()
NameError: name 'names' is not defined
>>> name= sree tanuja swathi
SyntaxError: invalid syntax
>>>  name= input()
 
SyntaxError: unexpected indent
>>> name=input()
sree lekha tanuja
>>> names
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    names
NameError: name 'names' is not defined
>>> name
'sree lekha tanuja'
>>> name.split()
['sree', 'lekha', 'tanuja']
>>> name.split(',')
['sree lekha tanuja']
>>> name.split("-")
['sree lekha tanuja']
>>> courses='python-java-c++-flask'
>>> courses.split('-')
['python', 'java', 'c++', 'flask']
>>> names=tuple(input("enter the nmaes:").split())
enter the nmaes:sree lekha tanuja swathi
>>> names
('sree', 'lekha', 'tanuja', 'swathi')
>>> marks=input. split()
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    marks=input. split()
AttributeError: 'builtin_function_or_method' object has no attribute 'split'
>>> marks=input(). split()
09 20 30 52
>>> marks
['09', '20', '30', '52']
>>> map(int,marks)
<map object at 0x0000026D82E59A00>
>>> list(map(int,marks))
[9, 20, 30, 52]
>>> marks=list(map(int,marks("eneter the marks:").split()))
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    marks=list(map(int,marks("eneter the marks:").split()))
TypeError: 'list' object is not callable
>>> marks=list(map(int,input("eneter the marks:").split()))
eneter the marks:50 20 30 40
>>> marks
[50, 20, 30, 40]
>>> marks=tuple(map(int,input("eneter the marks:").split()))
eneter the marks:20 30 40 50
>>> marks
(20, 30, 40, 50)
>>>  marks=list(map(float,input("enter the price:").split()))
 
SyntaxError: unexpected indent
>>> marks=list(map(int,input("eneter the marks:").split()))
eneter the marks:20.5 50.3 45.2
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    marks=list(map(int,input("eneter the marks:").split()))
ValueError: invalid literal for int() with base 10: '20.5'
>>> marks=list(map(float,input("enter the price:").split()))
enter the price:20.4 88.3 555.0
>>> prices
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    prices
NameError: name 'prices' is not defined
>>> price
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    price
NameError: name 'price' is not defined
>>> marks
[20.4, 88.3, 555.0]
>>>  price=list(map(float,input("enter the price:").split()))
 
SyntaxError: unexpected indent
>>> price=list(map(float,input("enter the price:").split()))
enter the price:55.0 33.6 99.0 415610.2 
>>> prices
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    prices
NameError: name 'prices' is not defined
>>> price
[55.0, 33.6, 99.0, 415610.2]
>>> price=tuple(map(float,input("enter the price:").split()))
enter the price:52.33 98.222 45321.00 
>>> price
(52.33, 98.222, 45321.0)
>>> price=set(map(float,input("enter the price:").split()))
enter the price:6544658.52 5156.00 515.22 
>>> price
{6544658.52, 515.22, 5156.0}
>>> a,b=1,2
>>> a
1
>>> b
2
>>> a,b,c=1,2,3
>>> a
1
>>> b
2
>>> c
3
>>> email,password=input("enter the email and password").split()
enter the email and password sree@gmail.com 51654
>>> email
'sree@gmail.com'
>>> password
'51654'
>>> int(password)
51654
>>> name,marks=input("enter the marks: ").split()
enter the marks: jhui
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    name,marks=input("enter the marks: ").split()
ValueError: not enough values to unpack (expected 2, got 1)
>>> name,marks=input("enter the name and marks: ").split()
enter the name and marks: sree 5264
>>> name
'sree'
>>> marks
'5264'
>>> name,marks=list(map(int,input("enter the name and marks: ").split()))
enter the name and marks: sree 523
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    name,marks=list(map(int,input("enter the name and marks: ").split()))
ValueError: invalid literal for int() with base 10: 'sree'
>>> a,b,c=list(map(int,input().split()))

Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    a,b,c=list(map(int,input().split()))
ValueError: not enough values to unpack (expected 3, got 0)
>>> a,b,c=list(map(int,input().split()))
a,b,c=list(map(int,input().split()))
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    a,b,c=list(map(int,input().split()))
ValueError: invalid literal for int() with base 10: 'a,b,c=list(map(int,input().split()))'
>>> a,b,c=list(map(int,input().split()))

Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    a,b,c=list(map(int,input().split()))
ValueError: not enough values to unpack (expected 3, got 0)
>>> 
>>> status=eval(input())
status=eval(input())
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    status=eval(input())
  File "<string>", line 1
    status=eval(input())
          ^
SyntaxError: invalid syntax
>>> status=eval(input())
46
>>> type(status)
<class 'int'>
>>> status=eval(input())
2+3j
>>> type(status)
<class 'complex'>
>>> status=eval(input())
(1,2,3,4)
>>> type(status)
<class 'tuple'>
>>> 