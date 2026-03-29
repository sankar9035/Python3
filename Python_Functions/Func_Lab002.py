#Possitional and Keyword argument
#Positional when required N-numbers of argument need to pass we used(*args).
#args are not a keyword it's a globally recommended can use any name instead of args.

def print_numbers(*args):
    for i in args:
        print(i)

print_numbers(1,2,3,4,5,6,7,8,9)
print("``````````````````")

x=3
print(x)
x%=x
print(x)



