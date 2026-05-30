Python 3.13.13 (tags/v3.13.13:01104ce, Apr  7 2026, 19:25:48) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> a=20
>>> b=10
>>> a+b
30
>>> a-b
10
>>> a*b
200
>>> a/b
2.0
>>> a//b
2
>>> a%b
0
>>> a**2
400
>>> a=20
>>> b=10
>>> a<b
False
>>> a>b
True
>>> a<=b
False
>>> a>=b
True
>>> a==b
False
>>> a!=b
True
>>> assignment operators
SyntaxError: invalid syntax
>>> y=10
>>> y=y+10
>>> y
20
>>> y+=10
>>> y
30
y-=10
y
20
y*=10
y
200
y/=10
y
20.0
y//=10
y
2.0
y%=2
y
0.0
y=10
y//=2
y
5
logical
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    logical
NameError: name 'logical' is not defined
a=20
b=10
a
20


5
a%10==0
True
a%20==0 and b%20==0 and a>b
False
a%20==0 or b%20==0 or a>b
True
a%20==0 or b%20==0 or a<b
True
a%22==0 or b%20==0 or a<b
False
not a%20==0
False
not a>b
False
#membership operators
a='python programming'
a
'python programming'
'y'in a
True
'g'in a
True
'z'not in a
True
'r' not in a
False
l=['java','python','mysql','c++']
l
['java', 'python', 'mysql', 'c++']
'mysql' in l
True
'c'in l
False
'python' not in l
False
t=('laptop','mobile','charger')
t
('laptop', 'mobile', 'charger')
'mobile' in t
True
'mouse'in t
False
'charger'not in t
False
'cpu' not in t
True
t={1,2,3,4,5}
t
{1, 2, 3, 4, 5}
1 in t
True
3 not in t
False
d={'egg':40,'oil':120,'sugar':230}
d
{'egg': 40, 'oil': 120, 'sugar': 230}
'oil'in d
True
'chilli'in d
False
120 in d
False
#identity operators
l=[1,2,3,4,5]
m=[1,2,3,4,5]
l==m
True
n=m
n
[1, 2, 3, 4, 5]
n==m
True
l is m
False
n is m
True
id(l)
2266312472448
id(m)
2266359860736
id(n)
2266359860736
n is l
False
l is not m
True
n is not m
False
n is not l
True
#bitwise operators
8&14
8
8&7
0
8|7
15
10^11
1
~12
-13
~24
-25
8>>2
2
15>>1
7
15>>3
1
15>>2
3
16<<1
32
4<<2
16
