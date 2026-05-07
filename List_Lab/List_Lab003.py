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