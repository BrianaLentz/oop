


class User:
    def __init__(self , name):
        self.name = name
        self.amount = 500
        
    def make_deposit(self, amount):
        self.amount += amount
        return self
    def make_withdrawal(self, amount):
        self.amount -= amount
        return self
    def display_user_balance(self):
        print(f"User:{self.name}, Balance:{self.amount}")
        return self
        
briana = User("Briana")
brian = User("Brian")
michael = User("Michael")
briana.make_withdrawal(100).make_deposit(70).make_deposit(5).make_deposit(10).display_user_balance()
brian.make_deposit(100).make_deposit(30).make_withdrawal(300).make_withdrawal(50).display_user_balance()
michael.make_deposit(300).make_withdrawal(20).make_withdrawal(45).make_withdrawal(78).display_user_balance()



