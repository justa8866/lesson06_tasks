jezyki = ['Python', 'R', 'SQL', 'Python', 'Julia', 'R', 'Python', 'Scala', 'SQL']
unikalne = set(jezyki)
print('Poczatkowa liczba:', len(unikalne))
unikalne.update(['Go', 'Rust'])
print('Python:', 'Python' in unikalne, 'Fortran:', 'Fortran' in unikalne, 'Julia:', 'Julia' in unikalne)
unikalne.discard('Scala')
print('Finalny zbior:', unikalne, 'liczba:', len(unikalne))
