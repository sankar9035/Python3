'''
Accessing characters in Python String.
This is called indexing. Python Programming and access its characters using positive and negative indexing value.
The 0th element will be the first character of the string whereas the -1th element is the last character of the string.

'''

# Python Program to Access
# characters of String

String1 = "Python automation testing"
print("Initial String: ")
print(String1)

# Printing First character
print("\nFirst character of String is: ")
print(String1[0])

# Printing Last character
print("\nLast character of String is: ")
print(String1[-1])

# # Index error
# name = "Shankar"
# print(name[10])
#     print(name[10])
# IndexError: string index out of range

"""
String Slicing,  we will use the string-slicing method to extract a substring of the original string.

"""

# Python Program to
# demonstrate String slicing

# Creating a String
String1 = "Automation testing with SRP"
print("Initial String: ")
print(String1)

# Printing 3rd to 12th character
print("\nSlicing characters from 3-12: ")
print(String1[3:12])

# Printing characters between
# 3rd and 2nd last character
print("\nSlicing characters between " + "3rd and 2nd last character: ")
print(String1[3:-2])