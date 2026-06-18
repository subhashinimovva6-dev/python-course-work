'''def func(num):
    if num == 0:
        return
    print(num,end='')
    func(num-1)
    print(num,end='')
    
func(5)

#sum of digits:
def sumofdigits(n):
    if n==0:
        return 0
    return n+sumofdigits(n-1)
print(sumofdigits(5))


#product of digits:
def productofdigits(n):
    if n==0:
        return 1
    return n*productofdigits(n-1)
print(productofdigits(5))
'''

#power:
def power(base,pow):
    if pow==0:
        return 1
    return base*power(base,pow-1)
print(power(2,4))

#reverse:
def reverseofstr(s,ind):
    if ind == 0:
        return s[0]
    return s[ind]+reverseofstr(s,ind-1)
l="pyton"
print(reverseofstr(l,len(l)-1))
