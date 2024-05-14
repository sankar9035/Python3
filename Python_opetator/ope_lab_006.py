'''
6. Identity Operators (is, is not) and Membership Operators (in, not in)
Identity operator: Identity operators are used to compare the objects, not if they are equal,
but if they are actually the same object, with the same memory location.
is : Return's True if both variable's are the same object.
is not : Return's True if both variable's are not the same object
'''
# Example of Identity operator
num1 = 5
num2 = 5

lst1 = [1, 2, 3]
lst2 = [1, 2, 3]
lst3 = lst1

print(id(lst1))
print(id(lst2))
print(id(lst3))
"""‘lst1’ and ‘lst2’ have same data, the output is still False.
This is because both the lists refers to different objects in the memory.
Where as when we assign ‘lst3’ the value of ‘lst1’, it returns True.
This is because we are directly giving the reference of ‘lst1’ to ‘lst3’.
"""
str1 = "hello world"
str2 = "hello world"
str3 = str1
print("*********************")
print(id(str1))
print(id(str2))
print(id(str3))
# using 'is' identity operator on different datatypes
print(num1 is num2)
print(lst1 is lst2)
print(lst1 is lst3)
print(str1 is str2)
print(str1 is str3)
# Difference between ‘==’ and ‘is’ Operator
# of 'is' and '==' operators
'''The equality (==) operator is used to compare the value of two variables,
 whereas the identities operator (is) used to compare the memory location of two variables'''
print("Different between is' and '==' operators")
lst1 = [1, 2, 3]
lst2 = [1, 2, 3]

# using 'is' and '==' operators
print(lst1 is lst2)
print(lst1 == lst2)

"""Membership Operators (in, not in) : are use to test if a sequence is presented in an object
in : Returns True if a sequence with the specified value is present in the object.
not in : Return True if a sequence with the specified value is not present in the object.
"""
# initialized some sequences
list1 = [1, 2, 3, 4, 5]
str1 = "Hello World"
set1 = {1, 2, 3, 4, 5}
dict1 = {1: "python", 2:"automation", 3:"testing"}
tup1 = (1, 2, 3, 4, 5)

# using membership 'in' operator
print(3 in list1)
print('E' in str1)
print(9 in set1)
print(1 in dict1)
print(10 in tup1)
print("not in Example:")
print(3 not in list1)
print('E' not in str1)
print(9 not in set1)
print(1 not in dict1)
print(10 not in tup1)