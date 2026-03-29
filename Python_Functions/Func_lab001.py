num = 24
if num % 2 == 0:
    print("number is even")
else:
    print("number is odd")


#same will wrap up with function.
def even_or_odd(num):
    if num % 2 == 0:
        print("number is even")
    else:
        print("number is odd")

#now have call the function.
#syntex: function_name(parameter)
even_or_odd(35)

#function with multiple parameters
def add(a,b):
    return a+b

result = add(2,3)
print(result)

def mul(x,y):
    z = x*y
    return z
op = mul(9,5)
print(op)

#default parameters
def greet(name):
    print(f"Hello {name} welcome to the paradise")
greet("sankar")

def greet(name="Guest"):
    print(f"Hello {name} welcome to the paradise")
greet("Ravi")
