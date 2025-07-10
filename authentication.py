customers = {}                               #It is dictionary, used to store the customer details as key and value pairs

def register(customer):                      #inherits the customer cls
    customers[customer.account_number] = {
        'password': customer.password,
        'customer': customer
    }

def login(account_number, password):
    user = customers.get(account_number)
    if user and user['password'] == password:    #if the user given password and password stored in the customer dict is same then print logged in
        print("Login successful!")
        return user['customer']
    else:
        print("Login failed. Invalid account number or password.")
        return None

def delete_account(account_number, password):
    user = customers.get(account_number)
    if user and user['password'] == password:
        del customers[account_number]
        print(f"Account {account_number} deleted successfully.")
        return True
    else:
        print("Deletion failed. Incorrect account number or password.")
        return False
