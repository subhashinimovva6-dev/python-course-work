'''
#syntax:
var=lambda agr: exp

#add:
add=lambda a,b: a+b
print(add(12,13))

#wish:
wish=lambda name:f'welcome to the python class {name}'
print(wish('subha'))

#gst:
gst = lambda price:price+price*0.18
print(gst(1000))

#greatest:
greatest = lambda a,b : a if a>b else b
print(greatest(12,13))
print(greatest(2000,1990))
print(greatest(200,199))

#even:
is_even=lambda a:f"{a} num is even"if a%2==0 else f"{a} is odd"
print(is_even(7))
print(is_even(4))
print(is_even(5))

#chargers:
bill = lambda charge:charge if charge>99 else charge+30
print(bill(150))
print(bill(45))
print(bill(75))

#login:
login=True
instock=True
status = lambda login,instock:("you can buy a product"if instock else "product is out of stock") if login else"Login to buy a product"
print(status(login,instock))

#list:
l=[1,2,3,4,5,6]
res = list(map(lambda i:i**3,l))
print(res)

names=['subha','harika','maha']
t=list(map(lambda i:i.title(),names))
print(t)

#filter:

l=[1,2,3,4,5,6]
res = list(filter(lambda i:i%2==0,l))
print(res)

l=[1,2,3,4,5,6,7]
res = list(filter(lambda i:i>5,l))
print(res)

l=[1,2,3,4,5,6]
res = list(filter(lambda i:i%3==0,l))
print(res)

#reduce:
from functools import reduce
l=[1,2,3,4,5,6,7,8,9,10,11,12]
s=reduce(lambda sum,i:sum+i,l)
p=reduce(lambda pro,i:pro*i,l)
print(s,p)

from functools import reduce
l=[1,2,3,4,5,6,7,8,9,10,11,12]
s=reduce(lambda sum,i:sum+i,l)
p=reduce(lambda pro,i:pro*i,l)
m=reduce(lambda max,i:max if max>i else i,l)
min=reduce(lambda min,i:min if min<i else i,l)
print(s,p,m,min)
'''
#dictionary:
d={'subha':50,'harika':45,'maha':35,'gaya':25}
print(dict(sorted(d.items())))
print(dict(sorted(d.items(),key = lambda i:i[1])))
print(dict(sorted(d.items(),reverse=True)))
print(dict(sorted(d.items(),key = lambda i:i[1],reverse=True)))

