'''
list_manipulation([1,2,3], "remove", "end") # 3
list_manipulation([1,2,3], "remove", "beginning") #  1
list_manipulation([1,2,3], "add", "beginning", 20) #  [20,1,2,3]
list_manipulation([1,2,3], "add", "end", 30) #  [1,2,3,30]
'''

def list_manipulation(my_list, command, location, value=None):
    if command == "remove" and location == "end":
        return my_list.pop()
    elif command == "remove" and location == "beginning":
        return my_list.pop(0)
    elif command == "add" and location == "beginning":
        my_list.insert(0, value)
        return my_list
    else:
        my_list.append(value)
        return my_list