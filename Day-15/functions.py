'''
#syntax:
def function_namr(arg)
    #statement
    return
function_name(para)

#wish:

def wish(name):
    print(f'welcome to the python class {name}!')
wish('subha')
wish('harika')
wish('maha')
wish('gaya')

#iseven or odd:

def iseven(num):
    if num%2==0:
        return f"{num}-Even Number"
    else:
        return f"{num}-odd Number"
print(iseven(12))
print(iseven(13))

#factorial:

def factorial(num):
    fact=1
    for i in range(1,num+1):
        fact*=i
    return fact
num=int(input("Enter the number:"))
print("Factorial",factorial(num))
'''
#isprime:

def isprime(num):
    for i in range(2,num//2):
        if num%i==0:
            return f"{num} - not a prime number"
        return f"{num} - prime number"
num = int(input("enter the number:"))
print(isprime(num))
        
   
