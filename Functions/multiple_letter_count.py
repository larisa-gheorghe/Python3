'''
multiple_letter_count("awesome") # {'a': 1, 'e': 2, 'm': 1, 'o': 1, 's': 1, 'w': 1}
'''

def multiple_letter_count(text):
    return {char:text.count(char) for char in text}
    