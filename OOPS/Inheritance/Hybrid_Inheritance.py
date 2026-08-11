#Hybrid inheritance is a combination of more than one type of inheritance.
#It uses a mix like single, multiple, or multilevel inheritance within the same program.
#Python's method resolution order (MRO) handles such cases.
r"""
              A
            /   \
           ▼     ▼
          B       C
           \     /
            ▼   ▼
              D

================================

class A:
    pass

class B(A):
    pass

class C(A):
    pass

class D(B, C):
    pass
"""
#Simple example of Hybrid Inheritance.
# Base class
class School:
    def func1(self):
        print("This function is in school.")

# Derived class 1 (Single Inheritance)
class Student1(School):
    def func2(self):
        print("This function is in student 1.")

# Derived class 2 (Another Single Inheritance)
class Student2(School):
    def func3(self):
        print("This function is in student 2.")

# Derived class 3 (Multiple Inheritance)
class Student3(Student1, School):
    def func4(self):
        print("This function is in student 3.")

# Driver code
obj = Student3()
obj.func1()
obj.func2()

print("====================================================================")

#banking system example of Hybrid Inheritance
class Customer:

    def __init__(self, customer_id, customer_name, mobile):
        self.customer_id = customer_id
        self.customer_name = customer_name
        self.mobile = mobile

    def customer_details(self):
        print(f"Customer : {self.customer_name}")


# ---------------- Hierarchical ----------------

class SalaryAccount(Customer):

    def __init__(self,
                 customer_id,
                 customer_name,
                 mobile,
                 employer):

        super().__init__(
            customer_id,
            customer_name,
            mobile
        )

        self.employer = employer

    def salary_credit(self, amount):
        print(f"Salary of ₹{amount} credited.")


class SavingsAccount(Customer):

    def __init__(self,
                 customer_id,
                 customer_name,
                 mobile,
                 interest_rate):

        super().__init__(
            customer_id,
            customer_name,
            mobile
        )

        self.interest_rate = interest_rate

    def calculate_interest(self, balance):
        interest = balance * self.interest_rate / 100
        print(f"Interest : ₹{interest:.2f}")


# ---------------- Independent Parent ----------------

class RewardsProgram:

    def __init__(self):
        self.reward_points = 0

    def earn_points(self, points):
        self.reward_points += points

    def redeem_points(self):
        print(f"Redeemed {self.reward_points} reward points.")


# ---------------- Hybrid ----------------

class PremiumSalaryAccount(SalaryAccount, RewardsProgram):

    def __init__(self,
                 customer_id,
                 customer_name,
                 mobile,
                 employer):

        SalaryAccount.__init__(
            self,
            customer_id,
            customer_name,
            mobile,
            employer
        )

        RewardsProgram.__init__(self)

    def premium_lounge_access(self):
        print("Premium Lounge Access Enabled")

premium = PremiumSalaryAccount(
    101,
    "Sankar",
    "9876543210",
    "TCS"
)

premium.customer_details()

premium.salary_credit(85000)

premium.earn_points(500)

premium.redeem_points()

premium.premium_lounge_access()

"""
                               object
                                  │
                                  ▼
                      ┌──────────────────────┐
                      │      Customer        │
                      ├──────────────────────┤
                      │ customer_id          │
                      │ customer_name        │
                      │ mobile              │
                      └──────────────────────┘
                          ▲             ▲
                          │             │
                ┌─────────┘             └─────────┐
                │                                 │
                ▼                                 ▼
      ┌──────────────────┐              ┌──────────────────┐
      │ SavingsAccount   │              │ SalaryAccount    │
      ├──────────────────┤              ├──────────────────┤
      │ interest_rate    │              │ employer_name    │
      │ calculate_       │              │ salary_credit()  │
      │ interest()       │              └──────────────────┘
      └──────────────────┘
                                              ▲
                                              │
                        ┌─────────────────────┴────────────────────┐
                        │                                          │
                        ▼                                          ▼
             ┌──────────────────┐                     ┌────────────────────┐
             │ RewardsProgram   │                     │ PremiumSalaryAccount│
             ├──────────────────┤                     ├────────────────────┤
             │ reward_points    │◄────────────────────┤ Hybrid Inheritance │
             │ redeem_points()  │      Multiple       │ premium_lounge()   │
             └──────────────────┘                     └────────────────────┘
"""