Python 3.13.13 (tags/v3.13.13:01104ce, Apr  7 2026, 19:25:48) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> a=12
>>> b=12.5
>>> c="python"
>>> print(a,b,c)
12 12.5 python
>>> print("a=",a,"b=",b,"c=",c)
a= 12 b= 12.5 c= python
>>> print("a=",a,"b=",b,"c=",c,sep='')
a=12b=12.5c=python
>>> print("a=",a,"b=",b,"c=",c,sep='\n')
a=
12
b=
12.5
c=
python
>>> print("a=",a,"b=",b,"c=",c,sep='',end='@@@')
a=12b=12.5c=python@@@
>>> print(f'a={a} b={b} c={c}')
a=12 b=12.5 c=python
>>> print('a=%d b=%.2f c%s'%(a,b,c))
a=12 b=12.50 cpython
>>> print('a={} b={}
...       
SyntaxError: unterminated string literal (detected at line 1)
>>> print('a={} b={} c={]'.format(a,b,c))
...       
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    print('a={} b={} c={]'.format(a,b,c))
ValueError: expected '}' before end of string
>>> print('a={} b={} c={}'.format(a,b,c))
...       
a=12 b=12.5 c=python
>>> print('a={2} b={0} c={1}'.format(a,b,c))
...       
a=python b=12 c=12.5
