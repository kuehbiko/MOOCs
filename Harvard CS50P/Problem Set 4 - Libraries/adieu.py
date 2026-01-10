# https://cs50.harvard.edu/python/2022/psets/4/adieu/

# import libraries
import inflect

# define global variables
name_list = []
p = inflect.engine()

# infinite input loop
while True: # loop forever
    try:
        name = input("Name: ").title()
        name_list.append(name)

    except EOFError: # breaks loop when user enters ctrl+d
        break

name_list_joined = p.join(name_list) #using inflect to join list
print()
print(f"Adieu, adieu, to {name_list_joined}")
