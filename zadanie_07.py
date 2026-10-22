pracownik = ('Julia', 'Wiśniewska', 28, 'Data Analyst', 8500.0)
imie, nazwisko, wiek, stanowisko, pensja = pracownik
print(f'{imie} {nazwisko} ({wiek}) – {stanowisko}, pensja: {pensja:.2f} zł')
imie, *reszta = pracownik
print(imie, reszta)
