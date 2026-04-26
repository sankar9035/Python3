'''
Method
1. Instance Method → the most common type, they take self as the first parameter and can access instance variables and other methods.
2. Class Method → defined with @classmethod decorator, they take cls as the first parameter and can access class variables and other class methods.
3. Static Method → defined with @staticmethod decorator, they do not take self or cls as parameters
and cannot access instance or class variables,they are like regular functions but belong to the class's namespace.
4. Magic Method → also known as dunder methods (double underscore), they have special names like __init__, __str__, __repr__, etc.,
and are used to define the behavior of objects in certain situations (e.g., when printing an object, when comparing objects, etc.).
'''

class BankAccount:

#Constructor method to initialize the attributes of the class
    def __init__(self, owner_name, account_number, balance):
        self.owner_name = owner_name
        self.account_number = account_number
        self.balance = balance

# Instance method to deposit money into the account
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance: {self.balance}")
# Instance method to withdraw money from the account
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")

    def get_balance(self):
        return self.balance

# Magic method to provide a string representation of the object
    def __str__(self):
        return f"BankAccount(owner_name='{self.owner_name}', account_number='{self.account_number}', balance={self.balance})"

# Create an instance of BankAccount
account1 = BankAccount("Sankar Rudrapal", "123456789", 1000)
# Use the deposit and withdraw methods
account1.deposit(500)  # Deposited 500. New balance: 1500
account1.withdraw(200)  # Withdrew 200. New balance: 1300
account1.withdraw(1500)  # Insufficient funds
account1.get_balance()  # 1300
# Print the account details using the __str__ method
print(account1)  # BankAccount(owner_name='123456789', account_number='None', balance=1300)

