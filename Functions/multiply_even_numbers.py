'''
multiply_even_numbers([2,3,4,5,6]) # 48
'''

def multiply_even_numbers(list_of_num):
    product = 1
    for num in list_of_num:
        if num % 2 == 0:
            product *= num
    return product