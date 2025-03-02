def is_palindrome(val):
    """
    Check palindrome

    >>> is_palindrome('madam')
    True
    >>> is_palindrome(121)
    True
    >>> is_palindrome(12341)
    False
    >>> is_palindrome('2432dfd3')
    False
    """
    return str(val) == str(val)[::-1]

# works for number and string
print(is_palindrome('madam'))
print(is_palindrome(121))


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
    