sprzedaz = {(2024, 'Q1'): 120_000, (2024, 'Q2'): 145_000, (2024, 'Q3'): 138_000, (2024, 'Q4'): 167_000, (2025, 'Q1'): 130_000, (2025, 'Q2'): 155_000, (2025, 'Q3'): 149_000}
print('Suma:', sum(sprzedaz.values()))
print('Max:', max(sprzedaz.values()), 'Min:', min(sprzedaz.values()))
klucz_max = max(sprzedaz, key=sprzedaz.get)
rok_max, kw_max = klucz_max
print(f'Najwyzsza sprzedaz: {rok_max} {kw_max} – {sprzedaz[klucz_max]}')
ranking = sorted(sprzedaz, key=sprzedaz.get, reverse=True)
print('Trzy najwyzsze klucze:', ranking[0], ranking[1], ranking[2])
lata = {2024, 2025}
print('Unikalne lata:', lata)
