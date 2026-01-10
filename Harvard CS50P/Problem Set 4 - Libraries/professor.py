# https://cs50.harvard.edu/python/2022/psets/4/professor/

import random
from random import randint

def main():
    level = get_level() # get integer level
    correct_count = 0 # correct count out of 10 problems

    for i in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        problem = f"{str(x)} + {str(y)} = "
        answer = x + y
        wrong_count = 0 # wrong count for current problem

        while wrong_count < 3: # give only 3 tries
            try:
                response = int(input(problem)) # will catch error if input is not a number

                if response == answer: # answer is right
                    correct_count += 1
                    break # breaks while loop and goes back to top of for loop to generate new problem
                else: # answer is wrong
                    print("EEE")
                    wrong_count += 1

            except Exception:
                print("EEE")
                wrong_count += 1
                pass # pass back to top of while loop and prompts user again

            if wrong_count == 3:
                print(f"{problem}{answer}") # only prints answer after 3 wrong answers

    print(f"Score: {correct_count}") # print user's score at the end

def get_level(): # getting input level
    while True:
        level = input("Level: ")
        try:
            level = int(level)
            if level in [1, 2, 3]: # level can only be 1, 2, 3
                return level
        except Exception: # raise value error
            pass


def generate_integer(level):
    lower = level-1
    upper = level
    return randint(0, 9) if level == 1 else randint(10**lower, 10**upper-1) # https://medium.com/@s10131416/little-professor-cs50p-week4-1266f4019d07


if __name__ == "__main__":
    main()
