#ORDERED · MUTABLE · ALLOWS DUPLICATES · INDEXED
"""A list is Python's most versatile sequence type. Think of it as a dynamic array — you can add, remove, and modify items freely.
 Lists preserve the order of insertion, support indexing/slicing, and can hold mixed data types including other lists.
"""

# When to Use
# You need to add/remove items at runtime
# Order of items matters
# You need duplicate values
# You'll iterate or slice the collection
# Building queues, stacks, or dynamic sequences

'''
Where to Use (Real World)
Shopping cart items in e-commerce
Log messages or event history
API response arrays
Matrix rows in data science
Task/todo queues in applications
'''

'''
Method	     Description	            Example
append(x)	 Add item to end	        lst.append(5)
insert(i,x)	 Insert at index i	        lst.insert(0,'a')
remove(x)	 Remove first occurrence	lst.remove('a')
pop(i)	     Remove & return item	    lst.pop(-1)
sort()	     Sort in-place	            lst.sort(reverse=True)
index(x)	 Find index of item	        lst.index('a')
count(x)	 Count occurrences	        lst.count(5)
extend(lst2) Merge another iterable	    lst.extend([1,2])
'''

