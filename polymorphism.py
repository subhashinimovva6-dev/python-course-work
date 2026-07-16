'''
class Hotstar:
    def __init__(self,name):
        self.name = name
        print(f'Hi {self.name}, welcome to the Hotstar')
    def login(self):
        print("you can login")
    def dashboard(self):
        print("you can see the dashboard items")
    def search(self):
        print("you can search")
    def languages(self):
        print("you select the languages")
    def playcontrollers(self):
        print("you can pause and play the video")
    def ads(self):
        print("ads will run")
    def movies(self):
        print("you can limited access for movies")
    def sports(self):
        print("you can limited access for sports")
    def quality(self):
        print("limited quality")
subha = Hotstar('subha')
subha.login()
subha.dashboard()
subha.search()
subha.languages()
subha.playcontrollers()
subha.ads()
subha.movies()
subha.sports()
subha.quality()


class PremiumHotstar:
    def __init__(self,name):
        self.name = name
        print(f'Hi {self.name}, welcome to the Premium Hotstar')
    def ads(self):
        print("ads won't run")
    def movies(self):
        print("you can unlimited access for movies")
    def sports(self):
        print("you can watch sports")
    def quality(self):
        print("High quality")
subhashini = PremiumHotstar('subhashini')
subhashini.login()
subhashini.dashboard()
subhashini.search()
subhashini.languages()
subhashini.playcontrollers()
subhashini.ads()
subhashini.movies()
subhashini.sports()
subhashini.quality()

#operator overloading:
class Number:
    def __init__(self,n):
        self.n = n
    def __add__(self,other):
        return self.n+other.n
    def __sub__(self,other):
        return self.n-other.n
    def __mul__(self,other):
        return self.n*other.n
    def __truediv__(self,other):
        return self.n/other.n
    def __lt__(self,other):
        return self.n<other.n
    def __gt__(self,other):
        return self.n>other.n
    def __equal__(self,other):
        return self.n==other.n
    def __str__(self):
        return str(self.n)
n1 = Number(10)
n2 = Number(20)
print(n1+n2)
print(n1-n2)
print(n1*n2)
print(n1/n2)
print(n1<n2)
print(n1>n2)
print(n1==n2)
print(n1,n2)
'''

class payment:
    def pay(self,amount):
        pass
class creditcard(payment):
    def pay(self,amount):
        print(f"paid {amount} by creditcard")
class phonepay(payment):
    def pay(self,amount):
        print(f"paid {amount} by phonepay")
def checkout(payment_method):
    payment_method.pay(300)
checkout(creditcard())
checkout(phonepay())
        
































    
