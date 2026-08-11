#Single inheritance enables a derived class to inherit properties from a single parent class,
#thus enabling code reusability and the addition of new features to existing code.
"""
Object
   │
   ▼
ParentClass
   │
   ▼
ChildClass
==================================
class Parent:
    pass

class Child(Parent):
    pass
"""
# Base class
class Parent:
    def func1(self):
        print("This function is in parent class.")

# Derived class
class Child(Parent):
    def func2(self):
        print("This function is in child class.")

# Driver code
obj = Child()
obj.func1()
obj.func2()

print("====================================================================")
#Example of Single Inheritance
class Account:
    """
    Parent Class (Base Class)

    Common functionality shared by all account types.
    """

    # Class Variable
    bank_name = "ABC National Bank"

    def __init__(self, account_number, customer_name, balance):
        self.account_number = account_number
        self.customer_name = customer_name
        self.balance = balance

    # Instance Method
    def deposit(self, amount):
        self.balance += amount
        print(f"₹{amount} deposited successfully.")

    # Instance Method
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"₹{amount} withdrawn successfully.")
        else:
            print("Insufficient Balance.")

    # Instance Method
    def show_balance(self):
        print(f"Available Balance : ₹{self.balance}")

    # Class Method
    @classmethod
    def bank_details(cls):
        print(f"Bank Name : {cls.bank_name}")

    # Static Method
    @staticmethod
    def validate_pan(pan):
        return len(pan) == 10


class SavingsAccount(Account):
    """
    Child Class

    Adds savings-account-specific behavior.
    """

    def __init__(self, account_number, customer_name, balance, interest_rate):
        super().__init__(account_number, customer_name, balance)
        self.interest_rate = interest_rate

    # Child Method
    def calculate_interest(self):
        interest = self.balance * self.interest_rate / 100
        print(f"Interest Earned : ₹{interest}")

    # Method Overriding
    def withdraw(self, amount):
        minimum_balance = 1000

        if self.balance - amount >= minimum_balance:
            self.balance -= amount
            print(f"₹{amount} withdrawn successfully.")
        else:
            print("Withdrawal denied. Minimum balance must be ₹1000.")
#Object creation and method calls

account = SavingsAccount(
    account_number="SB10024567",
    customer_name="Sankar Rudrapaul",
    balance=50000,
    interest_rate=4.5
)

account.deposit(5000)
account.withdraw(10000)
account.show_balance()
account.calculate_interest()

SavingsAccount.bank_details()

print(SavingsAccount.validate_pan("ABCDE1234F"))

#Industry Class Hierarchy
'''
                           object
                              │
                              ▼
                    ┌─────────────────┐
                    │     Account      │
                    ├─────────────────┤
                    │ bank_name       │
                    │ account_number  │
                    │ customer_name   │
                    │ balance         │
                    ├─────────────────┤
                    │ deposit()       │
                    │ withdraw()      │
                    │ show_balance()  │
                    │ bank_details()  │
                    │ validate_pan()  │
                    └─────────────────┘
                              │
                              │ inherits
                              ▼
                ┌──────────────────────────┐
                │    SavingsAccount        │
                ├──────────────────────────┤
                │ interest_rate            │
                ├──────────────────────────┤
                │ calculate_interest()     │
                │ withdraw()  (Override)   │
                └──────────────────────────┘
                
'''