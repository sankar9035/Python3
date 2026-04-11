#Write a Python code to check if a number is even or odd

# Function to check if a number is even or odd
def check_even_odd(number):
    if number % 2 == 0:
        return f"{number} is Even"
    else:
        return f"{number} is Odd"

# Input from the user
try:
    user_input = int(input("Enter a number: "))
    print(check_even_odd(user_input))
except ValueError:
    print("Invalid input! Please enter an integer.")

print("--- Test with some examples ---")
def check_even_odd(number):
    if number % 2 == 0:
        return f"{number} is Even"
    else:
        return f"{number} is Odd"

# Test with some examples
numbers = [0, 1, 7, 12, 25, 100, -3, -8]
for num in numbers:
    print(check_even_odd(num))

