Python 3.9.4 (tags/v3.9.4:1f2e308, Apr  6 2021, 13:40:21) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a=90
>>> b=13.8
>>> c='sree'
>>> print(a,b,c)
90 13.8 sree
>>> print('a:',a,'b:',b,'c:',c)
a: 90 b: 13.8 c: sree
>>> print('a:',a,'b:',b,'c:',c,sep='')
a:90b:13.8c:sree
>>> print('a:',a,'b:',b,'c:',c, sep='\n\n')
a:

90

b:

13.8

c:

sree
>>> print('a:',a,'b:',b,'c:',c, sep="t")
a:t90tb:t13.8tc:tsree
>>> print('a:',a,'b:',b,'c:',c,sep='\t')
a:	90	b:	13.8	c:	sree
>>> print('a:',a,'b:',b,'c:',c, sep='\n', end='\n\n')
a:
90
b:
13.8
c:
sree

>>> print('a:',a,'b:',b,'c:',c, end='#')
a: 90 b: 13.8 c: sree#
>>> print(f'a={a} b={b} c={c})
      
SyntaxError: EOL while scanning string literal
>>>  print(f'a={a} b={b} c={c}')
 
SyntaxError: unexpected indent
>>> print(f'a={a} b={b} c={c}')
a=90 b=13.8 c=sree
>>> print('a=%d b=%f c=%s' %(a,b,c))
a=90 b=13.800000 c=sree
>>> print('a={} b={}
      
SyntaxError: EOL while scanning string literal
>>> print('a={} b={} c={}'.format(a,b,c))
a=90 b=13.8 c=sree
>>> print('a={} b={} c={}'.format(b,c,a))
a=13.8 b=sree c=90
>>> 