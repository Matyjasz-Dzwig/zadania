'''kazdemu elementowi z listy odpowiada inna lista'''

bands = {'Architects':['Gravedigger', "These colours don't run",
    'Alpha Omega',"Devil's Island","Gone with the wind"], 'Parkway Drive':
    ['Dark Days', 'Karma', 'Carrion', 'Horizons']}
while True:
    word = str(input("Choose a band: "))
    a = bands.get(word)
    print(a)
