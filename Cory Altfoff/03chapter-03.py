print("Witaj ponownie Krzysiu uwu\nThis programme's gonna divide 2 numbers\n")
while True:
    try:
        num1 = int(input("choose a first number:"))
        num2 = int(input("choose another number "))
        Q = num1 // num2
        R = num1 % num2
        print("Result is", Q, "with remainder of ", R, "\n")
    except(ZeroDivisionError):
        print("\nThe second number cannot be a zero")
    except(ValueError):
        print("\nyou must choose a integer number")
