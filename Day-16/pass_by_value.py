'''#integer
def update(n):
    n+=10
    print("inside:",n)

n=10
update(n)
print("Outside",n)


#float:
def update(n):
    n+=10
    print("inside:",n)

n=13.4
update(n)
print("Outside",n)

#complex:
def update(n):
    n+=10
    print("inside:",n)

n=5+7j
update(n)
print("Outside",n)

#str:
def update(n):
    n.update(lang)
    print("inside:",n)

n="python"
update(n)
print("Outside",n)


#list:
def update(n):
    n+=[1,2,3,4,5]
    print("inside:",n)

n=[1,2,3,4]
update(n)
print("Outside",n)

#tuple:
def update(n):
    n+=(1,2,3,4,5)
    print("inside:",n)

n=(1,2,3,4)
update(n)
print("Outside",n)
'''
#set:
def update(n):
    n+={1,2,3,4,5}
    print("inside:",n)

n={1,2,3,4}
update(n)
print("Outside",n)
