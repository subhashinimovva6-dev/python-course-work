Python 3.13.13 (tags/v3.13.13:01104ce, Apr  7 2026, 19:25:48) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
a=10
a
10
float(a)
10.0
complex(a)
(10+0j)
str(a)
'10'
list(a)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    list(a)
TypeError: 'int' object is not iterable
tuple(a)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    tuple(a)
TypeError: 'int' object is not iterable
set(a)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    set(a)
TypeError: 'int' object is not iterable
dict(a)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    dict(a)
TypeError: 'int' object is not iterable
bool(a)
True
b=75.2
int(b)
75
complex(b)
(75.2+0j)
str(b)
'75.2'
list(b)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    list(b)
TypeError: 'float' object is not iterable
tuple(b)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    tuple(b)
TypeError: 'float' object is not iterable
set(b)
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    set(b)
TypeError: 'float' object is not iterable
dict(b)
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    dict(b)
TypeError: 'float' object is not iterable
bool(b)
True
c=75+2j
int(c)
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    int(c)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
float(c)
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    float(c)
TypeError: float() argument must be a string or a real number, not 'complex'
str(c)
'(75+2j)'
list(c)
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    list(c)
TypeError: 'complex' object is not iterable
tuple(c)
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    tuple(c)
TypeError: 'complex' object is not iterable
dict(c)
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    dict(c)
TypeError: 'complex' object is not iterable
bool(c)
True
s="subha"
s="2456"
s="456.789"
int(s)
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    int(s)
ValueError: invalid literal for int() with base 10: '456.789'
s="subha"
a='1234'
b='13.45'
int(a)
1234
float(b)
13.45
list(s)
['s', 'u', 'b', 'h', 'a']
list(a)
['1', '2', '3', '4']
list(b)
['1', '3', '.', '4', '5']
tuple(s)
('s', 'u', 'b', 'h', 'a')
tuple(a)
('1', '2', '3', '4')
tuple(b)
('1', '3', '.', '4', '5')
set(a)
{'1', '3', '4', '2'}
set(s)
{'a', 'u', 'b', 's', 'h'}
set(b)
{'1', '.', '5', '4', '3'}
dict(s)
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    dict(s)
ValueError: dictionary update sequence element #0 has length 1; 2 is required
bool(s)
True
bool(a)
True
bool(b)
True
l=[1,2,3,4]
l
[1, 2, 3, 4]
int(l)
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    int(l)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'list'
float(l)
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    float(l)
TypeError: float() argument must be a string or a real number, not 'list'
complex(l)
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    complex(l)
TypeError: complex() first argument must be a string or a number, not 'list'
tuple(l)
(1, 2, 3, 4)
se(l)
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    se(l)
NameError: name 'se' is not defined. Did you mean: 's'?
set(l)
{1, 2, 3, 4}
bool(l)
True
t=(1,2,3,4,5)
t
(1, 2, 3, 4, 5)
>>> str(t)
'(1, 2, 3, 4, 5)'
>>> list(t)
[1, 2, 3, 4, 5]
>>> tuple(t)
(1, 2, 3, 4, 5)
>>> bool(t)
True
>>> s={1,2,3}
>>> str(s)
'{1, 2, 3}'
>>> list(s)
[1, 2, 3]
>>> tuple(s)
(1, 2, 3)
>>> bool(s)
True
>>> b=True
>>> int(b)
1
>>> float(b)
1.0
>>> complex(b)
(1+0j)
>>> str(b)
'True'
>>> d={'name':'subha','age':'21'}
>>> d
{'name': 'subha', 'age': '21'}
>>> str(d)
"{'name': 'subha', 'age': '21'}"
>>> list(d)
['name', 'age']
>>> tuple(d)
('name', 'age')
>>> set(d)
{'age', 'name'}
>>> bool(d)
True
