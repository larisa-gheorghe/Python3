'''
@only_ints 
def add(x, y):
    return x + y
    
add(1, 2) # 3
add("1", "2") # "Please only invoke with integers."
'''

from functools import wraps

def only_ints(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        types_set = {type(arg) for arg in args}
        if int in types_set:
            return fn(*args, **kwargs)
        return "Please only invoke with integers."
    return wrapper
    



