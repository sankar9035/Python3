'''
Inheritance is a fundamental concept in object-oriented programming (OOP)
that allows a class (called a child or derived class) to inherit attributes and methods
from another class (called a parent or base class).
'''

class ParentClass:
    """
    Parent Class Documentation(DOCSTRING)
    """

    # Class Variable
    class_variable = "Parent"

    def __init__(self, parent_attribute):
        # Instance Variable
        self.parent_attribute = parent_attribute

    # Instance Method
    def parent_method(self):
        pass

    # Class Method
    @classmethod
    def parent_class_method(cls):
        pass

    # Static Method
    @staticmethod
    def parent_static_method():
        pass


class ChildClass(ParentClass):
    """
    Child Class Documentation(DOCSTRING)
    """

    # Class Variable
    child_class_variable = "Child"

    def __init__(self, parent_attribute, child_attribute):
        # Call Parent Constructor
        super().__init__(parent_attribute)

        # Child Instance Variable
        self.child_attribute = child_attribute

    # Child Instance Method
    def child_method(self):
        pass

    # Method Overriding
    def parent_method(self):
        print("Overridden Parent Method")

    # Child Class Method
    @classmethod
    def child_class_method(cls):
        pass

    # Child Static Method
    @staticmethod
    def child_static_method():
        pass


    '''
Object
│
├── Parent Class (Base Class / Super Class)
│      │
│      ├── Attributes
│      ├── Constructor
│      ├── Instance Methods
│      ├── Class Methods
│      └── Static Methods
│
└── Child Class (Derived Class / Subclass)
       │
       ├── Inherits Parent Members
       ├── Own Attributes
       ├── Own Constructor
       ├── Calls Parent Constructor (super())
       ├── Own Instance Methods
       ├── Method Overriding
       ├── Own Class Methods
       └── Own Static Methods
       
    '''