class bankaccount:
    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = balance

    def deposite(self,amount):
        if (amount >0):
            self.balance = self.balance + amount
        else:
            print("the deposite must be positive")

    def withdraw(self,amount):
        if(amount<0):
            print("the withdraw must be positive")
        elif (amount>self.balance):
            print("withdrawing more that balance is not possible")
        else:
            self.balance = self.balance - amount

class savings_account(bankaccount):
    def __init__(self,owner,balance,interest_rate):
        super().__init__(owner,balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        self.balance = self.balance + self.balance*self.interest_rate


savings =bankaccount("Ahnaf",1400)
print(f"the owner = {savings.owner}  \n  balance = {savings.balance}")
savings.deposite(88)
print(f" after depositing new balance is {savings.balance} ")
savings.deposite(-88)
print(f" after depositing new balance is {savings.balance} ")
savings.withdraw(-88)
print(f" after withdrawing new balance is {savings.balance} ")
savings.withdraw(988)
print(f" after withdrawing new balance is {savings.balance} ")
savings =savings_account("Ahnaf",balance=200,interest_rate=0.19)

