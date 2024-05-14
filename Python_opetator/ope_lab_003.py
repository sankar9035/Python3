'''
3. Assignment operators (=, +=, -=, *=, /=, %=, **=, &=, |=, ^=, >>=, <<=)
'''
# 1) Assign (=) : This operator is used to assign the value of the right side of the expression to the left side operand.
a = 9
b = 6
c = a + b
print(c)
# 2) Add and Assign(+=): This operator is used to add the right side operand with the left side operand and then assigning the result to the left operand.
# x += y
x = 8
x += x
print(x)

# 3) Subtract and Assign: This operator is used to subtract the right operand from the left operand and then assigning the result to the left operand.
# x -= y
x = 15
#y = 9
# x = x-y
x -= x
print(x)

#  4) Multiply and Assign: This operator is used to multiply the right operand with the left operand and then assigning the result to the left operand.
# x *= y
x = 11
y = 8
x *= y + x  # first x and y value will added than it's multiply with x value.
print(x)

# 5) Divide and Assign (/=): This operator is used to divide the left operand with the right operand and then assigning the result to the left operand.
# x /= y
a = 45
b = 3
# a = a / b
a /= b
print(a)

# 6) Modulus and Assign (%=): This operator is used to take the modulus using the left and the right operands and then assigning the result to the left operand.
# x %= y
x = 3
y = 5
# x = x % y
x %= y
print(x)

# 7) Divide (floor) and Assign (//=): This operator is used to divide the left operand with the right operand and then assigning the result(floor) to the left operand.
# x //= y
x = 3
y = 5
# x = x // y
x //= y
print(x)

#  8) Exponent and Assign (**=): This operator is used to calculate the exponent(raise power) value using operands and then assigning the result to the left operand.
# x **= y
x = 3
y = 5
# x = x ** y
x **= y
print(x)

# 9) Bitwise AND and Assign: This operator is used to perform Bitwise AND on both operands and then assigning the result to the left operand.
# x &= y
x = 3
y = 5
# x = x & y
x &= y
print(x)

# 10) Bitwise OR and Assign (|=): This operator is used to perform Bitwise OR on the operands and then assigning result to the left operand.
# x |= y

x = 3
y = 5
# x = x | y
x |= y
print(x)

# 11) Bitwise XOR and Assign (^=): This operator is used to perform Bitwise XOR on the operands and then assigning result to the left operand.
# x ^= y
x = 3
y = 5
# a = a ^ b
x ^= y
print(x)

# 12) Bitwise Right Shift and Assign: This operator is used to perform Bitwise right shift on the operands and then assigning result to the left operand.
# x >>= y

x = 3
y = 5
# x = x >> y
x >>= y
print(x)

# 13) Bitwise Left Shift and Assign: This operator is used to perform Bitwise left shift on the operands and then assigning result to the left operand.
# x <<= y

x = 3
y = 5
# x = x << y
x <<= y
print(x)