class User:
    def __init__(self , name):
        self.name = name
        self.account_balance = 500
    def make_deposit(self, amount):
        self.account_balance += amount

    def make_withdrawal(self, amount):
        self.account_balance -= amount

    def display_user_balance(self):
        print(f"User:{self.name}, Balance:{self.amount}")
        
briana = User("Briana")
brian = User("Brian")
michael = User("Michael")

briana.make_withdrawal(100)
briana.make_deposit(70)
briana.make_deposit(5)
briana.make_deposit(10)
print(briana.account_balance)

brian.make_deposit(100)
brian.make_deposit(30)
brian.make_withdrawal(300)
brian.make_withdrawal(50)
print(brian.account_balance)

michael.make_deposit(300)
michael.make_withdrawal(20)
michael.make_withdrawal(45)
michael.make_withdrawal(78)
print(michael.account_balance)
