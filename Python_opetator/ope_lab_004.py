'''
4. logical operators (not, and, or)
'''

# 1) and: Returns True if both the operands are true.
# 2) or: Returns True if either of the operands is true.
# 3) not: Returns True if the operand is false.

# logical 'AND' operator
a = 17
b = 17
c = -17
if a > 0 and b > 0:
    print("The numbers are greater than 0")
if a > 0 and b > 0 and c > 0:
    print("The numbers are greater than 0")
else:
    print("Atleast one number is not greater than 0")

print("**********************************")
# logical 'AND' operator
a = 10
b = 12
c = 0
if a and b and c:
    print("All the numbers have boolean value as True")
else:
    print("Atleast one number has boolean value as False")

