'''
triple_and_filter([1,2,3,4]) # [12]
triple_and_filter([6,8,10,12]) # [24,36]
'''

def triple_and_filter(my_list):
    return list(map(lambda num: num * 3,filter(lambda n: n % 4 == 0, my_list)))