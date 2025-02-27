class Bank:
    total_accounts = 0 # class level attributes
    
    def __init__(self, name):
        self.name = name
        Bank.total_accounts += 1
        
    @staticmethod
    def is_valid_account(account_number):  # Static method
        return len(str(account_number)) == 10
        
    @classmethod
    def get_total_accounts(cls): # class method
        return cls.total_accounts
    
    
# we can use static method as utility function
print(Bank.is_valid_account(1234567890))  # True
print(Bank.is_valid_account(12345))  # False

# we can track total objects created by using class method
b1 = Bank("Account 1")
b2 = Bank("Account 2")
print(f"Total number of accounts are created : {Bank.get_total_accounts()}")


class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):  # Instance method
        self.balance += amount
        return f"{self.account_holder} deposited {amount}. New balance: {self.balance}"

# instance method is useful when working with instance-specific data like a user's account balance
acc = BankAccount("Prashanth", 1000)
print(acc.deposit(500))  # Changes the instance balance
