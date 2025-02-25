def factorial(num):
    try:
        if num == 0 or num == 1:
            return 1
        return num * factorial(num - 1)
    except TypeError:
        print('Only numbers are allowed !!!')

print(factorial(5))