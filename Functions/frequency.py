'''
frequency([1,2,3,4,4,4], 4) # 3
frequency([True, False, True, True], False) # 1
'''

def frequency(my_list, search_term):
    return my_list.count(search_term)
    