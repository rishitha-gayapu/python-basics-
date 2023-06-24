class BankAccount:
    acc_no=1010101
    bal=50000
    date_of_opening=9-10-23
    cust_name="siri"
    def deposit(self,amt):
        self.bal+=amt
        print(self.bal)
    def withdraw(self,amt):
        if(wd<amt):
            self.bal-=wd-amt
            print(self.bal)
        else:
            print("insufficient bal")
    def check_bal(self):
        print("bal=",self.bal)
amt=int(input("enter amt"))
wd=int(input("enter wd"))
obj=BankAccount()
obj.deposit(amt)
obj.withdraw()
obj.check_bal()
