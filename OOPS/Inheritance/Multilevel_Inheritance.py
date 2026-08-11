#In multilevel inheritance, features of the base class and the derived class are further inherited into the new derived class.
#This is similar to a relationship representing a child and a grandfather.
"""
Object
   │
   ▼
GrandParent
   │
   ▼
Parent
   │
   ▼
Child

========================================

class GrandParent:
    pass

class Parent(GrandParent):
    pass

class Child(Parent):
    pass
"""
# Base class
class Grandfather:
    def __init__(self, grandfathername):
        self.grandfathername = grandfathername

# Intermediate class
class Father(Grandfather):
    def __init__(self, fathername, grandfathername):
        self.fathername = fathername
        # Call the constructor of Grandfather
        Grandfather.__init__(self, grandfathername)

# Derived class
class Son(Father):
    def __init__(self, sonname, fathername, grandfathername):
        self.sonname = sonname
        # Call the constructor of Father
        Father.__init__(self, fathername, grandfathername)

    def print_name(self):
        print('Grandfather name :', self.grandfathername)
        print('Father name :', self.fathername)
        print('Son name :', self.sonname)

# Driver code
s1 = Son('Prince', 'Rampal', 'Lal mani')
print(s1.grandfathername)
s1.print_name()

#Example of Multilevel Inheritance banking system
print("====================================================================")
class Customer:
    """
    Level 1 (Grand Parent Class)
    Responsible for Customer/KYC information.
    """
    bank_name = "ABC National Bank"

    def __init__(self, customer_id, customer_name, mobile, kyc_completed):
        self.customer_id = customer_id
        self.customer_name = customer_name
        self.mobile = mobile
        self.kyc_completed = kyc_completed


class Account(Customer):

    """
    Level 2 (Parent Class)
    Responsible for Account operations.
    """
    def __init__(self,
                 customer_id,
                 customer_name,
                 mobile,
                 kyc_completed,
                 account_number,
                 balance,
                 account_status):

        super().__init__(
            customer_id,
            customer_name,
            mobile,
            kyc_completed
        )

        self.account_number = account_number
        self.balance = balance
        self.account_status = account_status

    def deposit(self, amount):

        if amount <= 0:
            print("Deposit amount must be greater than zero.")
            return

        self.balance += amount
        print(f"₹{amount} Deposited Successfully")

    def show_balance(self):
        print(f"Available Balance : ₹{self.balance}")


class SavingsAccount(Account):
    """
    Level 3 (Child Class)
    Savings Account specific features.

    """

    MINIMUM_BALANCE = 1000
    DAILY_WITHDRAWAL_LIMIT = 50000

    def __init__(self,
                 customer_id,
                 customer_name,
                 mobile,
                 kyc_completed,
                 account_number,
                 balance,
                 account_status,
                 interest_rate):

        super().__init__(
            customer_id,
            customer_name,
            mobile,
            kyc_completed,
            account_number,
            balance,
            account_status
        )

        self.interest_rate = interest_rate
        self.daily_withdrawn = 0

    def withdraw(self, amount):

        # Restriction 1
        if self.account_status != "ACTIVE":
            print("Transaction Failed : Account is not active.")
            return

        # Restriction 2
        if not self.kyc_completed:
            print("Transaction Failed : Complete KYC first.")
            return

        # Restriction 3
        if amount <= 0:
            print("Invalid withdrawal amount.")
            return

        # Restriction 4
        if amount > self.balance:
            print("Insufficient Balance.")
            return

        # Restriction 5
        if self.balance - amount < self.MINIMUM_BALANCE:
            print("Minimum balance of ₹1000 must be maintained.")
            return

        # Restriction 6
        if self.daily_withdrawn + amount > self.DAILY_WITHDRAWAL_LIMIT:
            print("Daily withdrawal limit exceeded.")
            return

        self.balance -= amount
        self.daily_withdrawn += amount

        print("Withdrawal Successful")
        print(f"Withdrawn : ₹{amount}")
        print(f"Remaining Balance : ₹{self.balance}")

    def calculate_interest(self):

        interest = self.balance * self.interest_rate / 100
        print(f"Interest Earned : ₹{interest:.2f}")


saving = SavingsAccount(
    customer_id=101,
    customer_name="Sankar",
    mobile="9876543210",
    kyc_completed=True,
    account_number="SB10001",
    balance=60000,
    account_status="ACTIVE",
    interest_rate=4.5
)

saving.withdraw(15000)
saving.show_balance()
saving.calculate_interest()

'''
                                object
                                   │
                                   ▼
                     ┌──────────────────────────┐
                     │        Customer          │
                     ├──────────────────────────┤
                     │ customer_id             │
                     │ customer_name           │
                     │ mobile                  │
                     ├──────────────────────────┤
                     │ customer_details()      │
                     │ bank_details()          │
                     │ validate_mobile()       │
                     └──────────────────────────┘
                                   │
                                   │ inherits
                                   ▼
                     ┌──────────────────────────┐
                     │         Account          │
                     ├──────────────────────────┤
                     │ account_number          │
                     │ balance                 │
                     ├──────────────────────────┤
                     │ deposit()               │
                     │ withdraw()              │
                     │ show_balance()          │
                     └──────────────────────────┘
                                   │
                                   │ inherits
                                   ▼
                  ┌────────────────────────────────┐
                  │      SavingsAccount            │
                  ├────────────────────────────────┤
                  │ interest_rate                 │
                  │ MINIMUM_BALANCE               │
                  ├────────────────────────────────┤
                  │ calculate_interest()          │
                  │ withdraw()  (Overridden)      │
                  └────────────────────────────────┘
'''