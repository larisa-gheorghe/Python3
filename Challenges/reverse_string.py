def reverse_string(str):
    s = ''
    for i, char in enumerate(str[::-1]):
        s += char
    return s