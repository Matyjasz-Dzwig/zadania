numbers = str([2137,69,666,32])

while True:
    guess = input("Try to guess: ")
    if guess == 'q':
        break
    if guess in numbers:
        print("you guessed")
    else:
        print(guess, "is not in list")
