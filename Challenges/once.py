def once(fn):
    fn.is_called = False
    def inner(*args):
        if not(fn.is_called):
            fn.is_called = True
            return fn(*args)
    return inner