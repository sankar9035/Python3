


def find_Average(n):          # n is the argument (list of numbers)
    sum_num = 0             # initialise sum

    for i in n:              # loop through every number in list
        sum_num = sum_num + i  # accumulate the sum

    avg = sum_num / len(n)   # divide by count → average
    print(n)
    return avg

# ── Main program ──────────────────────────────────
l = [5, 3, 8, 20, 15]
print("The average of list", find_Average(l))  # calling the function

#1. Reverse a list in place without using built-in functions.
#Why it’s asked: Tests basic pointer manipulation without relying on list.reverse() or [::-1].
def reverse_list(lst):
    left, right = 0, len(lst) - 1
    while left < right:
        lst[left], lst[right] = lst[right], lst[left]
        left += 1
        right -= 1
    return lst

# Test
print(reverse_list(["sankar", 1, "hello"]))  # Output: [5, 4, 3, 2, 1]