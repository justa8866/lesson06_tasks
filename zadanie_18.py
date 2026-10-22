projekt = {'nazwa': 'iris_classification', 'wersja': (1, 2, 0), 'autorzy': {'Anna', 'Bartek', 'Cezary'}, 'dataset': {'nazwa': 'Iris', 'shape': (150, 4), 'klasy': ('setosa', 'versicolor', 'virginica')}, 'hiperparametry': {'lr': 0.001, 'batch_size': 64, 'epochs': 50}}
major, minor, patch = projekt['wersja']
print(f'v{major}.{minor}.{patch}')
n_rekordow, n_cech = projekt['dataset']['shape']
print(f"Dataset {projekt['dataset']['nazwa']}: {n_rekordow} × {n_cech}")
projekt['autorzy'].add('Dorota')
print('Liczba autorow:', len(projekt['autorzy']), 'autorzy:', sorted(projekt['autorzy']))
projekt['hiperparametry'].update({'dropout': 0.3, 'batch_size': 128})
print('Hiperparametry:', projekt['hiperparametry'])
projekt['dataset']['klasy'] = set(projekt['dataset']['klasy'])
print('Czy setosa jest w klasach:', 'setosa' in projekt['dataset']['klasy'])
