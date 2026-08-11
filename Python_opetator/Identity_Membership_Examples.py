# Identity Operators (is, is not)
# These operators compare the memory location (identity) of two objects.

print("--- Identity Operators ---")
a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(f"a: {a}, id: {id(a)}")
print(f"b: {b}, id: {id(b)}")
print(f"c: {c}, id: {id(c)}")

# 'is' returns True if both variables point to the same object
print(f"a is b: {a is b}")      # False: same content, different objects
print(f"a is c: {a is c}")      # True: c is a reference to a

# 'is not' returns True if both variables point to different objects
print(f"a is not b: {a is not b}") # True
print(f"a is not c: {a is not c}") # False

# Comparison with '==' (Equality)
print("\n--- Identity (is) vs Equality (==) ---")
print(f"a == b: {a == b}")      # True: values are equal
print(f"a is b: {a is b}")      # False: objects are different

# Membership Operators (in, not in)
# These operators test if a value is a member of a sequence (list, string, tuple, etc.)

print("\n--- Membership Operators ---")
fruits = ["apple", "banana", "cherry"]
message = "Hello Python"

# 'in' returns True if the value exists in the sequence
print(f"'apple' in fruits: {'apple' in fruits}")   # True
print(f"'P' in message: {'P' in message}")         # True
print(f"'z' in fruits: {'z' in fruits}")           # False

# 'not in' returns True if the value does NOT exist in the sequence
print(f"'orange' not in fruits: {'orange' not in fruits}") # True
print(f"'Java' not in message: {'Java' not in message}")   # True

