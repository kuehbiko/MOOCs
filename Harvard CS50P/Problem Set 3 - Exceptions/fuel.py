# https://cs50.harvard.edu/python/2022/psets/3/fuel/

def main():
    x = fraction("Fraction: ")
    if x >= 0.99:
        print('F')
    elif x <= 0.01:
        print('E')
    else:
        print(f"{round(x*100)}%")

def fraction(prompt):
    while True:
        try:
            y = input(prompt)
            i,j = y.split('/')
            if int(i) / int(j) <= 1:
                return int(i) / int(j)
        except (ValueError, ZeroDivisionError):
            pass


main()
