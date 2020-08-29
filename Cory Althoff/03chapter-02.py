print("Witaj ponownie Krzysiu uwu\n")
while True:
    num = int(input("Choose a number:"))
    if num < 10:
        print("number is smaller than 10")
    elif num == 10:
        print("your number is 10!")
    elif num > 10 and num < 25:
        print("your number is greater than 10, but smaller than 25")
    elif num == 25:
        print("your number is 25!")
    elif num > 25:
        print("your number is grater than 25! ")
