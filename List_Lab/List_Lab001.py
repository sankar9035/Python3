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