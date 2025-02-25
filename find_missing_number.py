def find_missing_number(lst, n):
    total_sum = n * (n + 1) // 2   # // is for integer division
    actual_sum = sum(lst)
    return total_sum - actual_sum

print(find_missing_number([1, 2, 4, 5, 6], 6))  