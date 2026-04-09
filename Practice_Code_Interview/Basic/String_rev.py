def reverse_words_individually(input_string):
    """
    Reverses each word individually and reverses the order of words.
    Splits the input string into words: ["Python", "is", "good"]
    Reverses each word individually: ["nohtyP", "si", "doog"]
    Reverses the order of words: ["doog", "si", "nohtyP"]
    Joins them back: "doog si nohtyP"
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
#print(f"Expected: 'doog si nohtyP'")

