# banking_app/accounts.py

# Dictionary to store balance records: {customer_id: balance}
balance_record = {}

def check_balance(customer_id):
    """Return the current balance for the given customer_id."""
    if customer_id in balance_record:
        return balance_record[customer_id]
    else:
        print("No account found for this customer ID")
        return 0

def deposit(customer_id, amount):
    """Add the specified amount to the user's balance."""
    if amount <= 0:
        print("Invalid deposit amount")
        return
    if customer_id not in balance_record:
        balance_record[customer_id] = 0
    balance_record[customer_id] += amount
    print(f"Deposited {amount}. New balance: {balance_record[customer_id]}")

def withdraw(customer_id, amount):
    """Deduct the specified amount from the user's balance if sufficient funds are available."""
    if amount <= 0:
        print("Invalid withdrawal amount")
        return
    if customer_id in balance_record and balance_record[customer_id] >= amount:
        balance_record[customer_id] -= amount
        print(f"Withdrew {amount}. New balance: {balance_record[customer_id]}")
    else:
        print("Insufficient balance or invalid customer ID")