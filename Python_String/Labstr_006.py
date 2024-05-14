# String Formatting with F-Strings
'''
PEP 498 introduced a new string formatting mechanism known as Literal String Interpolation or more commonly as F-strings.
To create an f-string in Python, prefix the string with the letter “f”.

'''

# f-string
name = "Shankar Rudrapaul"
print(f"My name is {name}.")

# Arithmetic operations using F-strings.
# a = int(input("Enter the number to print the tables for: "))
# print(f"{a} table of  {a}*1=", a*1)
# print(f"{a} table of  {a}*2=", a*2)
# print(f"{a} table of  {a}*3=", a*3)
# print(f"{a} table of  {a}*4=", a*4)
# print(f"{a} table of  {a}*5=", a*5)
# print(f"{a} table of  {a}*6=", a*6)
# print(f"{a} table of  {a}*7=", a*7)
# print(f"{a} table of  {a}*8=", a*8)
# print(f"{a} table of  {a}*9=", a*9)
# print(f"{a} table of  {a}*10=", a*10)
print("**********************************")
# Lambda Expressions using F-strings
print(f"He said his age is {(lambda x: x*9)(3)}")
#Float precision in the f-String Method
#Syntax: {value:{width}.{precision}}
'''
f-string formatting is used to interpolate the value of the num variable into the string
'''
print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
num = 3.14159265359
print(f"The value of pi is : {num:{1}.{5}}")
