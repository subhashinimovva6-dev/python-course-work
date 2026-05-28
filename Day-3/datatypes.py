Python 3.13.13 (tags/v3.13.13:01104ce, Apr  7 2026, 19:25:48) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> a=10
>>> type(a)
<class 'int'>
>>> t=75.45
>>> type(t)
<class 'float'>
>>> c=12+5j
>>> type(c)
<class 'complex'>
>>> s="subhashini"
>>> type(s)
<class 'str'>
>>> s='subha'
>>> type(s)
<class 'str'>
>>> s='''subhashini'''
>>> type(s)
<class 'str'>
>>> l=[1,2,3]
>>> id(l)
2697884373056
>>> l=['post1.png','reel1.mp4']
>>> l
['post1.png', 'reel1.mp4']
>>> l=[]
>>> l=list()
>>> type(l)
<class 'list'>
>>> t=(1,2,34,75,43)
>>> t
(1, 2, 34, 75, 43)
>>> type(t)
<class 'tuple'>
>>> s={1,2,3,4,6}
>>> type(s)
<class 'set'>
>>> s=set()
>>> s={45678,678,56789,897}
a
10
s
{897, 678, 56789, 45678}

d={'name':'abc','age':100,'course':'PSF'}
D
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    D
NameError: name 'D' is not defined. Did you mean: 'd'?
d
{'name': 'abc', 'age': 100, 'course': 'PSF'}
type(d)
<class 'dict'>
status=True
satus=False
type(status)
<class 'bool'>
a=None
type(a)
<class 'NoneType'>
