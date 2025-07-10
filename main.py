from customer import Customer
from account import Account
import authentication

def main():
    accounts = {}

    while True:
        print("**** The Bank Management System ****")
        print("1. Create Account")
        print("2. Login")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter your name: ")
            account_number = input("Enter account number: ")
            password = input("Enter your password: ")

            cust = Customer(name, account_number, password)      #creating the customer obj
            authentication.register(cust)                        #calling the register method present in authentication
            acc = Account(account_number)                        #creating the account obj
            acc.create_account()                                 #calling the create account method
            accounts[account_number] = acc       #store an account object (acc) in a dictionary (accounts), using the account_number as the key.

        elif choice == '2':
            account_number = input("Enter account number: ")
            password = input("Enter your password: ")
            customer = authentication.login(account_number, password)   #calling login method present inside the authentication

            if customer:
                acc = accounts.get(account_number)         #get the account_number that is stored in the accounts dict
                while True:
                    print("**** Account Menu ****")
                    print("1. Deposit")
                    print("2. Withdraw")
                    print("3. Check Balance")
                    print("4. Customer Details")
                    print("5. Delete Account")
                    print("6. Logout")

                    choice = input("Enter your choice: ")

                    if choice == '1':
                        amt = float(input("Enter amount to deposit: "))
                        acc.deposit(amt)
                    elif choice == '2':
                        amt = float(input("Enter amount to withdraw: "))
                        acc.withdraw(amt)
                    elif choice == '3':
                        acc.display_balance()
                    elif choice == '4':
                        customer.display_details()
                    elif choice == '5':
                      if authentication.delete_account(account_number, password):
                        accounts.pop(account_number, None)
                        break
                    elif choice == '6':
                        print("Logged out.")
                        break
                    else:
                        print("Invalid choice.")

        elif choice == '3':
            print("Thankyou for visiting our system.")
            break
        else:
            print("Invalid input. Try again.")

if __name__ == "__main__":
    main()
