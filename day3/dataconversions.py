Python 3.9.4 (tags/v3.9.4:1f2e308, Apr  6 2021, 13:40:21) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # type conversion
>>> a=10
>>> float(a)
10.0
>>> complex(a)
(10+0j)
>>> bool(a)
True
>>> list(a)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    list(a)
TypeError: 'int' object is not iterable
>>> tuple(a)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    tuple(a)
TypeError: 'int' object is not iterable
>>> dict(a)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    dict(a)
TypeError: 'int' object is not iterable
>>> f=10.2
>>> int(b)
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    int(b)
NameError: name 'b' is not defined
>>> dict(b)
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    dict(b)
NameError: name 'b' is not defined
>>> str(b)
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    str(b)
NameError: name 'b' is not defined
>>> str(f)
'10.2'
>>> tuple(f)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    tuple(f)
TypeError: 'float' object is not iterable
>>> dict(f)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    dict(f)
TypeError: 'float' object is not iterable
>>> c=3+8j
>>> int(c)
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    int(c)
TypeError: can't convert complex to int
>>> flot(c)
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    flot(c)
NameError: name 'flot' is not defined
>>> str(c)
'(3+8j)'
>>> bool(c)
True
>>> s='codegnan'
>>> a='345567'
>>> int(a)
345567
>>> list(a)
['3', '4', '5', '5', '6', '7']
>>> tuple(a)
('3', '4', '5', '5', '6', '7')
>>> set(a)
{'4', '6', '5', '7', '3'}
>>> 