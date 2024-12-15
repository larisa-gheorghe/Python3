from random import choice

def flip():
    """

    >>> flip() in ["Head", "Tail"]
    True

    """
    return choice(["Head", "Tail"])

print(flip())