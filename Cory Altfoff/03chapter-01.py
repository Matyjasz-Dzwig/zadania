print("Witaj Krzysiu")
print("I'm doing some exercices to practice my Python knowledge")
print("I hope I will improve as a programmer \n")
while True:
    a = int(input("Choose a number: "))
    print("your number is", a)
    if a % 2 == 0:
        print("your number is even")
    elif a %2 !=0:
        print("your number is odd")
    if a < 10:
        print("you number is smaller than 10")
    elif a > 10:
        print("your number is greater than 10")
    print("")
