def factorial(num):
    if not isinstance(num, int) or isinstance(num, bool):  
            return "Only positive integers are allowed!"
    if num == 0 or num == 1:
            return 1
    try:        
        if num < 0:
          raise RecursionError('No Negative')
        return num * factorial(num - 1)
    except RecursionError as r:
        print(f"{r}")
        raise r
    except Exception as e:
        print(f'{e}')

print(factorial(5))
print(factorial("abc"))