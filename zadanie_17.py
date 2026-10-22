wersja_1 = {'lr': 0.01, 'epochs': 100, 'optimizer': 'sgd', 'batch_size': 32, 'dropout': 0.2}
wersja_2 = {'lr': 0.001, 'epochs': 100, 'optimizer': 'adam', 'batch_size': 64, 'momentum': 0.9}
print('Wszystkie klucze:', set(wersja_1) | set(wersja_2))
print('Wspolne:', set(wersja_1) & set(wersja_2))
print('Tylko wersja 1:', set(wersja_1) - set(wersja_2))
print('Tylko wersja 2:', set(wersja_2) - set(wersja_1))
rozne_lr = wersja_1['lr'] != wersja_2['lr']
rozne_epochs = wersja_1['epochs'] != wersja_2['epochs']
rozne_optimizer = wersja_1['optimizer'] != wersja_2['optimizer']
rozne_batch_size = wersja_1['batch_size'] != wersja_2['batch_size']
print('Rozne lr:', rozne_lr, 'epochs:', rozne_epochs, 'optimizer:', rozne_optimizer, 'batch_size:', rozne_batch_size)
