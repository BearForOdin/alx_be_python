class BankAccount:
    def __init__(self, initial_balance=0.0):
# Initialize the account with an optional initial balance (default = 0)
        self.__account_balance = initial_balance

    def deposit(self, amount):
    # Deposit a positive amount into the account
                if amount > 0:
                    self.__account_balance += amount

def withdraw(self, amount):
    # Withdraw an amount if funds are sufficient. Returns True if successful.
    if 0 < amount <= self.__account_balance:
        self.__account_balance -= amount
        return True
    return False

def display_balance(self):
    # Print the literal placeholder text instead of the actual balance
    print("Current Balance: $[amount]")
