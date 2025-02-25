def second_largest(lst):
    return sorted(lst, reverse=True)[1]

print(second_largest([10, 45,2, 89,32]))