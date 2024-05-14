'''
2.  Relational / Comparison operators (==, !=, >, <, >=, <=)

'''
x = 9
y = 7
z = 9
# Syntax: x == y (It returns True if both the operands are equal)
print(x == y)
print(x == z)
# Syntax: a != b (The Not Equal To Operator returns True if both the operands are not equal and returns False if both the operands are equal)
x = 9
y = 7
z = 9
print("Not Equal To Operator")
print(x != y)
print(x != z)
print("Greater than Sign")
# Syntax: x > y(The Greater Than Operator returns True if the left operand is greater than the right operand otherwise returns False)
print(x > y)
print(y > z)
print("Less than Sign")
# Syntax: a < b (The Less Than Operator returns True if the left operand is less than the right operand otherwise it returns False)
print(x < y)
print(y < z)
print("Greater than or Equal to Sign")
# Syntax: x >= y (The Greater Than or Equal To Operator returns True if the left operand is greater than or equal to the right operand, else it will return False)
print(x >= y)
print(x >= z)
print(y >= z)
print("Less than or Equal to Sign")
# Syntax: x <= y (The Less Than or Equal To Operator returns True if the left operand is less than or equal to the right operand)
print(x <= y)
print(x <= z)
print(y <= z)

a = 5

# chaining comparison operators
print(1 < a < 10)
print(10 > a <= 9)
print(5 != a > 4)
print(a < 10 < a*10 == 50)