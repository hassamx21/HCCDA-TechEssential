# banking_app/bankcore.py

# Module variables
branch_id = 2057
user_number = 0  # To track the user number for generating customer_id
users_info = {}  # Dictionary to store user info: {customer_id: [name, password]}

def generate_customer_id():
    """Generate a unique customer_id in the format branch_id-user_number."""
    global user_number
    user_number += 1
    return f"{branch_id}-{user_number}"

def create_account(name, password):
    """Register a new user with name and password."""
    customer_id = generate_customer_id()
    users_info[customer_id] = [name, password]
    print(f"Account created successfully! Your customer ID is {customer_id}")
    return customer_id

def login(customer_id, password):
    """Authenticate user based on customer_id and password."""
    if customer_id in users_info and users_info[customer_id][1] == password:
        print("Login successful!")
        return True
    else:
        print("Invalid login")
        return False