'''
correct_password="admin123"
while True:
    password=input("Enter password:")
    if password===correct_password:
        print("password correct")
        break
    else:
        print("password incorrect")
'''   
pin=1234
for i in range(5):
    e_pin=int(input("Enter the pin:"))
    if e_pin==pin:
        print("unlock the phone")
        break
    else:
        print("incorrect pin")
else:
    print("Try again,after some time")
