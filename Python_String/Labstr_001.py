'''
A String is a data structure in Python Programming that represents a sequence of characters.
It is an immutable data type.
Syntax of String Data Type.
string_variable = "Python Automation with Shankar"
'''

string_var = "Python is a versatile programming language"
print(string_var)
print(id(string_var))
print(type(string_var)) #That will show which type of data it is.

# Creating a String
# with single Quotes
String1 = 'Welcome to the Python Automation course'
print("String with the use of Single Quotes: ")
print(String1)
print(id(String1))

# Creating a String
# with double Quotes
String1 = "This is Shankar Rudrapaul"
print("\nString with the use of Double Quotes: ")
print(String1)
print(id(String1))

# Creating a String
# with triple Quotes
String1 = '''I'm a your trainer and I have "create this course"'''
print("\nString with the use of Triple Quotes: ")
print(String1)
print(id(String1))

# Creating String with triple
# Quotes allows multiple lines
String1 = '''keep
practicing programming
write code that will help to build logic'''
print("\nCreating a multiline String: ")
print(String1)
print(id(String1))
print("********************************************")
name1 = "shankar"
name1 = 'rudrapaul'
print(name1)
print(name1)
print(id(name1))
"""
name1 first value has assign as shankar and again next line value has given rudrapaul
while printing second value will print since we have re_assign or change the value from shankar to rudrapaul
"""
print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")

'''
But below example same variable name2 has two different value here we are not re_assign the value.
once name2 value assign Amit we print but same variable_name again used to it's has different value.
here we are not re_assign the value.
'''
name2 = 'Amit'
print(name2)
print(id(name2))

name2 = 'Kumar'
print(name2)
print(id(name2))