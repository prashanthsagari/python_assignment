import math
import NegativeNumberError as ne

def square_root(n):
    if not isinstance(n, (int, float)):
        raise TypeError("Only numbers are allowed!")
    if n < 0:
        raise ne.NegativeNumberError()
    # print(n ** 0.5) or math.sqrt(n)
    return math.sqrt(n)

print(square_root(4))
