# def interleave(string1, string2):
#     pairs = list(zip(string1, string2))
#     final_string = ''
#     for pair in pairs:
#         for letter in pair:
#             final_string += letter
#     return final_string

def interleave(string1, string2):
    """

    :param string1: str
    :param string2: str
    :return: str

    >>> interleave("bla","bla")
    'bbllaa'

    >>> interleave(1,2)
    Traceback (most recent call last):
        ...
    TypeError: 'int' object is not iterable
    """
    final_string = ''.join(''.join(pair) for pair in list(zip(string1, string2)))
    return final_string

print(interleave('hi', 'ha'))
print(interleave('aaa', 'zzz'))
print(interleave('lzr','iad'))
