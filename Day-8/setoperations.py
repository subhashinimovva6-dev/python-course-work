Python 3.13.13 (tags/v3.13.13:01104ce, Apr  7 2026, 19:25:48) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
t=(1,2,3,4,5)
t
(1, 2, 3, 4, 5)
t=()
t=(1,1,1,1,1)
t
(1, 1, 1, 1, 1)
t=(1,1.1,'tryu',[])
t
(1, 1.1, 'tryu', [])
t=(10,20,30,40,50)
t
(10, 20, 30, 40, 50)
h=(90,80,70)
t+h
(10, 20, 30, 40, 50, 90, 80, 70)
t
(10, 20, 30, 40, 50)
t[1]
20
t[4]
50
t[2]
30
t[1]
20
t
(10, 20, 30, 40, 50)
t[:3]
(10, 20, 30)
t[3:]
(40, 50)
t[1:4]
(20, 30, 40)
t[2:]
(30, 40, 50)
t[::2]
(10, 30, 50)
t[-1:-4:-1]
(50, 40, 30)
t
(10, 20, 30, 40, 50)
10 in t
True
30 not in t
False
80 in t
False
60 not in t
True
len(t)
5
sorted(t)
[10, 20, 30, 40, 50]
min(t)
10
max(t)
50
sum(t)
150
t.count(10)
1
t.index(10)
0
a=(1,2,4)
a
(1, 2, 4)
x,y,z=a
x
1
y
2
z
4
t=(1,2,3,[4,5,6],7,8)
t
(1, 2, 3, [4, 5, 6], 7, 8)
t(0)
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    t(0)
TypeError: 'tuple' object is not callable
t[0]
1
t[3]
[4, 5, 6]
t[3].append(10)
t
(1, 2, 3, [4, 5, 6, 10], 7, 8)
#set operations
s={1,2,3,4}
s
{1, 2, 3, 4}
s=set()
s={1,1,1,1,1,1}
s
{1}
s={987,654,345,78,689,1,2,3,56}
s
{1, 2, 3, 78, 654, 689, 56, 345, 987}
s=set()
s
set()
s.add(1)
s
{1}
s.add{56.75}
SyntaxError: invalid syntax
s.add(56.75)
s
{56.75, 1}
s.add("hjk")
s
{56.75, 1, 'hjk'}
s.add((1,2,3,4))
s
{56.75, 1, 'hjk', (1, 2, 3, 4)}
s
{56.75, 1, 'hjk', (1, 2, 3, 4)}
s.add(True)
s
{56.75, 1, 'hjk', (1, 2, 3, 4)}
s.add(False)
s
{False, 1, (1, 2, 3, 4), 'hjk', 56.75}
1 in s
True
True in s
True
2 in s
False
False not in s
False
a={1,2,3,5,6,8,10}
b={6,7,8,9}
a | b
{1, 2, 3, 5, 6, 7, 8, 9, 10}
a.union(b)
{1, 2, 3, 5, 6, 7, 8, 9, 10}
a & b
{8, 6}
a.intersection(b)
{8, 6}
a-b
{1, 2, 3, 5, 10}
a^b
{1, 2, 3, 5, 7, 9, 10}
a
{1, 2, 3, 5, 6, 8, 10}
#{1} {2,3},{1,2,3,5} are the subsets
a<={1}
False
a>={1}
True
a<={1,2,3,4,5,6,8,10,11,12}
True
a>={6,10,8}
True
a
{1, 2, 3, 5, 6, 8, 10}
b
{8, 9, 6, 7}
a.isdisjoint(b)
False
a.isdisjoint({90,80})
True
a.add(17)
a
{1, 2, 3, 17, 5, 6, 8, 10}
a.add(14)
a
{1, 2, 3, 5, 6, 8, 10, 14, 17}
a.update({11,12,13})
a
{1, 2, 3, 5, 6, 8, 10, 11, 12, 13, 14, 17}
a.pop()
1
a.pop()
2
a
{3, 5, 6, 8, 10, 11, 12, 13, 14, 17}
>>> a.remove(6)
>>> a
{3, 5, 8, 10, 11, 12, 13, 14, 17}
>>> a.remove(10)
>>> a.discard(3)
>>> a
{5, 8, 11, 12, 13, 14, 17}
>>> a.discard(10)
>>> a
{5, 8, 11, 12, 13, 14, 17}
>>> a
{5, 8, 11, 12, 13, 14, 17}
>>> b={1,2,4,34}
>>> b
{1, 2, 4, 34}
>>> a.intersection(b)
set()
>>> a.intersection_update(b)
>>> a
set()
>>> b
{1, 2, 4, 34}
>>> a={1,4}
>>> a
{1, 4}
>>> c=b
>>> c.add(12)
>>> c
{1, 2, 34, 4, 12}
>>> len(c)
5
>>> min(c)
1
>>> max(c)
34
>>> sorted(c)
[1, 2, 4, 12, 34]
>>> sum(c)
53
