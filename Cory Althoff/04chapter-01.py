print("Witaj Krzysiu. This programme will tell you the square of a number")

def sqr(num):
    return num * num

while True:
    try:
        num1 = int(input("your number: "))
        print(sqr(num1))
    except ValueError:
        print("choose a integer number")
