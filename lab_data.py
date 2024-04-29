
# python Data_type
'''
primitive data types: integers, floats, booleans and strings
non primitive data types: lists, tuples, dictionaries, and sets
mutable data type: List, Dict, Set.
Immutable data type: number, string, booleans, Byte, Tuple
There are different name has given based on there characteristic like mutable data type which we can modify.
immutable data type which we can not change after created
'''
# Numeric data type: Int, Float, Complex.
# Boolean type : bool
# Sequence Type : String, List and Tuple.
# Mapping type : Dict
# Set
# None
a = 10
b = 3.587
c = 10+20j
print(a)
print(type(a))
print(b)
print(type(b))
print(c)
print(type(c))

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