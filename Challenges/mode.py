def mode(collection):
    count = {val: collection.count(val) for val in collection}
    # find the highest value
    max_value = max(count.values())
    # see at which index the highest value is at
    correct_index = list(count.values()).index(max_value)
    # return the correct key for the correct index
    return list(count.keys())[correct_index]