# Reverse a string in Python without using inbuilt function

def rev_str(string):
    reverse = string[::-1]
    return reverse

str = "hello world"

result = rev_str(str)
print(result)

#2nd approach
def rev_s(s):
    str = ""
    for i in s:
        str = i + str
    return str
string = "welcome"
result = rev_s(string)
print(result)






