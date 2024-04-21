'''
Escape Sequencing in Python
To insert characters that are illegal in a string, use an escape character.
An escape character is a backslash \ followed by the character you want to insert.
To ignore the escape sequences in a String, r or R is used,
this implies that the string is a raw string and escape sequences inside it are to be ignored.
'''
# Using raw String to
# ignore Escape Sequences
String1 = r"This is \x47\x65\x65\x6b\x73 in \x48\x45\x58"
print("\nPrinting Raw String in HEX Format: ")
print(String1)

# Single Quote
# \'
txt = 'It\'s alright.'
print(txt)

# Backslash
# \\  --- if we want to print any backslash can mention double backslash.
txt = "This will insert one \\ (backslash)."
print(txt)

# New Line
# \n ---- this will used for new line by default in print fun() end with new line.

txt = "Hello\nWorld!"
print(txt)

#Octal value
# \ooo
#A backslash followed by three integers will result in a octal value:
txt = "\110\145\154\154\157"
print(txt)

