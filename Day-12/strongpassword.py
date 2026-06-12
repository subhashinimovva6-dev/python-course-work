'''
password = input("Enter Password: ")

upper = lower = digit = special = 0

for ch in password:
    if ch.isupper():
        upper += 1
    elif ch.islower():
        lower += 1
    elif ch.isdigit():
        digit += 1
    else:
        special += 1

if len(password) >= 8 and upper >= 1 and lower >= 1 and digit >= 1 and special >= 1:
    print("Strong Password")
else:
    print("Weak Password")
'''
password = input("Enter Password: ")
if len(password)>=8:
    s=set()
    for i in password:
        if i.isupper():
            s.add('u')
        elif i.islower():
            s.add('l')
        elif i.isdigit():
            s.add('d')
        else:
            s.add('s')
    if len(s)==4:
        print("strong password")
    else:
        print("weak password")
else:
    print("weak password")
        
