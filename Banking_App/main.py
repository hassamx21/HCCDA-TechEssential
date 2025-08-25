# banking_app/main.py

from bankcore import create_account, login
from accounts import check_balance, deposit, withdraw

def main():
    """Main function to run the banking application."""
    print("Welcome to ABC Bank")
    
    while True:
        print("\nSelect 1 or 2:")
        print("1. Login to the account")
        print("2. Create an account")
        choice = input("Enter your choice (1 or 2, or 'q' to quit): ")
        
        if choice == 'q':
            print("Thank you for using ABC Bank!")
            break
        
        if choice == '1':
            customer_id = input("Enter customer ID: ")
            password = input("Enter password: ")
            if login(customer_id, password):
                while True:
                    print("\nSelect an option:")
                    print("1. Check balance")
                    print("2. Deposit money")
                    print("3. Withdraw money")
                    print("4. Logout")
                    action = input("Enter your choice (1-4): ")
                    
                    if action == '1':
                        balance = check_balance(customer_id)
                        print(f"Current balance: {balance}")
                    elif action == '2':
                        try:
                            amount = float(input("Enter amount to deposit: "))
                            deposit(customer_id, amount)
                        except ValueError:
                            print("Invalid amount entered")
                    elif action == '3':
                        try:
                            amount = float(input("Enter amount to withdraw: "))
                            withdraw(customer_id, amount)
                        except ValueError:
                            print("Invalid amount entered")
                    elif action == '4':
                        print("Logged out successfully")
                        break
                    else:
                        print("Invalid choice")
        
        elif choice == '2':
            name = input("Enter your name: ")
            password = input("Enter your password: ")
            customer_id = create_account(name, password)
            print(f"Please note your customer ID: {customer_id}")
        
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()