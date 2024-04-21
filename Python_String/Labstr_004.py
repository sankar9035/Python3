"""
Formatting of Strings
Strings in Python or string data type in Python can be formatted with the use of format() method
which is a very versatile and powerful tool for formatting Strings.
Format method in String contains curly braces {} as placeholders
which can hold arguments according to position or keyword to specify the order.

"""

# Python Program for
# Formatting of Strings
# Syntax: ‘String here {} then also {}’.format(‘something1′,’something2’)
# Default order
String1 = "{} {} {}".format('Python', 'Automation', 'Testing')
print("Print String in default order: ")
print(String1)

# Positional Formatting
String1 = "{1} {0} {2}".format('Python', 'Automation', 'Testing')
print("\nPrint String in Positional order: ")
print(String1)

# Keyword Formatting
String1 = "{P} {A} {T}".format(P='Python', A='Automation', T='Testing')
print("\nPrint String in order of Keywords: ")
print(String1)