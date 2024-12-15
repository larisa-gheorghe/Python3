'''
def isEven(num):
    return num % 2 == 0

partition([1,2,3,4], isEven) # [[2,4],[1,3]]
'''

# def partition(my_list, isEven):
#     truthy_list = []
#     falsey_list = []
#     for item in my_list:
#         if isEven(item):
#             truthy_list.append(item)
#         else:
#             falsey_list.append(item)
#     return [truthy_list, falsey_list]

def partition(my_list, isEven):
    truthy_list = [item for item in my_list if isEven(item)]
    falsey_list = [item for item in my_list if not isEven(item)]
    return [truthy_list, falsey_list]
    
    
    
    
    
    