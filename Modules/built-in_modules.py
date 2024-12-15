import keyword

def contains_keyword(*args):
    boolean_list = [keyword.iskeyword(arg) for arg in args]
    return True in boolean_list
    
# def contains_keyword(*args):
#     for arg in args:
#         if keyword.iskeyword(arg):
#             return True
#     return False