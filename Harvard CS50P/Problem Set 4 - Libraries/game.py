# https://cs50.harvard.edu/python/2022/psets/4/game/

# import libraries
import random

while True:
    try:
        level = int(input("Level: "))
        x = random.randint(1, level)
        while True:
            guess = int(input("Guess: "))
            if guess > x:
                print("Too large!")
            elif guess < x:
                print("Too small!")
            elif guess == x:
                print("Just right!")
                raise EOFError
    except ValueError:
        pass
    except EOFError:
        break
