#Write a Python code to check if a number is even or odd

# Function to check if a number is even or odd
def check_even_odd(number1):
    if number1 % 2 == 0:
        return f"{number1} is Even"
    else:
        return f"{number1} is Odd"




print("\n--- Test with some examples ---")
def check_even_odd(number):
    if number % 2 == 0:
        return f"{number} is Even"
    else:
        return f"{number} is Odd"

# Test with some examples
numbers = [0, 1, 7, 12, 25, 100, -3, -8]
for num in numbers:
    print(check_even_odd(num))

print("\n\n*** SEPARATE ODD AND EVEN NUMBERS WITH TRANSFORMATIONS ***")
print("Odd numbers are squared, Even numbers are cubed\n")

# Function to separate and transform odd/even numbers
def separate_odd_even_transform(numbers):
    odd_list = []
    even_list = []
    
    for num in numbers:
        if num % 2 == 0:
            even_list.append(num ** 3)  # Cube the even number
        else:
            odd_list.append(num ** 2)   # Square the odd number
    
    return odd_list, even_list

# Test with examples
test_numbers = [0, 1, 7, 12, 25, 100, -3, -8, 5, 10, 15, 20]
odd_squared, even_cubed = separate_odd_even_transform(test_numbers)

print(f"Original Numbers: {test_numbers}")
print(f"Odd Numbers (Squared): {odd_squared}")
print(f"Even Numbers (Cubed): {even_cubed}")



