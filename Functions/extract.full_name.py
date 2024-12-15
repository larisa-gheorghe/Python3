'''
names = [{'first': 'Elie', 'last': 'Schoppik'}, {'first': 'Colt', 'last': 'Steele'}]
extract_full_name(names) # ['Elie Schoppik', 'Colt Steele']
'''

# def extract_full_name(my_list):
#     return [' '.join(pair.values()) for pair in my_list]

def extract_full_name(my_list):
    return list(map(lambda name: f'{name["first"]} {name["last"]}', my_list))