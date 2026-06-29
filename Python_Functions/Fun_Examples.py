'''
1. Temperature conversion.
2. Password strength checking.
3. Calculate the total cost of item in a shopping cart.
4. Check if a string is palindrome or not.
5. Calculate the factorials of a number using recursion.
'''
#1. Temperature conversion.
#Celsius to Fahrenheit formulae: F = (C * 9/5) + 32.
#Fahrenheit to Celsius formulae: C = (F - 32) * 5/9.

def temp_conversion(temp, unit):
	if unit == 'C':
		return (temp*9/5)+32
	elif unit == 'F':
		return (temp-32)*5/9
	else:
		return None


#calling function
print(temp_conversion(45, 'C'))
print(temp_conversion(113, 'F'))


#2. Password strength checking.
