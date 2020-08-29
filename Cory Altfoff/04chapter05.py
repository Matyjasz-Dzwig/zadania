def Conv(string):
    return float(string)

while True:
    try:
        string = str(input("your string: "))
        print(Conv(string))
    except ValueError:
        print("You can only convert numbers")
