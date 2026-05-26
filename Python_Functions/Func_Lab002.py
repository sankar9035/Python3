""" Variable length argument """


#Possitional and Keyword argument
#Positional when required N-numbers of argument need to pass we used(*args).
#args are not a keyword it's a globally recommended can use any name instead of args.

def print_numbers(*args):
    for i in args:
        print(i)


print_numbers(1, 2, 3, 4, 5, 6, 7, 8, 9)
print("``````````````````")

x = 3
print(x)
x %= x
print(x)


def pos_key_argument(*args, **kwargs):
    for val in args:
        print(f"possitional arguments: {val}")

    for key, value in kwargs.items():
        # Correct way: .items() gives you both key and value
        print(f"{key}:{value}")

#calling function
pos_key_argument(1, 2, 3, 4, 5, 6, "sankar", name="sankar", age="32", country="india")

'''Method,              What it gives you,              Best used when...
kwargs.items(),         Both (Key & Value),             You need both and want clean code (Standard).
for key in kwargs,      Key only,                       You want to manually look up values or filter keys.
kwargs.values(),        Value only,                     "You don't care about the labels, just the data."
'''