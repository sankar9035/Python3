#Dynamic typing
## Python allows the type of variable to change as the program execute.
'''
Type System = Rules that define how a
programming language handles data types

Every variable stores some type of data:
→ Number    (int, float)
→ Text      (string)
→ True/False (boolean)
→ List, Dict, etc.

The question is → WHEN does the language check what type a variable is?

Python is dynamically typed because
   variable types are determined at RUNTIME,
   not at compile time. In Python, a variable
   is just a label that points to an object —
   the type belongs to the object/value, not
   the variable itself. This means the same
   variable can hold different types at
   different points in the program.

   For example:
   x = 10      → integer
   x = "hello" → string
   x = 3.14    → float

   Python allows this without any error.
   This makes Python flexible and easy to
   write but type errors are only caught
   at runtime, not before execution.

┌─────────────────┬─────────────────┐
│  STATIC TYPING  │ DYNAMIC TYPING  │
├─────────────────┼─────────────────┤
│ Type checked at │ Type checked at │
│ COMPILE time    │ RUNTIME         │
├─────────────────┼─────────────────┤
│ Must declare    │ No need to      │
│ type explicitly │ declare type    │
├─────────────────┼─────────────────┤
│ Java, C, C++,   │ Python, Ruby,   │
│ Swift, Kotlin   │ JavaScript, PHP │
└─────────────────┴─────────────────┘


'''

# In Python — variable is just a LABEL
# The VALUE carries the type, not the variable

x = 10          # x points to integer 10
x = "Hello"     # x now points to string
x = 3.14        # x now points to float
x = [1, 2, 3]   # x now points to a list
print(x)
# Python allows all of this — NO ERROR!
# The variable 'x' has no fixed type