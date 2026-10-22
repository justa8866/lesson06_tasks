dataset_a = {'wiek', 'plec', 'miasto', 'dochod', 'wyksztalcenie', 'stan_cywilny'}
dataset_b = {'wiek', 'plec', 'miasto', 'pensja', 'stanowisko', 'staz'}
wspolne = dataset_a & dataset_b
print('Wspolne:', wspolne)
print('Tylko A:', dataset_a - dataset_b)
print('Tylko B:', dataset_b - dataset_a)
print('Suma:', dataset_a | dataset_b)
print('Symetryczna:', dataset_a ^ dataset_b)
print('Podzbior:', {'wiek', 'plec'}.issubset(wspolne))
