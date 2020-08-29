'''Demonstruje liste'''

bands = ['Architetcs','Parkway Drive', 'The Amity Affliction', 'Northlane',
        'Bring me the Horizon', 'Suicide Silence', 'Miss May I',
        'Like Moths to Flames', 'Fit for a King', 'Bury Tomorrow', 'Phinehas',
        'Motionless in White', 'Polaris', 'Currents', 'Novelists',
        'Born of Osiris', 'Veil of Maya', ]
while True:
    num = int(input("Choose a number: "))
    print(bands[num-1])
