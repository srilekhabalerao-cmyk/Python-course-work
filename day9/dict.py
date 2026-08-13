Python 3.9.4 (tags/v3.9.4:1f2e308, Apr  6 2021, 13:40:21) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> d={}
>>> type(d)
<class 'dict'>
>>> d=
SyntaxError: invalid syntax
>>> d={1:4,2:6,3:8}
>>> d
{1: 4, 2: 6, 3: 8}
>>> d={}
>>> d={}
>>> d[1]=1
>>> d[12.3]=1
>>> d['str']=1
>>> d[(1,2,3)]=1
>>> d[True]=1
>>> d[[1,2]]
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    d[[1,2]]
TypeError: unhashable type: 'list'
>>> d[{1,2}]=1
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    d[{1,2}]=1
TypeError: unhashable type: 'set'
>>> d
{1: 1, 12.3: 1, 'str': 1, (1, 2, 3): 1}
>>> d[flase]=1
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    d[flase]=1
NameError: name 'flase' is not defined
>>> d[False]=1
>>> d
{1: 1, 12.3: 1, 'str': 1, (1, 2, 3): 1, False: 1}
>>> d[1]=1
>>> d[2]=12.3
>>> d[3]='str'
>>> d[4]=2+3j
>>> d[5]=True
>>> d[6]=[1,2,3]
>>> d[7]=(1,2,3)
>>> d[8]={1,2,3}
>>> d[9]=frozenset({1,2})
>>> d[1]=None
>>> d
{1: None, 12.3: 1, 'str': 1, (1, 2, 3): 1, False: 1, 2: 12.3, 3: 'str', 4: (2+3j), 5: True, 6: [1, 2, 3], 7: (1, 2, 3), 8: {1, 2, 3}, 9: frozenset({1, 2})}
4
>>> d={}
>>> d[1]=2
>>> d
{1: 2}
>>> d[2]=5
>>> d
{1: 2, 2: 5}
>>> d[2]=3
>>> d
{1: 2, 2: 3}
>>> data={'name':'sree','course':'pfs','batch':65}
>>> data
{'name': 'sree', 'course': 'pfs', 'batch': 65}
>>> 65 in data
False
>>> 'course'in data
True
>>> data['batch']
65
>>> data['course']
'pfs'
>>> data.get('name')
'sree'
>>> data.get('course')
'pfs'
>>> data.get('age','key is not present')
'key is not present'
>>> 
KeyboardInterrupt
>>> data.get('batch','key is not present')
65
>>> data
{'name': 'sree', 'course': 'pfs', 'batch': 65}
>>> data['age']=21
>>> data
{'name': 'sree', 'course': 'pfs', 'batch': 65, 'age': 21}
>>> data['phno']=9632587412
>>> data
{'name': 'sree', 'course': 'pfs', 'batch': 65, 'age': 21, 'phno': 9632587412}
>>> data.update(('email':'sree@gmail.com', "py":2026)
	    
SyntaxError: invalid syntax
>>> 
KeyboardInterrupt
>>> data.update({'email':'sree@gmail.com', "py":2026})
>>> data
{'name': 'sree', 'course': 'pfs', 'batch': 65, 'age': 21, 'phno': 9632587412, 'email': 'sree@gmail.com', 'py': 2026}
>>> id(data)
2262092627776
>>> data['py']
2026
>>> data['py']=2027
>>> data
{'name': 'sree', 'course': 'pfs', 'batch': 65, 'age': 21, 'phno': 9632587412, 'email': 'sree@gmail.com', 'py': 2027}
>>> data['age']=22
>>> id(data)
2262092627776
>>> data.poputem()
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    data.poputem()
AttributeError: 'dict' object has no attribute 'poputem'
>>> data.popitem()
('py', 2027)
>>> data.pop('course')
'pfs'
>>> data
{'name': 'sree', 'batch': 65, 'age': 22, 'phno': 9632587412, 'email': 'sree@gmail.com'}
>>> len(data)
5
>>> data.keys()
dict_keys(['name', 'batch', 'age', 'phno', 'email'])
>>> data.values()
dict_values(['sree', 65, 22, 9632587412, 'sree@gmail.com'])
>>> data.items()
dict_items([('name', 'sree'), ('batch', 65), ('age', 22), ('phno', 9632587412), ('email', 'sree@gmail.com')])
>>> sorted(data)
['age', 'batch', 'email', 'name', 'phno']
>>> max(data)
'phno'
>>> min(data)
'age'
>>> d.clear()
>>> d
{}
>>> d={1:1,2:2}
>>> d=m
Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    d=m
NameError: name 'm' is not defined
>>> m=d
>>> d
{1: 1, 2: 2}
>>> m
{1: 1, 2: 2}
>>> m[3]=3
>>> m
{1: 1, 2: 2, 3: 3}
>>> d
{1: 1, 2: 2, 3: 3}
>>> n=d.copy()
>>> n[5]=5
>>> n
{1: 1, 2: 2, 3: 3, 5: 5}
>>> d
{1: 1, 2: 2, 3: 3}
>>> data
{'name': 'sree', 'batch': 65, 'age': 22, 'phno': 9632587412, 'email': 'sree@gmail.com'}
>>> data.get('py')
>>> data.setdefault("py",2026)
2026
>>> data
{'name': 'sree', 'batch': 65, 'age': 22, 'phno': 9632587412, 'email': 'sree@gmail.com', 'py': 2026}
>>> data.setdefault("name",2026)
'sree'
>>> data.setdefault("key",2026)
2026
>>> data
{'name': 'sree', 'batch': 65, 'age': 22, 'phno': 9632587412, 'email': 'sree@gmail.com', 'py': 2026, 'key': 2026}
>>> 