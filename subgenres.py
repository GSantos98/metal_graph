# O codigo serve para criar uma lista com os subgeneros presentes na base de dados usado

import csv 
with open('genres.csv') as csvfile:
    genres = csv.reader(csvfile, delimiter=',')
    subgenres = []
    
    for row in genres:
        for i in range(5):
            subgenre = row[i]
            if ((subgenre not in subgenres) and (subgenre != '')):
                subgenres.append(subgenre)

    subgenres = sorted(subgenres)
    print(subgenres)
    print(len(subgenres))
