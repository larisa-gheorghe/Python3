'''
is_palindrome('testing') # False
is_palindrome('tacocat') # True
is_palindrome('hannah') # True
is_palindrome('robert') # False
is_palindrome('amanaplanacanalpanama') # True
'''

def is_palindrome(text):
    no_spaces = text.replace(" ", "").lower()
    return text == no_spaces[::-1]
    