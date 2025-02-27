def enforce_types(func):
    def wrapper(*args):
        for arg in args:
            if not isinstance(arg, int):
                raise TypeError("All arguments must be integers.")
        return func(*args)
    return wrapper


@enforce_types
def addition(a, b):
    return a + b

print(addition(2, 2))