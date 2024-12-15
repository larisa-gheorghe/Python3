'''
last_element([1,2,3]) # 3
last_element([]) # None
'''

def last_element(bla=[]):
    if bla:
        return bla[-1]
    return None
    