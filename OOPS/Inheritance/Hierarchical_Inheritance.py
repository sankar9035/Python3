#When more than one derived class are created from a single base this type of inheritance is called hierarchical inheritance.
#In this program, we have a parent (base) class and two child (derived) classes.
"""
           Object
              │
              ▼
         ParentClass
         /     |      \
        ▼      ▼       ▼
    Child1  Child2  Child3

=====================================================

class Parent:
    pass

class Child1(Parent):
    pass

class Child2(Parent):
    pass

class Child3(Parent):
    pass
"""
#Simple example of Hierarchical Inheritance.
# Base class
class Parent:
    def func1(self):
        print("This function is in parent class.")

# Derived class 1
class Child1(Parent):
    def func2(self):
        print("This function is in child 1.")

# Derived class 2
class Child2(Parent):
    def func3(self):
        print("This function is in child 2.")

# Driver code
object1 = Child1()
object2 = Child2()

object1.func1()
object1.func2()
object2.func1()
object2.func3()

print("====================================================================")

#Banking system example of Hierarchical Inheritance.

class Customer:
    """
    Parent Class
    """

    bank_name = "ABC National Bank"

    def __init__(self, customer_id, customer_name, mobile):

        self.customer_id = customer_id
        self.customer_name = customer_name
        self.mobile = mobile

    def customer_details(self):

        print(f"Customer ID   : {self.customer_id}")
        print(f"Customer Name : {self.customer_name}")
        print(f"Mobile        : {self.mobile}")


# --------------------------------------------

class SavingsAccount(Customer):

    def __init__(self,
                 customer_id,
                 customer_name,
                 mobile,
                 balance,
                 interest_rate):

        super().__init__(customer_id,
                         customer_name,
                         mobile)

        self.balance = balance
        self.interest_rate = interest_rate

    def calculate_interest(self):

        interest = self.balance * self.interest_rate / 100
        print(f"Savings Interest : ₹{interest:.2f}")


# --------------------------------------------

class CurrentAccount(Customer):

    def __init__(self,
                 customer_id,
                 customer_name,
                 mobile,
                 overdraft_limit):

        super().__init__(customer_id,
                         customer_name,
                         mobile)

        self.overdraft_limit = overdraft_limit

    def check_overdraft(self):

        print(f"Overdraft Limit : ₹{self.overdraft_limit}")


# --------------------------------------------

class SalaryAccount(Customer):

    def __init__(self,
                 customer_id,
                 customer_name,
                 mobile,
                 employer):

        super().__init__(customer_id,
                         customer_name,
                         mobile)

        self.employer = employer

    def salary_credit(self):

        print("Monthly salary credited successfully.")


# --------------------------------------------

class FixedDepositAccount(Customer):

    def __init__(self,
                 customer_id,
                 customer_name,
                 mobile,
                 amount,
                 tenure,
                 rate):

        super().__init__(customer_id,
                         customer_name,
                         mobile)

        self.amount = amount
        self.tenure = tenure
        self.rate = rate

    def maturity_amount(self):

        maturity = self.amount + (self.amount * self.rate * self.tenure / 100)

        print(f"Maturity Amount : ₹{maturity:.2f}")


saving = SavingsAccount(
    101,
    "Sankar",
    "9876543210",
    50000,
    4.5
)

current = CurrentAccount(
    102,
    "Rahul",
    "9876500000",
    100000
)

salary = SalaryAccount(
    103,
    "Anita",
    "9876511111",
    "Infosys"
)

fd = FixedDepositAccount(
    104,
    "David",
    "9876522222",
    200000,
    5,
    7.25
)

saving.customer_details()
saving.calculate_interest()

current.check_overdraft()

salary.salary_credit()

fd.maturity_amount()


"""
                                   object
                                      │
                                      ▼
                    ┌─────────────────────────────────┐
                    │            Customer             │
                    ├─────────────────────────────────┤
                    │ customer_id                     │
                    │ customer_name                   │
                    │ mobile                          │
                    │ kyc_completed                   │
                    ├─────────────────────────────────┤
                    │ customer_details()              │
                    └─────────────────────────────────┘
                           ▲        ▲        ▲        ▲
                           │        │        │        │
           ┌───────────────┘        │        │        └───────────────┐
           │                        │        │                        │
           ▼                        ▼        ▼                        ▼
┌─────────────────┐     ┌─────────────────┐    ┌─────────────────┐    ┌──────────────────┐
│ SavingsAccount  │     │ CurrentAccount  │    │ SalaryAccount   │    │ FixedDeposit     │
├─────────────────┤     ├─────────────────┤    ├─────────────────┤    ├──────────────────┤
│ interest_rate   │     │ overdraft_limit │    │ employer_name   │    │ tenure           │
│ min_balance     │     │                 │    │                 │    │ fd_rate          │
├─────────────────┤     ├─────────────────┤    ├─────────────────┤    ├──────────────────┤
│ calculate_      │     │ check_          │    │ salary_credit() │    │ maturity_amount()│
│ interest()      │     │ overdraft()     │    │                 │    │                  │
└─────────────────┘     └─────────────────┘    └─────────────────┘    └──────────────────┘
"""