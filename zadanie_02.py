konfig = {'lr': 0.01, 'epochs': 100, 'optimizer': 'adam'}
print(konfig.get('lr'))
print(konfig.get('momentum'))
print(konfig.get('momentum', 0.9))
print('batch_size' in konfig)
