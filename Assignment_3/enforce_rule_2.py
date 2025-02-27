
def enforce_types(*types):
    def decorator(func):
        def wrapper(*args):
            if len(args) != len(types):
                raise TypeError("Number of arguments must match the expected types.")
            
            for arg, expected_type in zip(args, types):
                print(arg, expected_type)  # print information
                if not isinstance(arg, expected_type):
                    raise TypeError(f"Expected {expected_type.__name__}, but got {type(arg).__name__}.")
            
            return func(*args)
        return wrapper
    return decorator

@enforce_types(str, int)
def display_details(name,age):
    return f"{name} is {age} years old"


print(display_details("Prashanth", 30))