def sum_squares(a,b):
    """
    Returns the sum of the squares of two numbers.

    >>> sum_squares(3, 4)
    25
    >>> sum_squares(0, 5)
    25
    >>> sum_squares(-3, 4)
    25
    >>> sum_squares("a", 3)  # Invalid input
    'Only positive integers are allowed!'
    >>> sum_squares(True, 3)  # Invalid input (True is treated as 1)
    'Only positive integers are allowed!'
    >>> sum_squares(2.5, 3.5)  # Invalid input
    'Only positive integers are allowed!'
    """
    if not (isinstance(a, int) and not isinstance(a, bool) and isinstance(b, int) and not isinstance(b, bool)):
        return "Only positive integers are allowed!"
    return a**2 + b**2

print(sum_squares(2,3))

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)