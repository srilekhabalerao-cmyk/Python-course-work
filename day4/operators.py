Python 3.9.4 (tags/v3.9.4:1f2e308, Apr  6 2021, 13:40:21) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #python operators
>>> #arithmetic operators
>>> a=10
>>> b=15
>>> a+b
25
>>> a*b
150
>>> a/b
0.6666666666666666
>>> a//b
0
>>> 10/3
3.3333333333333335
>>> 10//3
3
>>> a%b
10
>>> 2**4
16
>>> 
>>> 
>>> a<b
True
>>> a>b
False
>>> a==b
False
>>> a!=b
True
>>> a>=b
False
>>> a>=10
True
>>> a<=15
True
>>> a=10
>>> a+=20
>>> a
30
>>> a**7
21870000000
>>> a//2
15
>>> a/=2
>>> a
15.0
>>> a*=20
>>> a
300.0
>>> Login=true
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    Login=true
NameError: name 'true' is not defined
>>> login=treu
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    login=treu
NameError: name 'treu' is not defined
>>> login=true
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    login=true
NameError: name 'true' is not defined
>>> email=true
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    email=true
NameError: name 'true' is not defined
>>> email=True
>>> password=False
>>> email and password
False
>>> 's' in 'aeiou'
False
>>> 's' not in 'aeiou'
True
>>> 3%2==0 and 5%2==0
False
>>> 4%2==0 or 5%2==0
True
>>> s='python programming'
>>> 'python' in s
True
>>> 'a' in s
True
>>> 'html' in s
False
>>> l=[1,2,4,6,8]
>>> 5 not in l
True
>>> 6 in l
True
>>> 9 not in l
True
>>> t=(20,4,5,6)
>>> 9 not in t
True
>>> 20 in t
True
>>> 10 not in t
True
>>> data ={'name':'sree', 'course':'pfs', 'batch':'65'}
>>> 'sree' in data
False
>>> 'batch' in data
True
>>> 'pfs'in data
False
>>> '65'in data
False
>>> 'course' in data
True
>>> 'batch' in data
True
>>> # by this we understood that they will onlt check keys not the values
>>> l=[1,2,3,4]
>>> m=[1,2,3,4]
>>> id(l)
2413305257920
>>> id(m)
2413306002176
>>> l == m
True
>>> l is m
False
>>> n=m
>>> n
[1, 2, 3, 4]
>>> m is n
True
>>> id(n)
2413306002176
>>> m is n
True
>>> n is l
False
>>> n is not l
True
>>> 11 |
SyntaxError: invalid syntax
>>> 11 | 15
15
>>> 11^ 4
15
>>> 2<<2
8
>>> 4>>2
1
>>> 