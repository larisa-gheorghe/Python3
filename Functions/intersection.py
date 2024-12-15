# def intersection(list1, list2):
#     list1 = set(list1)
#     list2 = set(list2)
#     return list(list1 & list2)

def intersection(list1, list2):
    return [val for val in set(list1) & set(list2)]