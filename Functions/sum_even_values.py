'''
sum_even_values(1,2,3,4,5,6) # 12
sum_even_values(4,2,1,10) # 16
sum_even_values(1) # 0
'''

# define sum_even_values
# def sum_even_values(*args):
#     even_values = [num for num in args if num % 2 == 0]
#     sum = 0
#     for val in even_values:
#         sum += val
#     return sum
    
def sum_even_values(*args):
    return sum(num for num in args if num % 2 == 0)
    