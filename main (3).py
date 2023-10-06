class BankAccount:
    def __init__(self, account_holder, balance=0.0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance: ${self.balance}")
        else:
            print("Invalid deposit amount. Amount must be greater than 0.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")
        else:
            print("Invalid withdrawal amount or insufficient balance.")

# Create an instance of BankAccount
account = BankAccount("John Doe", 1000.0)

# Test deposit and withdrawal functionality
account.deposit(500.0)  # Deposit $500. New balance: $1500.0
account.withdraw(200.0) # Withdrew $200. New balance: $1300.0
account.withdraw(1500.0) # Invalid withdrawal amount or insufficient balance.

