class BankAccount:
    
    def __init__(self, name, int_rate, balance): 
        self.int_rate = int_rate
        self.balance = balance
        self.name = name

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

# account1 = BankAccount('Account1', .075, 5000)
# account2 = BankAccount('Account2', .075, 2000)


# End Bank Account Class

# Start User Class


class User:
    def __init__(self , name):
        self.name = name
        self.account = BankAccount(int_rate=.075, balance=0, name=name)
        
    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self
    def make_withdrawal(self, amount):
        self.account.withdraw(amount)
        return self
    def display_user_balance(self):
        print(f"User:{self.name}, Balance:{self.account.balance}")
        return self
        


briana = User("Briana")

briana.make_deposit(100)
briana.display_user_balance()

