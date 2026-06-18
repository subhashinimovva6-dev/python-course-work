'''
#1.positional arguments:
def display(name,email,password):
    print("Name:",name)
    print("Email:",email)
    print("Password:",password)
display('subha','subhashinimovva6@gmail.com','subha@123')
display('subha@123','subhashinimovva6@gmail.com','subha')
display('subhashinimovva6@gmail.com','subha','subha@123')

#2.keyword:
def display(name,email,password):
    print("Name:",name)
    print("Email:",email)
    print("Password:",password)
display(name='subha',email='subhashinimovva6@gmail.com',password='subha@123')
display(password='subha@123',email='subhashinimovva6@gmail.com',name='subha')
display(email='subhashinimovva6@gmail.com',name='subha',password='subha@123')
'''
#keyword variable lenth:
def display(**names):
    print("Names:",names)
display(k1='subha',k2='harika',k3='maha',k4='gaya')
display(k1='subha',k2='harika',k3='maha')
display(k1='subha',k2='harika')
'''
#3.default:
def display(name,email,password=''):
    print("Name:",name)
    print("Email:",email)
    print("Password:",password)
display('subha','subhashinimovva6@gmail.com')
display('subha@123','subhashinimovva6@gmail.com','subha')

#variable length:
def display(*names):
    print("Names:",names)
display('subha','harika','maha','gaya')
display('subha','harika','maha')
display('subha','harika')

'''


    
