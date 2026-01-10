# https://cs50.harvard.edu/python/2022/psets/4/emojize/

# input: In a file called emojize.py, implement a program that prompts the user for a str in English and then
# output: outputs the “emojized” version of that str, converting any codes (or aliases) therein to their corresponding emoji.

import emoji # https://github.com/carpedm20/emoji

text = input("Input: ")
print(f"Output: {emoji.emojize(text, language='alias')}")
