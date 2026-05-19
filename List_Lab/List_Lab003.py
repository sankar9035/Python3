#The most Pythonic way to build and filter lists. Equivalent to map/filter but far more readable.
# Filter even numbers and square them
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_squares = [x**2 for x in numbers if x % 2 == 0]

# Nested comprehension — 3x3 matrix
matrix = [[i * j for j in range(1,4)] for i in range(1,4)]

# Flatten the matrix
flat = [val for row in matrix for val in row]

print(even_squares)
print(matrix)
print(flat)

# ==========================================
# STEP 1 — Define the list (mixed data)
# ==========================================
my_list = ["madam", "test", "level", "python"]

# ==========================================
# STEP 2 — Helper function: check palindrome
# ==========================================
def is_palindrome(value):
    # Only check strings — skip integers, floats etc.
    if isinstance(value, str):
        return value == value[::-1]   # reverse using slicing
    return False                       # non-strings → not palindrome

# ==========================================
# STEP 3 — Process list WITHOUT changing position
# ==========================================
result = []

for item in my_list:
    if is_palindrome(item):
        result.append(item.upper())   # palindrome → UPPERCASE
    else:
        result.append(item)           # not palindrome → keep as is

# ==========================================
# STEP 4 — Print output
# ==========================================
print("Input  :", my_list)
print("Output :", result)

# Bonus — handles mixed types safely!
my_list = ["madam", 123, "level", 45.6, "python", True]

result = [item.upper() if is_palindrome(item) else item for item in my_list]

print(result)

print("***********************************************")

# ==========================================
# STEP 1 — Define the list
# ==========================================
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# ==========================================
# STEP 2 — Separate odd and even
# ==========================================
odd_numbers  = [n for n in numbers if n % 2 != 0]
even_numbers = [n for n in numbers if n % 2 == 0]

print("Odd  Numbers :", odd_numbers)
print("Even Numbers :", even_numbers)

# ==========================================
# STEP 3 — Apply operations
# ==========================================
squared_odds  = [n ** 2 for n in odd_numbers]   # ODD  → Square (n²)
cubed_evens   = [n ** 3 for n in even_numbers]  # EVEN → Cube   (n³)

print("\nOdd  Squared :", squared_odds)
print("Even Cubed   :", cubed_evens)

# ==========================================
# STEP 4 — Combined result (preserving position)
# ==========================================
final_result = []

for n in numbers:
    if n % 2 != 0:
        final_result.append(n ** 2)   # odd  → square
    else:
        final_result.append(n ** 3)   # even → cube

print("\nOriginal List :", numbers)
print("Final Result  :", final_result)


# Bonus — handles mixed types safely!
my_list = ["madam", 123, "level", 45.6, "python", True]

result = [item.upper() if is_palindrome(item) else item for item in my_list]

print(result)
# Output: ['MADAM', 123, 'LEVEL', 45.6, 'python', True]
# integers, floats, booleans untouched

print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

def is_palindrome(val):
    # Only check if it's a string
    if isinstance(val, str):
        return val == val[::-1]
    return False
my_list = ["madam", 123, "level", 45.54, "python", True]
# 2. Add a type check inside the list comprehension
result = [
    item.upper() if (isinstance(item, str) and is_palindrome(item)) else item
    for item in my_list
]
print(result)