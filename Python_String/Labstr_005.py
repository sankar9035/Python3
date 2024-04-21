'''
Python Docstrings:
Python documentation strings (or docstrings) provide a convenient way of associating documentation with Python modules, functions, classes, and methods.
Declaring Docstrings: The docstrings are declared using ”’triple single quotes”’ or “”” triple double quotes “””
just below the class, method, or function declaration. All functions should have a docstring.
Accessing Docstrings: The docstrings can be accessed using the __doc__ method of the object or using the help function.
The below examples demonstrate how to declare and access a docstring.
Docstrings in Python

Triple-Quoted Strings
Google Style Docstrings
Numpydoc Style Docstrings
One-line Docstrings
Multi-line Docstrings
Indentation in Docstrings
Docstrings in Classes
Difference between Python comments and docstrings
'''

# Example: 1

def my_function():
    '''Demonstrates triple double quotes
    docstrings and does nothing really.'''

    return None
print("Using __doc__:")
print(my_function.__doc__)

print("Using help:")
help(my_function)

print("****************************************")

def power(a, b):
    '''This is single line Doc_String returns arg1 raised to power arg2'''

    return a**b
print(power.__doc__)
print(power(5, 6))

print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
# Multi-line Docstrings
def add_number(a, b):
    """
    This function takes two numbers as input and returns their sum.

    Parameters:
    a (int): The first number.
    b (int): The second number.

    Returns:
    int: The sum of a and b.
  """
    return a+b
print(add_number.__doc__)
print(add_number(5, 8))