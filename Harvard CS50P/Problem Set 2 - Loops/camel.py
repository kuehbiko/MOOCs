#task:
#user input in camel case
#return output in snake case

#define variables
camel_case = input("CamelCase: ")
snake_case = []

#convert to snake case
for letter in camel_case:
    if letter.islower():
        snake_case.append(letter)
    else:
        new_letter = "_" + letter.lower()
        snake_case.append(new_letter)

print("snake_case: " + "".join(snake_case))
