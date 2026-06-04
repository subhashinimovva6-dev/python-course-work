Python 3.13.13 (tags/v3.13.13:01104ce, Apr  7 2026, 19:25:48) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
s='   hello   world   '
s
'   hello   world   '
s.strip()
'hello   world'
s.lstrip()
'hello   world   '
s.rstrip()
'   hello   world'
#string testing
s='strings.py'
s
'strings.py'
s.startswith('str')
True
s.startswith('ghj')
False
s.endswith('py')
True
s.endswith('hjk')
False
'sdfyuk'.isalpha()
True
'wet5568'.isalpha()
False
'DGhyggjk'.isalpha()
True
'dfr34@'.isalpha()
False
'2345'.isalnum()
True
'ewrtyuii'.islower()
True
'dfgjhjkjn354*$#@'.islower()
True
'ASFhkjn'.islower()
False
'DGHG'.isupper()
True
' '.isspace()
True
'hello     '.isspace()
False
'Py Prh Lan'.istitle()
True
'Py phj'.istitle()
False
'py_python'.isidentifier()
True
'py@123'.isidentifier()
False
#list
l=[]
l=list()
type(l)
<class 'list'>
l=[1,2,3]
m=[1,3,4]
l+m
[1, 2, 3, 1, 3, 4]
l*4
[1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]
l=[10,20,38,68]
l=[10,20,30,40,50]
l
[10, 20, 30, 40, 50]
l[4]
50
l[0]
10
l[2]
30
l[-1]
50
l[-3]
30
l[1:4]
[20, 30, 40]
l[::-1]
[50, 40, 30, 20, 10]
l[-1:-4:-1]
[50, 40, 30]
l[-3::-1]
[30, 20, 10]
l
[10, 20, 30, 40, 50]
20 in l
True
50 in l
True
80 in l
False
10 not in l
False
70 not in l
True
l
[10, 20, 30, 40, 50]
id(l)
2451048827968
l[1]
20
l[1]=70
l
[10, 70, 30, 40, 50]
id(l)
2451048827968
l[4]=100
l
[10, 70, 30, 40, 100]
l.append(120)
l
[10, 70, 30, 40, 100, 120]
l.append(400)
l
[10, 70, 30, 40, 100, 120, 400]
l.insert(1,60)
l
[10, 60, 70, 30, 40, 100, 120, 400]
l.insert(4,50)
l
[10, 60, 70, 30, 50, 40, 100, 120, 400]
l.extend([80,90,110])
l
[10, 60, 70, 30, 50, 40, 100, 120, 400, 80, 90, 110]
l.pop()
110
l
[10, 60, 70, 30, 50, 40, 100, 120, 400, 80, 90]
l.pop()
90
l
[10, 60, 70, 30, 50, 40, 100, 120, 400, 80]
l.pop(3)
30
l
[10, 60, 70, 50, 40, 100, 120, 400, 80]
l.pop(1)
60
l
[10, 70, 50, 40, 100, 120, 400, 80]
l.remove(100)
l
[10, 70, 50, 40, 120, 400, 80]
l.remove(400)
l
[10, 70, 50, 40, 120, 80]
del l[1]
l
[10, 50, 40, 120, 80]
del l[2]
l
[10, 50, 120, 80]
l.clear()
l
[]
>>> id(l)
2451048827968
>>> l=[200,30,33,42,10,70,50,40,100,120,400]
>>> l
[200, 30, 33, 42, 10, 70, 50, 40, 100, 120, 400]
>>> sorted(l)
[10, 30, 33, 40, 42, 50, 70, 100, 120, 200, 400]
>>> l.sort()
>>> l
[10, 30, 33, 40, 42, 50, 70, 100, 120, 200, 400]
>>> min(l)
10
>>> max(l)
400
>>> sorted(l,rerverse=True)
Traceback (most recent call last):
  File "<pyshell#97>", line 1, in <module>
    sorted(l,rerverse=True)
TypeError: sort() got an unexpected keyword argument 'rerverse'. Did you mean 'reverse'?
>>> sorted(l,reverse=True)
[400, 200, 120, 100, 70, 50, 42, 40, 33, 30, 10]
>>> l.index(120)
8
>>> l.index(200)
9
>>> l
[10, 30, 33, 40, 42, 50, 70, 100, 120, 200, 400]
>>> l.count(30)
1
>>> l
[10, 30, 33, 40, 42, 50, 70, 100, 120, 200, 400]
>>> len(l)
11
>>> sum(l)
1095
>>> any([1,2,4,5,5,0,0,0,0,])
True
>>> all([1,2,4,5,5,0,0,0,0])
False
