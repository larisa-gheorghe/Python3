inventory = {'croissant': 19, 'bagel': 4, 'muffin': 8, 'cake': 1}

# Make a copy of inventory and save it to a variable called stock_list USE A DICTIONARY METHOD
stock_list = inventory.copy()


# add the value 18 to stock_list under the key "cookie"
stock_list['cookie'] = 18


# remove 'cake' from stock_list USE A DICTIONARY METHOD
stock_list.pop('cake')