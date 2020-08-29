'''   pytanie o wartosci ze slownika
      demonstruje metody slownika      '''

dict = {'weight':68, 'height':175,'age':19,'eyes':'blue','dzwig':'otchlani'}
while True:

    word = str(input("choose a word: "))
    if word in dict:
        print(dict.get(word))
    else:
        print(word,"is not in dictionary :(" )
