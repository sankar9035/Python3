mixed_list = [
    "madam",
    "racecar",
    "hello",
    121,
    12321,
    12345,
    "A man, a plan, a canal: Panama",
    "No lemon, no melon",
    "Python",
    -101,
    3.3
]

print("Processing the list...\n")

for item in mixed_list:
    # 1. Convert everything (strings, ints, floats) to a lowercase string
    original_str = str(item).lower()

    # 2. Clean the string: keep only letters and numbers (ignore spaces/punctuation)
    cleaned_str = ""
    for char in original_str:
        if char.isalnum():  # checks if character is a letter or a number
            cleaned_str += char

    # 3. Check if the cleaned string is a palindrome
    if cleaned_str == cleaned_str[::-1]:
        print(f"✅ '{item}' IS a palindrome")
    else:
        print(f"❌ '{item}' is NOT a palindrome")