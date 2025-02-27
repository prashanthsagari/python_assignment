def is_prime(num):
    try:
        if num < 2:
            return False
        for i in range(2, num):
            if num % i == 0:
                return False
        return True
    except TypeError:
        print('Only numbers are allowed !!!')

print(is_prime(7))
