s = input('Input: ')
vowels = ['a', 'e', 'i', 'o', 'u']
s = [i for i in s if i.lower() not in vowels]
print(''.join(s))
