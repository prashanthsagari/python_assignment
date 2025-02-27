def is_palindrome(val):
    return str(val) == str(val)[::-1]

# works for number and string
print(is_palindrome('madam'))
print(is_palindrome(121))
    