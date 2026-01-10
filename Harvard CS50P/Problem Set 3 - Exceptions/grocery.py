# https://cs50.harvard.edu/python/2022/psets/3/grocery/

# input: prompts user to enter item to add to grocery list until user inputs ctrl+d
# output: grocery list in uppercase, sorted alphabetically, prefixing each line with the number of times the user inputted that item

# define global variables
grocery_list = {}

# adding items to grocery list
while True:
    try:
        item = input().upper()
        if item in grocery_list:
            grocery_list[item] += 1
        else:
            grocery_list[item] = 1
    except EOFError:
        break

# sorting grocery list alphabetically
grocery_list_sorted = {i: grocery_list[i] for i in sorted(list(grocery_list.keys()))}

# output grocery list
for item in grocery_list_sorted:
    print(f"{grocery_list_sorted[item]} {item}")
