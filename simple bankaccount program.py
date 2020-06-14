class bankacct:
    def __init__(self,account):
        self.account=account
        
    def deposit(self,plus):
        self.account+=plus
        
    def withdraw(self,minus):
        if self.account<minus:
            print('인출 불가 : 잔액 부족')
        else:
            self.account-=minus
            
    def balance(self):
        print(self.account)
a=bankacct(1000)
a.balance()
a.deposit(100)
a.balance()
a.withdraw(500)
a.balance()
a.withdraw(1000)
