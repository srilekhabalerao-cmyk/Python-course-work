Python 3.9.4 (tags/v3.9.4:1f2e308, Apr  6 2021, 13:40:21) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> t=()
>>> t=tuple()
>>> t=(1,2,3,4)
>>> t
(1, 2, 3, 4)
>>> t(1)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    t(1)
TypeError: 'tuple' object is not callable
>>> t=(1)
>>> t
1
>>> t=(1,)
>>> t
(1,)
>>> t=(1,1,1)
>>> t
(1, 1, 1)
>>> t=(1,12.35,'str',(1,4))
>>> t
(1, 12.35, 'str', (1, 4))
>>> type(t)
<class 'tuple'>
>>> t=(1,12.35,'str',(1,4),(1,2,3),{1,5,9},true,{1:4,2:6})
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    t=(1,12.35,'str',(1,4),(1,2,3),{1,5,9},true,{1:4,2:6})
NameError: name 'true' is not defined
>>>  t=(1,12.35,'str',(1,4),(1,2,3),{1,5,9},True,{1:4,2:6})
 
SyntaxError: unexpected indent
>>> t=(1,12.35,'str',(1,4),(1,2,3),{1,5,9},True,{1:4,2:6})
>>> t
(1, 12.35, 'str', (1, 4), (1, 2, 3), {1, 5, 9}, True, {1: 4, 2: 6})
>>> (1,2,3,4)+(21,36)
(1, 2, 3, 4, 21, 36)
\
>>> (1,2)*3
(1, 2, 1, 2, 1, 2)
>>> t[1]
12.35
>>> t[-1]
{1: 4, 2: 6}
>>> t[5]
{1, 5, 9}
>>> t[3:7]
((1, 4), (1, 2, 3), {1, 5, 9}, True)
>>> t[-1:-4:-1]
({1: 4, 2: 6}, True, {1, 5, 9})
>>> "str" in t
True
>>> True in t
True
>>> 12.35 in t
True
>>> t=(12,14,5215,8465,962,32,15,12,6854,14)
>>> t
(12, 14, 5215, 8465, 962, 32, 15, 12, 6854, 14)
>>> sorted(t)
[12, 12, 14, 14, 15, 32, 962, 5215, 6854, 8465]
>>> min(t)
12
>>> max(t)
8465
>>> len(t)
10
>>> t.index(12)
0
>>> sum(t)
21595
>>> count(t)
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    count(t)
NameError: name 'count' is not defined
>>> t.count(14)
2
>>> any(12,14)
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    any(12,14)
TypeError: any() takes exactly one argument (2 given)
>>> any((12,14,32))
True
>>> all((12,52,32))
True
>>> t=1,2,3
>>> a,b,c=t
>>> a
1
>>> b
2
>>> c
3
>>> t=(1,2,3,4,[23,24],3)
>>> t
(1, 2, 3, 4, [23, 24], 3)
>>> t[4].append(25)
>>> t
(1, 2, 3, 4, [23, 24, 25], 3)
>>> s=set()
>>> s={12,6498,52,4157,12,36}
>>> s
{6498, 36, 52, 12, 4157}
>>> s={1,1,1,1}
>>> s
{1}
>>> s=set()
>>> s.add(1)
>>> s.add(12.5)
>>> s.add("str")
>>> s.add((1,2,3))
>>> s.add({1,2,3})
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    s.add({1,2,3})
TypeError: unhashable type: 'set'
>>> s.add([1,2,3])
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    s.add([1,2,3])
TypeError: unhashable type: 'list'
>>> s.add(True)
>>> s
{1, (1, 2, 3), 12.5, 'str'}
>>> a=(1,2,3,4,5)
>>> b=(3,4,5,6,7,8)
>>> a|b
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    a|b
TypeError: unsupported operand type(s) for |: 'tuple' and 'tuple'
>>> a | b
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    a | b
TypeError: unsupported operand type(s) for |: 'tuple' and 'tuple'
>>> a&b
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    a&b
TypeError: unsupported operand type(s) for &: 'tuple' and 'tuple'
>>> a={1,2,3,4,5}
>>> b={3,2,9,10,12}
>>> a|b
{1, 2, 3, 4, 5, 9, 10, 12}
>>> a&b
{2, 3}
>>> a-b
{1, 4, 5}
>>> b-a
{9, 10, 12}
>>> a^b
{1, 4, 5, 9, 10, 12}
>>> 12 in b
True
>>> 12 not in b
False
>>> {1}<=a
True
>>> {1,2,3}<=a
True
>>> {1,5,6}<=a
False
>>> a>={1,3,9}
False
>>> a.isdisjoint(b)
False
>>> m={1,2,3}
>>> n={1,2,3}
>>> m.isdisjoint(n)
False
>>> a={12,45,89,523,5623}
>>> a
{5623, 89, 523, 12, 45}
>>> sorted(a)
[12, 45, 89, 523, 5623]
>>> min(a)
12
>>> max(a)
5623
>>> any({12,33,1654})
True
>>> all({12,45})
True
>>> sum(a)
6292
>>> a.add(100)
>>> a
{100, 5623, 89, 523, 12, 45}
>>> a.remove(100)
>>> a.discard(30)
>>> a
{5623, 89, 523, 12, 45}
>>> a.pop(12)
Traceback (most recent call last):
  File "<pyshell#99>", line 1, in <module>
    a.pop(12)
TypeError: set.pop() takes no arguments (1 given)
>>> a.pop()
5623
>>> a
{89, 523, 12, 45}
>>> a.clear()
>>> a
set()
>>> 