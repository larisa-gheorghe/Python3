def letter_counter(s):
    letter_counter.val = s
    def inner(char):
        return len(list(c.lower() for c in letter_counter.val.lower() if c == char))
    return inner