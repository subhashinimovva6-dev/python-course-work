Python 3.13.13 (tags/v3.13.13:01104ce, Apr  7 2026, 19:25:48) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> name=input()
subha
>>> name
'subha'
>>> name=input("enter your name:")
enter your name:subha
>>> name
'subha'
>>> age=input("enter your age:")
enter your age:21
>>> age
'21'
>>> age=int(input("enter your age:"))
enter your age:21
>>> age
21
>>> gpa=float(input("enter your cgpa:"))
enter your cgpa:7.97
>>> cgpa
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    cgpa
NameError: name 'cgpa' is not defined. Did you mean: 'gpa'?
>>> gpa
7.97
>>> names="subha harika maha gaya"
>>> names
'subha harika maha gaya'
>>> 'subha harika maha gaya'.split(' ')
['subha', 'harika', 'maha', 'gaya']
>>> 'java-pytyhon-c-c#'
'java-pytyhon-c-c#'
>>> names=input("enter the names:").split()
enter the names:subha harika maha gaya
>>> names
['subha', 'harika', 'maha', 'gaya']
>>> products=input("enter the products:")
enter the products:laptop mouse keyboard
>>> products
'laptop mouse keyboard'
products=input("enter the products:").split()
enter the products:laptop mouse keyboard
products
['laptop', 'mouse', 'keyboard']
topics=tuple(input("enter the topics:").split())
enter the topics:token statement variable comments
topics
('token', 'statement', 'variable', 'comments')
op=set(input("enter the op:").spli())
enter the op:in not in is is not and or not
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    op=set(input("enter the op:").spli())
AttributeError: 'str' object has no attribute 'spli'. Did you mean: 'split'?
op
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    op
NameError: name 'op' is not defined
op=set(input("enter the op:").split())
enter the op:in not in is and or not
op
{'or', 'in', 'is', 'not', 'and'}
list(map(int,input("enter the marks:").split()))
enter the marks:85 75 6 7
[85, 75, 6, 7]
prices=tuple(map(int,input("enter the prices:").split()))
enter the prices:345 678 987 6778
prices
(345, 678, 987, 6778)
rating=set(map(int,input("enter the rating:").split()))
enter the rating:5 4 3 2 5 4
rating
{2, 3, 4, 5}
per=list(map(float,input("enter the marks:").split()))
enter the marks:56.7 78.9 56.9
per
[56.7, 78.9, 56.9]
prices=tuple(map(float,input("enter the prices:").split()))
enter the prices:567 8967 4567 9876
prices
(567.0, 8967.0, 4567.0, 9876.0)
prices=set(map(float,input("enter the prices:").split()))
enter the prices:6657 789 4567
prices
{6657.0, 789.0, 4567.0}
a,b=10,20
a
10
b
20
a,b=(10,20)
a
10
b
20
a,b=[10,20]
a
10
b
20
username,password=input("enter username & password:").split()
enter username & password:codegnan c@123
username
'codegnan'
password
'c@123'
a,b,c,d=list(map(int,input("enter the sides of rectangles:").split()))
enter the sides of rectangles:4 5 8 7
a
4
b
5
c
8
d
7
price,discount=list(map(float,input("enter price & discount:").split()))
enter price & discount:34567 87
price
34567.0
discount
87.0
a=eval(input())
5678
a
5678
a=eval(input())
56.78
a
56.78
a=eval(input())
[1,2,3]
a
[1, 2, 3]
a=eval(input())
(12,3,4,5)
a
(12, 3, 4, 5)
a=eval(input())
{2,3,4,5}
a
{2, 3, 4, 5}
