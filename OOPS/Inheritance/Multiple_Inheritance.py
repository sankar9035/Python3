#When a class can be derived from more than one base class this type of inheritance is called multiple inheritances.
#In multiple inheritances, all the features of the base classes are inherited into the derived class.

r"""
        Parent1      Parent2
            \          /
             \        /
              ▼      ▼
             ChildClass

========================================

class Parent1:
    pass

class Parent2:
    pass

class Child(Parent1, Parent2):
    pass

"""
#Basic example of Multiple Inheritance.
# Base class 1
class Mother:
    mothername = ""

    def mother(self):
        print(self.mothername)

# Base class 2
class Father:
    fathername = ""

    def father(self):
        print(self.fathername)

# Derived class
class Son(Mother, Father):
    def parents(self):
        print("Father :", self.fathername)
        print("Mother :", self.mothername)

# Driver code
s1 = Son()
s1.fathername = "RAM"
s1.mothername = "SITA"
s1.parents()

print("=================================================================")
#Banking system example of Multiple Inheritance.
class SavingsAccount:

    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"₹{amount} Deposited Successfully")

    def withdraw(self, amount):

        if amount <= self.balance:
            self.balance -= amount
            print(f"₹{amount} Withdrawn Successfully")
        else:
            print("Insufficient Balance")

    def show_balance(self):
        print(f"Balance : ₹{self.balance}")


class OnlineBanking:

    def login(self):
        print("Internet Banking Login Successful")

    def fund_transfer(self, amount, beneficiary):

        print(f"₹{amount} transferred to {beneficiary}")

    def change_password(self):
        print("Password Changed Successfully")


class PremiumSavingsAccount(SavingsAccount, OnlineBanking):

    def __init__(self,
                 account_number,
                 balance,
                 customer_name):

        super().__init__(account_number, balance)
        self.customer_name = customer_name

    def premium_benefits(self):
        print("Premium Cashback Enabled")

#Object Creation
customer = PremiumSavingsAccount(
    account_number="SB10001",
    balance=50000,
    customer_name="Sankar"
)

customer.login()

customer.deposit(10000)

customer.withdraw(5000)

customer.fund_transfer(8000, "Rahul")

customer.show_balance()

customer.premium_benefits()


r"""
                               object
                                  │
            ┌─────────────────────┴─────────────────────┐
            ▼                                           ▼
+---------------------------+             +----------------------------+
|      SavingsAccount       |             |      OnlineBanking         |
+---------------------------+             +----------------------------+
| account_number            |             | username                   |
| balance                   |             | encrypted_password         |
| interest_rate             |             | last_login                 |
+---------------------------+             +----------------------------+
| deposit()                 |             | login()                    |
| withdraw()                |             | logout()                   |
| show_balance()            |             | fund_transfer()            |
| calculate_interest()      |             | change_password()          |
+---------------------------+             +----------------------------+
                    \                               /
                     \                             /
                      \                           /
                       ▼                         ▼
              +-------------------------------------------+
              |        PremiumSavingsAccount              |
              +-------------------------------------------+
              | customer_name                             |
              | reward_points                             |
              +-------------------------------------------+
              | premium_benefits()                        |
              +-------------------------------------------+
              
"""