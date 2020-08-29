'''kazdemu elementowi z listy odpowiada inna lista'''

bands = {'Architects':['Gravedigger', "These colours don't run",
    'Alpha Omega',"Devil's Island","Gone with the wind"], 'Parkway Drive':
    ['Dark Days', 'Karma', 'Carrion', 'Horizons']}
while True:
    word = str(input("Choose a band: "))
    while not word in bands:
        print("There is not", word,"in the list")
        word = str(input("Choose a band: "))
        if word in bands:
            break


    num = int(input("Choose a song number: "))
    a = bands.get(word)
    print(a[num-1],"\n")
