'''
4. logical operators (not, and, or)
'''

# 1) and: Returns True if both the operands are true.
# 2) or: Returns True if either of the operands is true.
# 3) not: Returns True if the operand is false.

# logical 'AND' operator: (The logical AND operator returns True if both the operands are True else it returns False)
a = 7
b = 17
c = -7
if a > 0 and b > 0:
    print("The numbers are greater than 0")
if a > 0 and b > 0 and c > 0:
    print("The numbers are greater than 0")
else:
    print("Atleast one number is not greater than 0")

print("**********************************")
# logical 'AND' operator
a = 9
b = 2
c = 0
if a and b and c:
    print("All the numbers have boolean value as True")
else:
    print("Atleast one number has boolean value as False")

# Logical OR operator: (Logical OR operator returns True if either of the operands is True)
# Python program to demonstrate
# logical or operator
print("Below logical OR operator Example:")
a = 9
b = -11
c = 0
if a > 0 or b > 0:
    print("Either of the number is greater than 0")
else:
    print("No number is greater than 0")
if b > 0 or c > 0:
    print("Either of the number is greater than 0")
else:
    print("No number is greater than 0")

# Logical NOT operator: (The logical not operator works with a single boolean value. If the boolean value is True it returns False)
print("Below Logical NOT operator")
a = 0
b = not a
print(b)
x = 5
if not x == 10:
    print("x is not equal to 10")
else:
    print("x is equal to 10")