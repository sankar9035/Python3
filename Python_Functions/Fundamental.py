'''
A function is a block of code that perform a specific task. Function helps organized code, reusing code and improved readability.
---> Calling function
---> Function with parameters
---> Function with return value
---> Default parameters
---> Variable length arguments
---> Return statement
'''
#Syntax of function
"""
def function_name(parameter):
	'''docstring'''
	function body
	return expression
"""
# 1st approach to use function
def user_message(message):
	print(message)

#Taking input from user.
message1 = input("enter your message: ")

#Calling function
user_message(message1)

# 2nd approach to use function
def get_and_user_input():
	user_input = input("Enter your message: ")
	print(user_input)

#calling function
get_and_user_input()

#3rd approach to use function
def get_and_print_input(prompt_text):
	#pamameter prompt_text is use inside the input function
	user_input = input(prompt_text)
	print(user_input)

#calling function
get_and_print_input("Enter your message : ")

#calculate bill
print("Calculate bill")
def calculate_bill(price, tax_rate):
	tax_amount = price * tax_rate
	total_price = price + tax_amount
	return total_price

num1 = float(input("Enter the price: "))
num2 = float(input("Enter the tax_rate: "))

#calling function
my_bill = calculate_bill(num1, num2)
print(my_bill)

#Default parameter
def default_arg(name="Sankar"):
	return f"Hello {name} practice code that will make you a become better programmer!"

print(default_arg())


