'''
# local scope:

def display():
    n=10
    print("Inside:",n)
display()

    #global access:

n=10
def display():
   
    print("Inside:",n)
display()
print("outside:",n)

      #global access 2:

def display():
    global n
    n=10
    print("Inside:",n)
display()
print("outside:",n)

     #global access 3:

def display(n):
    #global n
    n+=10
    print("Inside:",n)
n=10
display(n)
print("outside:",n)

 #global access 4:

def display():
    global n
    n+=10
    print("Inside:",n)
n=10
display()
print("outside:",n)
'''
#non local:
def outer():
    n=10
    def inner():
        nonlocal n
        n+=10
        print("Inner function:",n)
    inner()
    print("outer function:",n)
outer()
