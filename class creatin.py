class BankAcount:
    acc_num="23245A"
    balance=1000
    date_of_opening="10-11-2003"
    coustomername="ramu"
    def deposit(self,addamount):
        print("amount addded")
        self.balance+=addamount
    def withdraw(self,amount):
        if amount<=self.balance:
            self.balance-=amount
            print("amount withdrawed")
        else:
            print("insufficient balance")
    def check_balance(self):
        print("balance ",self.balance)
obj1=BankAcount()
obj1.deposit(500)
obj1.withdraw(600)
obj1.check_balance()
