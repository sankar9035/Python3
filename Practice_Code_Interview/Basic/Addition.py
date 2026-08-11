def word_count(str):
    counts = dict()
    words = str.split()

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts

print(word_count('the quick brown fox jumps over the lazy dog.'))

print("*" *45)
test_str = "python program"

# using naive method to get count
# of each element in string
all_freq = {}

for i in test_str:
    if i in all_freq:
        all_freq[i] += 1
    else:
        all_freq[i] = 1

# printing result
print("Count of all characters in Python program is :\n", str(all_freq))
#What if I dont want how many space are the that count to skip
#First approach
test_str = "python program"
all_freq = {}
for i in test_str:
    if i != " ":
        if i in all_freq:
            all_freq[i] += 1
        else:
            all_freq[i] = 1
print(all_freq)

print("*" *45)
#Second approach
test_str = "python program"
test_str = test_str.replace(" ", "")
all_freq = {}
for i in test_str:
    if i in all_freq:
        all_freq[i] += 1
    else:
        all_freq[i] = 1
print(all_freq)

#Best approach for using continue(keywords) Skip spaces using continue it use when we want to skip some iteration in loop.
print("*" *45)
test_str = "tomorrow"

all_freq = {}

for i in test_str:
    if i == " ":
        continue

    if i in all_freq:
        all_freq[i] += 1
    else:
        all_freq[i] = 1

print(all_freq)

text = input("Enter a string: ")

freq = {}

# Count frequency of each character
for ch in text:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1
print(freq)
# Print character with its frequency in order of first occurrence
result = ""

for ch in freq:
    result += ch + str(freq[ch])

print(result)