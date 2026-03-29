# Python is case sensitivity.
# python Data_type
'''
primitive data types: integers, floats, booleans and strings
non_primitive data types(also known as sequential data type): lists, tuples, dictionaries, and sets
mutable data type: List, Dict, Set.
Immutable data type: number, string, booleans, Byte, Tuple
There are different name has given based on their characteristic like mutable data type which we can modify.
immutable data type which we can not change after created
'''

'''semantics in python take an example of assigning variable, during rune time that why python is dynamically type.
'''
# Numeric data type: Int, Float, Complex.
# Boolean type : bool
# Sequence Type : String, List and Tuple.
# Mapping type : Dict
# Set
# None
a = 10 # Integer this is called semantics no need to mention about type of variable.
b = 3.587 # Float
c = 10+20j # Complex first part is real and other part is Imaginary.
print(a)
print(type(a))
print(b)
print(type(b))
print(c)
print(type(c))

#input is the function which is used to take an input from user.

name = input("Please enter your name: ")
print(name)
print(type(name))
'''
anything we take input from user using input function it will take as string.
that we have convert into integer or other type as well.
'''

num1 = int(input("Please Enter first number: "))
num2 = int(input("Please enter the second number: "))
sum = num1 + num2
print("Sum of two number ", sum)

#line continuation: use backslash (\) to continue to the next line.
total = 1+5+4+6+5+8+7+9+3+2+\
    6+7+9+2+1
print(total)

