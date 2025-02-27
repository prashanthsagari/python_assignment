def custom_decorator(original_function):
    def wrap_function():
        print('Start Decorator')
        original_function()
        print('End Decorator')
    return wrap_function

@custom_decorator    
def func():
    print('Normal function')

func()
