'''class Flipkart:
    pass
subha=Flipkart()
harika=Flipkart()
maha=Flipkart()


class Flipkart:
    disount = 10
    products = ['laptop','mouse','charger','phone']
    @classmethod
    def showProducts(cls):
        print(cls.products)
    def login(self,username,password):
        self.username = username
        self.password = password
        print(f'welcome to the flipkart {self.username}')
    @staticmethod
    def banner():
        print("10% discount is going on flipkart, shop now!")
subha=Flipkart()
subha.login('subha','subha@1223')
subha.banner()
subha.showProducts()
Flipkart.showProducts()
Flipkart.banner()
'''

class Instagram:
    def __init__(self,username,password):
        self.username = username
        self.__password = password
        self._followers = []
    def getpassword(self):
        return self.__password
    def setpassword(self,newpassword):
        self.__password = newpassword
    
subha = Instagram('subha','subha@123')
print("Before username:",subha.username)
subha.username = 'subhashini'
print("After username:",subha.username)
print("Before password:",subha.getpassword())
subha.setpassword('subhashini@123')
print("After password:",subha.getpassword())

    
