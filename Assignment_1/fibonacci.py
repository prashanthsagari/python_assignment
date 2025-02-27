def fibonacci(n):
    try:
        a = 0
        b = 1
        for _ in range(n):
            print(a, end=" ")
            a, b = b, a + b
    except TypeError:
        print('Only numbers are allowed !!!')


fibonacci(5)  