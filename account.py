class Account:
    def __init__(self, account_number):
        self.account_number = account_number
        self.balance = 0.0

    def create_account(self):
        print(f"Account {self.account_number} created successfully")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited Rs.{amount}. Available balance: RS.{self.balance}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawl Rs.{amount}. Available balance: Rs.{self.balance}")
        else:
            print("Invalid withdrawal amount or insufficient balance.")

    def display_balance(self):
        print(f"Total balance: Rs.{self.balance}")
