Python 3.9.4 (tags/v3.9.4:1f2e308, Apr  6 2021, 13:40:21) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
========================================================== RESTART: C:\Users\Rahul\OneDrive\Desktop\python course\day2\keywords.py =========================================================
['False', 'None', 'True', '__peg_parser__', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
36
>>> a=12
>>> type(a)
<class 'int'>
>>> b=12.4
\
>>> type(b)
<class 'float'>
>>> c=13+8i
SyntaxError: invalid syntax
>>> c= 12+3j
>>> type(c)
<class 'complex'>
>>> c
(12+3j)
>>> #string, list, tuple
>>> s= "Sree"
>>> id(s)
2076818805168
>>> s="lekha"
>>> s
'lekha'
>>> s+="Sree"
>>> s
'lekhaSree'
>>> id(s)
2076818796464
>>> type(s)
<class 'str'>
>>> l=[1,2,3,4,5,6]
>>> l
[1, 2, 3, 4, 5, 6]
>>> type(l)
<class 'list'>
>>> id(l)
2076818914176
>>> l=[1,12.3,'str',[1,4]]
>>> type(l)
<class 'list'>
>>> t=(1,23,58)
>>> type(t)
<class 'tuple'>
>>> #set , dict
>>> s={80,70,50,22,69,69,69}
>>> s
{80, 50, 69, 70, 22}
>>> id(s)
2076818764288
>>> s.add(20)
>>> s
{80, 50, 20, 69, 70, 22}
>>> d=frozen({1,2,3})
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    d=frozen({1,2,3})
NameError: name 'frozen' is not defined
>>> d=frozenset({1,32,88})
>>> d
frozenset({32, 1, 88})
>>> type(d)
<class 'frozenset'>
>>> a=True
>>> b=False
>>> a
True
>>> b
False
>>> type(a)
<class 'bool'>
>>> a=None
>>> a
>>> type(a)
<class 'NoneType'>
>>> 