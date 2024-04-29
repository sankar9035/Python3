# String Formatting with F-Strings
'''
PEP 498 introduced a new string formatting mechanism known as Literal String Interpolation or more commonly as F-strings.
To create an f-string in Python, prefix the string with the letter “f”.

'''

# f-string
name = "Shankar Rudrapaul"
print(f"My name is {name}.")

# Arithmetic operations using F-strings.
a = int(input("Enter the number which you would like to print the Table: "))
print(f"{a} table is  ", a*1)
print(f"{a} table is  ", a*2)
print(f"{a} table is  ", a*3)
print(f"{a} table is  ", a*4)
print(f"{a} table is  ", a*5)
print(f"{a} table is  ", a*6)
print(f"{a} table is  ", a*7)
print(f"{a} table is  ", a*8)
print(f"{a} table is  ", a*9)
print(f"{a} table is  ", a*10)
print("**********************************")
# Lambda Expressions using F-strings
print(f"She said her age is {(lambda x: x*9)(3)}")
#Float precision in the f-String Method
#Syntax: {value:{width}.{precision}}
'''
f-string formatting is used to interpolate the value of the num variable into the string
'''
print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
num = 3.14159265359
print(f"The value of pi is : {num:{1}.{5}}")
