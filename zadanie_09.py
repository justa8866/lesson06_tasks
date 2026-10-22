domyslne = {'lr': 0.01, 'epochs': 100, 'optimizer': 'sgd', 'batch_size': 32}
uzytkownika = {'lr': 0.001, 'batch_size': 64, 'momentum': 0.9}
finalna = domyslne | uzytkownika
finalna2 = domyslne.copy()
finalna2.update(uzytkownika)
print('Konfiguracje rowne:', finalna == finalna2)
print(f"lr: {finalna['lr']}\nbatch_size: {finalna['batch_size']}\nmomentum: {finalna['momentum']}")
