# few more example of variables.

# Different mode of variable.
# 1st x = 5 : the normal way to define.
# 2nd _x , if any variable start with underscore its means its protected.
# 3rd __x , double underscore means private.
# 4th __x__ , any variable start with double underscore and end with double underscore it's a magic variable.
# To get in details about all types check PDF title "Different mode of variable". This concept is very important for OOPs concept.
# We will discuss in details in OOPs section.

# Simply define without any underscore
# Accessible from ANYWHERE
# NORMAL VARIABLE
x = 5
name = "Rahul"
age = 25


class MyClass:
    x = 100  # public variable

    def show(self):
        print(self.x)  # accessible inside class


obj = MyClass()
print(obj.x)  # accessible outside too
print(MyClass.x)  #accessible directly

# PROTECTED VARIABLE — _x
# Single underscore prefix
# Convention → "Hey! Handle with care"
# NOT strictly enforced by Python

class BankAccount:
    def __init__(self):
        self.name = "Rahul"  # public
        self._balance = 50000  # protected

    def show_balance(self):
        print(self._balance)  # ✅ accessible inside


class SavingsAccount(BankAccount):  # child class
    def show(self):
        print(self._balance)  # ✅ accessible in child


# Outside class
obj = BankAccount()
print(obj._balance)
# Python ALLOWS it but shows warning
# Convention says "Don't access directly"

#PRIVATE VARIABLE — __x
# Double underscore prefix
# NAME MANGLING happens here
# Python RENAMES it internally

class BankAccount:
    def __init__(self):
        self.name      = "Rahul"  # public
        self._balance  = 50000    # protected
        self.__pin     = 1234     # private ←

    def show_pin(self):
        print(self.__pin)         # works inside class

obj = BankAccount()
print(obj.name)       # Rahul
print(obj._balance)   # 50000 (with warning)
#print(obj.__pin)      # AttributeError!
                      # Cannot access from outside

# MAGIC VARIABLE — __x__
class Student:
    def __init__(self, name, age):  # constructor
        self.name = name
        self.age = age

    def __str__(self):  # string representation
        return f"Student: {self.name}"

    def __len__(self):  # len() behavior
        return self.age

    def __eq__(self, other):  # == behavior
        return self.name == other.name


s1 = Student("Rahul", 20)
s2 = Student("Priya", 22)

print(str(s1))  # Student: Rahul  (uses __str__)
print(len(s1))  # 20              (uses __len__)
print(s1 == s2)  # False           (uses __eq__)
