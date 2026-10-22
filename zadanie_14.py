dane = [('setosa', 5.1, 3.5, 1.4, 0.2), ('setosa', 4.9, 3.0, 1.4, 0.2), ('versicolor', 7.0, 3.2, 4.7, 1.4), ('versicolor', 6.4, 3.2, 4.5, 1.5), ('virginica', 6.3, 3.3, 6.0, 2.5), ('virginica', 5.8, 2.7, 5.1, 1.9), ('setosa', 4.7, 3.2, 1.3, 0.2)]
gatunki = {dane[0][0], dane[1][0], dane[2][0], dane[3][0], dane[4][0], dane[5][0], dane[6][0]}
print('Gatunki:', gatunki, 'liczba:', len(gatunki))
pierwszy_rekord = dane[0]
gatunek, sl, sw, pl, pw = pierwszy_rekord
print('Pierwszy rekord:', gatunek, sl, sw, pl, pw)
sepal_length = [dane[0][1], dane[1][1], dane[2][1], dane[3][1], dane[4][1], dane[5][1], dane[6][1]]
print('Min:', min(sepal_length), 'Max:', max(sepal_length), 'Suma:', sum(sepal_length), f'Srednia: {sum(sepal_length) / len(sepal_length):.3f}')
