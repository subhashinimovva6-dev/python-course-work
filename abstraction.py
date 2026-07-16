from abc import ABC, abstractmethod
class BankAccount(ABC):
    def checkbalance(self):
        print("you can checkout your balance")
    def viewhistory(self):
        print("you can your transactions")
    def userinfo(self):
        print("you can see your details")
    def transactions(self):
        print("you can transfer money through netbanking")
    @abstractmethod
    def deposit(self):
        pass
    @abstractmethod
    def withdraw(self):
        pass
class CurrentAccount(BankAccount):
    def deposit(self):
        print("You Can deposit - CA")
    def withdraw(self):
        print("you can withdraw - CA")   
class SavingAccount(BankAccount):
    def deposit(self):
        print("You Can deposit - SA")
    def withdraw(self):
        print("you can withdraw - SA")              
class FixedDeposit(BankAccount):
    def deposit(self):
        print("You Can deposit - FD")
    def withdraw(self):
        print("you can withdraw - FD")
class SalaryAccount(BankAccount):
    def deposit(self):
        print("You Can deposit - SA")
    def withdraw(self):
        print("you can withdraw - SA")
class ZeroBalanceAccount(BankAccount):
    def deposit(self):
        print("You Can deposit - ZBA")
    def withdraw(self):
        print("you can withdraw - ZBA")
subha = SalaryAccount()
subha.deposit()
subha.withdraw()
subha.checkbalance()
subha.viewhistory()
subha.userinfo()
subha.transactions()












        
