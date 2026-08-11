class Account:
    """Parent Class"""

    def __init__(self, account_number, holder_name, balance):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = balance

    def withdraw(self, amount):
        """Default Withdrawal"""
        pass


# ---------------------------------------------

class SavingsAccount(Account):

    MINIMUM_BALANCE = 1000

    def withdraw(self, amount):

        if amount <= 0:
            print("Invalid Amount")

        elif amount > self.balance:
            print("Insufficient Balance")

        elif self.balance - amount < self.MINIMUM_BALANCE:
            print(f"Minimum Balance of ₹{self.MINIMUM_BALANCE} must be maintained.")

        else:
            self.balance -= amount
            print(f"₹{amount} Withdrawn Successfully")
            print(f"Remaining Balance : ₹{self.balance}")


# ---------------------------------------------

class CurrentAccount(Account):

    OVERDRAFT_LIMIT = 50000

    def withdraw(self, amount):

        available = self.balance + self.OVERDRAFT_LIMIT

        if amount <= available:
            self.balance -= amount
            print(f"₹{amount} Withdrawn Successfully")
            print(f"Remaining Balance : ₹{self.balance}")
        else:
            print("Overdraft Limit Exceeded")


# ---------------------------------------------

class FixedDeposit(Account):

    def withdraw(self, amount):
        print("Withdrawal Not Allowed Before Maturity")


# =============================================
#                Main Program
# =============================================

print("Select Account Type")
print("1. Savings Account")
print("2. Current Account")
print("3. Fixed Deposit")

choice = int(input("Enter Choice : "))

account_number = input("Account Number : ")
holder_name = input("Account Holder Name : ")
balance = float(input("Current Balance : "))
amount = float(input("Enter Withdrawal Amount : "))

if choice == 1:
    account = SavingsAccount(account_number, holder_name, balance)

elif choice == 2:
    account = CurrentAccount(account_number, holder_name, balance)

elif choice == 3:
    account = FixedDeposit(account_number, holder_name, balance)

else:
    print("Invalid Choice")
    exit()

print("\n----- Transaction -----")
print("Account Holder :", account.holder_name)

# Same Method Call
account.withdraw(amount)