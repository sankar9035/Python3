#CLASS
#OBJECTS
#INSTANTIATION

'''
Instantiation = Process of creating an
OBJECT from a CLASS

Class  → Blueprint / Template
Object → Real thing created from blueprint

Simple analogy:
Class  → House Blueprint (plan on paper)
Object → Actual House built from that plan

You can build MULTIPLE houses
from ONE blueprint — same way
you can create MULTIPLE objects
from ONE class


Class       → Template/Blueprint
Object      → Instance of a class
Instance    → Another word for Object
Instantiation → Act of creating an object

# These mean the SAME thing:
obj = MyClass()
→ "obj is an OBJECT of MyClass"
→ "obj is an INSTANCE of MyClass"
→ "We INSTANTIATED MyClass"
→ "We created an INSTANCE of MyClass"
'''


# Step 1 → Define a CLASS (Blueprint)
class Dog:

    def __init__(self, name, breed, age):
        # These are INSTANCE VARIABLES
        # Each object gets its OWN copy
        self.name = name
        self.breed = breed
        self.age = age

    def bark(self):
        return f"{self.name} says: Woof!"

    def info(self):
        return f"{self.name} is a {self.breed}, age {self.age}"


# Step 2 → INSTANTIATE (Create Objects)
dog1 = Dog("Tommy", "Labrador", 3)  # object 1
dog2 = Dog("Bruno", "Poodle", 5)  # object 2
dog3 = Dog("Max", "Husky", 2)  # object 3

# Step 3 → USE the objects
print(dog1.name)  # Tommy
print(dog2.breed)  # Poodle
print(dog3.age)  # 2

print(dog1.bark())  # Tommy says: Woof!
print(dog2.info())  # Bruno is a Poodle, age 5

'''
In Python OOP:

Variable   → General term for storing data
Attribute  → Variable that belongs to 
             a CLASS or OBJECT

Simple Rule:
→ Outside class = called VARIABLE
→ Inside class  = called ATTRIBUTE

x = 10              # this is a VARIABLE

class MyClass:
    x = 10          # this is an ATTRIBUTE
    self.x = 10     # this is also ATTRIBUTE
'''


class Student:

    def __init__(self, name, age, marks):
        #  ↓ self = current object
        self.name = name  # instance variable
        self.age = age  # instance variable
        self.marks = marks  # instance variable
        self.grade = "A"  # instance variable
        # with default value


# Creating 3 DIFFERENT objects
s1 = Student("Rahul", 20, 90)
s2 = Student("Priya", 22, 85)
s3 = Student("Amit", 21, 78)

# Each object has its OWN copy
print(s1.name, s1.age, s1.marks, s1.grade)  # Rahul 20 90
print(s2.name, s2.age, s2.marks)  # Priya 22 85
print(s3.name, s3.age, s3.marks)  # Amit  21 78

# Changing one does NOT affect others
s1.marks = 95
print(s1.marks)  # 95  → changed
print(s2.marks)  # 85  → unchanged
print(s3.marks)  # 78  → unchanged