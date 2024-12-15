def calculate(**kwargs):
    """

    :param kwargs:
    :return:
    """
    result = 0
    if kwargs.get("operation"):
        if kwargs.get("operation") == "add":
            result = kwargs.get("first") + kwargs.get("second")
        if kwargs.get("operation") == "subtract":
            result = kwargs.get("first") - kwargs.get("second")
        if kwargs.get("operation") == "multiply":
            result = kwargs.get("first") * kwargs.get("second")
        if kwargs.get("operation") == "divide":
            result = kwargs.get("first") / kwargs.get("second")
    if kwargs.get("make_float"):
        result = float(result)
    else:
        result = int(result)
    if kwargs.get("message"):
        return f'{kwargs.get("message")} {result}'
    return f"The result is {result}"


print(calculate(make_float=False, operation='add', message='You just added', first=2, second=4)) # "You just added 6"
print(calculate(make_float=True, operation='divide', first=3.5, second=5)) # "The result is 0.7"