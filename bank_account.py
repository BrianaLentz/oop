class BankAccount:
    
# don't forget to add some default values for these parameters!
    def __init__(self, name, int_rate, balance): 
        self.int_rate = int_rate
        self.balance = balance
        self.name = name
#  (remember, instance attributes go here)
# don't worry about user info here; we'll involve the User class soon
    def deposit(self, amount):
        self.balance += amount
        print(f"{self.name} made a deposit of {amount}")
        return self

    def withdraw(self, amount):
        if self.balance - amount <= 0:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
            return self
        self.balance -= amount
        print(f"{self.name} made a withdrawal of {amount}")
        return self
        
    def display_account_info(self):
        print(f"Balance:${self.balance:.2f}")
        return self

    def yield_interest(self):
        self.balance += self.balance * self.int_rate
        return self

account1 = BankAccount('Account1', .075, 5000)
account2 = BankAccount('Account2', .075, 2000)

account1.deposit(50).deposit(100).deposit(25).withdraw(6000).yield_interest()

account1.display_account_info()

account2.deposit(100).deposit(25).withdraw(15).withdraw(40).withdraw(20).withdraw(10).yield_interest()

account2.display_account_info()
