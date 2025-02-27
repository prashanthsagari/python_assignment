import time
def timer(func):
    def wrapper(*args):
        start = time.time()  # Start time
        result = func(*args)  # Call the function
        end = time.time()  # End time
        print(f"Execution time: {end - start:.6f} seconds")
        return result  # Return the original function's result
    return wrapper

@timer
def sum_of_squares(n):
    return sum(i ** 2 for i in range(1, n + 1))

print(sum_of_squares(1000))