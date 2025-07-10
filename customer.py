class Customer:
    def __init__(self, name, account_number, password):
        self.name = name
        self.account_number = account_number
        self.password = password

    def display_details(self):
        print(f"Customer Name: {self.name}")
        print(f"Account Number: {self.account_number}")
