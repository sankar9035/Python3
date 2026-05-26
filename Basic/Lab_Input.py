'''
--> print command which use to print anything. input is the function which use to take INPUT from user.
--->type() is a built-in function that is used to return the type of data stored in the objects or variables in the program.
---->id() function is a built-in function that returns the unique identifier of an object
means which represents the memory address of the object.
'''
print("*******************************************************")
"""
Python print() Function Syntax
Syntax : print(value(s), sep= ‘ ‘, end = ‘\n’, file=file, flush=flush)

Parameters:

value(s): Any value, and as many as you like. Will be converted to a string before printed
sep=’separator’ : (Optional) Specify how to separate the objects, if there is more than one.Default :’ ‘
end=’end’: (Optional) Specify what to print at the end.Default : ‘\n’
file : (Optional) An object with a write method. Default :sys.stdout
flush : (Optional) A Boolean, specifying if the output is flushed (True) or buffered (False). Default: False

"""
# value(s)
print("Hello world")

p = input("Please enter your best programing language: ")
print(p, "is best programing for beginner")
# Python “sep” parameter in print()
name = "Shankar"
age = 30
course = "python"
print(name, age, course, sep="-")
"""
Note: As sep, end, flush, and file are keyword arguments their position does not change the result of the code. 
Positional arguments cannot appear after keyword arguments. In the below example 10, 20 and 30 are positional arguments where sep=’ – ‘ is a keyword argument.
print(10, 20, sep=' - ', 30)
    print(10, 20, sep=' - ', 30)
                            ^
SyntaxError: positional argument follows keyword argument
"""
# Python “end” parameter in print()

# This line will automatically add a new line before the
# next print statement
print("Welcome to the python Automation testing course.")

# This print() function ends with "**" as set in the end argument.
print("We will learning python from basic to advance", end="**")
print("to automate our test cases")

'''
what is the different between below two line
print("result")
print(result)
'''

#1. print("result")
#What it does: Prints the exact word result.

#Why: The quotation marks "" turn the text into a string (a literal piece of text).
#Python doesn't look for any deeper meaning; it just prints exactly what is inside the quotes.

#2. print(result)
#What it does: Prints the value stored inside a variable named result.

#Why: Without quotes, Python treats result as a variable name.
#It will look back through your code to see what data you assigned to that variable and print that data instead.

result = 100

print("result")
print(result)

print("hello")
'''
1. print("hello") — Outputting Text
Because hello is wrapped in quotes ("hello"), Python treats it as a string (literal text).
It doesn't try to figure out what "hello" means; it just prints the letters directly to the screen.

Result: Outputs hello
'''

#--> print(world)
'''
2. print(world) — Looking for a Variable
Because world does not have quotes, Python thinks it is a variable (a container holding data).
It searches your code to see if you have defined world earlier (like writing world = "Earth").

Result: If you haven't defined it, Python will crash and give you a NameError: name 'world' is not defined.
'''