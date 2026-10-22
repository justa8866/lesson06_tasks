sprzedaz = {(2024, 'Q1'): 120_000, (2024, 'Q2'): 140_000, (2024, 'Q3'): 135_000, (2024, 'Q4'): 160_000}
print('2024 Q2:', sprzedaz[(2024, 'Q2')])
sprzedaz[(2025, 'Q1')] = 130_000
print('Max:', max(sprzedaz.values()), 'Min:', min(sprzedaz.values()), 'Suma:', sum(sprzedaz.values()), 'Liczba:', len(sprzedaz))
