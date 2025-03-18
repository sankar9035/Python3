# Variable
'''
Python Variable is containers that store values. Python is not “statically typed”.
We do not need to declare variables before using them or declare their type. Python is dynamically type.
A variable is created the moment we first assign a value to it.
A Python variable is a name given to a memory location.
It is the basic unit of storage in a program.
In this article, we will see how to define a variable in Python.
LITERALS ARE THE ACTUAL VALUES ASSIGNED.
'''
# below one example.
# syntax of variable: variable_name = variable_value
# variable_name -> Identifiers (Variable names corresponded to Identifiers)
# variable_value -> Literals (Variable values corresponded to literals)

pi = 3.141
name = "Shankar"
print(pi)
print(name)
# Identifiers: It's a name which is used to identify.
# pi is Identifiers and 3.141 its a value
# there are certain rules to define Identifiers.

'''
rules to create Identifiers
we can use a-z, A-Z, 0-9 and underscore(_).
Identifiers should not start with Digits ex: 123total = 30.
Special symbols can not use.
keyword can not use as Identifiers
Identifiers are case sensitive. Total & total both are different.
Multi Words Variable Names:
 1) Camel Case: Each word, except the first, starts with a capital letter:
 example
        myVariableName = "Amit kumar"
2) Pascal Case: Each word starts with a capital letter:
 example:
        MyVariableName = "Ravikant kumar"
3) Snake Case: Each word is separated by an underscore character (This one is recommended)

example:
        my_variable_name = "Shankar Rudrapaul"
'''
# below all are Python Keywords

'''Keywords

and 	False	nonlocal
as	finally	not
assert	for	or
break	from	pass
class	global	raise
continue	if	return
def	import	True 
del	is	try
elif	in	while
else	lambda	with
except	None	yield'''
# an Identifiers can be any length.

total = 10
print(total)
print(id(total))
Total = 20
print(Total)
print(id(Total))
TOTAL = 30
print(TOTAL)
print(id(TOTAL))
