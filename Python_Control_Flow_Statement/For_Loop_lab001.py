'''For Loops in Python are a special type of loop statement that is used for sequential traversal.
Python For loop is used for iterating over an iterable like a String, Tuple, List, Set, or Dictionary.
Syntex : for var in iterable:
            # statements
'''

# Reverse a string in Python without using inbuilt function
def findReverse(string):  #user-defined function
   # find reverse of string
   reverse = string[::-1]
   return reverse

# take inputs
string = input('Enter the string: ')

# calling function and display result
result = findReverse(string)
print('The reverse string is', result)
#=========
def reverse(s):
    str = ""
    for i in s:
        str = i+str
    return str
s = "sankar"
print(reverse(s))

#===================
def reverse_words_in_string(input_string):
    """
    Reverses the order of words in a given string.

    Args:
        input_string: The string to be processed.

    Returns:
        A new string with the words in reversed order.
    """
    words = input_string.split()  # Step 1: Split the string into words
    reversed_words = words[::-1]  # Step 2: Reverse the list of words
    reversed_string = ' '.join(reversed_words)  # Step 3: Join the words back
    return reversed_string

# Test cases
s1 = "Python is good"
print(f"Original: '{s1}'")
print(f"Reversed: '{reverse_words_in_string(s1)}'")

s2 = "Hello from Study tonight"
print(f"Original: '{s2}'")
print(f"Reversed: '{reverse_words_in_string(s2)}'")

a = 5
b = -a
print(b)

#===================
# Reverse each word AND reverse the order of words
def reverse_words_individually(input_string):
    """
    Reverses each word individually and reverses the order of words.
    Input: "Python is good"
    Output: "doog si nohtyp"

    Args:
        input_string: The string to be processed.

    Returns:
        A new string with each word reversed and words in reversed order.
    """
    words = input_string.split()  # Step 1: Split the string into words
    reversed_words = [word[::-1] for word in words]  # Step 2: Reverse each word
    reversed_words.reverse()  # Step 3: Reverse the order of words
    result = ' '.join(reversed_words)  # Step 4: Join the words back
    return result

# Test with the required example
print("\n--- Required Output ---")
test_input = "Python is good"
test_output = reverse_words_individually(test_input)
print(f"Input: '{test_input}'")
print(f"Output: '{test_output}'")
print(f"Expected: 'doog si nohtyP'")
