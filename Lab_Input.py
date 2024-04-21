# print command wnich use to print anything. input is the function which use to take INPUT from user.
# type() is a built-in function that is used to return the type of data stored in the objects or variables in the program.
# id() function is a built-in function that returns the unique identifier of an object means which represents the memory address of the object.
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
#value(s)
print("Hello world")

p = input("Please enter your best programing language: ")
print(p, "is best programing for beginner")
#Python “sep” parameter in print()
name = "Shankar"
age = 30
course = "python"
print(name,age,course,sep="-")
"""
Note: As sep, end, flush, and file are keyword arguments their position does not change the result of the code. 
Positional arguments cannot appear after keyword arguments. In the below example 10, 20 and 30 are positional arguments where sep=’ – ‘ is a keyword argument.
print(10, 20, sep=' - ', 30)
    print(10, 20, sep=' - ', 30)
                            ^
SyntaxError: positional argument follows keyword argument
"""
#Python “end” parameter in print()

# This line will automatically add a new line before the
# next print statement
print ("Welcome to the python Automation testing course.")

# This print() function ends with "**" as set in the end argument.
print ("We will learning python from basic to advance", end= "**")
print("to automate our test cases")

#Taking multiple inputs from user in Python


