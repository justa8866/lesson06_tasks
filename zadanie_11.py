raport = {'Q1': {'przychod': 120_000, 'koszt': 80_000}, 'Q2': {'przychod': 145_000, 'koszt': 92_000}, 'Q3': {'przychod': 138_000, 'koszt': 88_000}, 'Q4': {'przychod': 167_000, 'koszt': 101_000}}
print('Przychody:', raport['Q1']['przychod'], raport['Q2']['przychod'], raport['Q3']['przychod'], raport['Q4']['przychod'], sep='\n')
raport['Q1']['zysk'] = raport['Q1']['przychod'] - raport['Q1']['koszt']
raport['Q2']['zysk'] = raport['Q2']['przychod'] - raport['Q2']['koszt']
raport['Q3']['zysk'] = raport['Q3']['przychod'] - raport['Q3']['koszt']
raport['Q4']['zysk'] = raport['Q4']['przychod'] - raport['Q4']['koszt']
print(f"{'Q1':^6} | {raport['Q1']['przychod']:>8} | {raport['Q1']['koszt']:>8} | {raport['Q1']['zysk']:>8}")
print(f"{'Q2':^6} | {raport['Q2']['przychod']:>8} | {raport['Q2']['koszt']:>8} | {raport['Q2']['zysk']:>8}")
print(f"{'Q3':^6} | {raport['Q3']['przychod']:>8} | {raport['Q3']['koszt']:>8} | {raport['Q3']['zysk']:>8}")
print(f"{'Q4':^6} | {raport['Q4']['przychod']:>8} | {raport['Q4']['koszt']:>8} | {raport['Q4']['zysk']:>8}")
zyski = [raport['Q1']['zysk'], raport['Q2']['zysk'], raport['Q3']['zysk'], raport['Q4']['zysk']]
print('Suma:', sum(zyski), 'Min:', min(zyski), 'Max:', max(zyski), 'Srednia:', sum(zyski) / len(zyski))
