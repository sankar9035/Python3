'''
Type of operators.
1. Arithmetic operators (+, -, *, /, %, **)
2.  Relational / Comparison operators (==, !=, >, <, >=, <=)
3. Assignment operators (=, +=, -=, *=, /=, %=, **=)
4. logical operators (not, and, or)
5. Bitwise operators: (&, |, ^, ~, <<, >>).
6. Identity Operators (is, is not) and Membership Operators (in, not in)
>OPERATORS: These are the special symbols. Eg- + , * , /, etc.
>OPERAND: It is the value on which the operator is applied.
'''

# Arithmetic operators.
a = 10
b = 9
c = a + b
d = a - b
e = a * b
f = a / b
print(c)
print(id(c))
print(type(c))
print(d)
print(id(d))
print(type(d))
print(e)
print(id(e))
print(type(e))
print(f)
print(id(f))
print(type(f))
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
# Division Operators. 1) Float division(/). 2) Floor division(//).
# 1. Float division: The quotient returned by this operator is always a float number, no matter if two numbers are integers.

print(9/9)
print(55/5)
print(-26/2)
print(88.0/8)
print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
"""Integer division 2. (Floor division) :The quotient returned by this operator is dependent on the argument being passed.
If any of the numbers is float, it returns output in float.
It is also known as Floor division because, if any number is negative, then the output will be floored.
"""
print(10//3)
print(-55//5)
print(22.0//2)
print(-18.0//9)

"""
Precedence of Arithmetic Operators
The precedence of Arithmetic Operators in Python is as follows:

P – Parentheses
E – Exponentiation
M – Multiplication (Multiplication and division have the same precedence)
D – Division
A – Addition (Addition and subtraction have the same precedence)
S – Subtraction
"""
