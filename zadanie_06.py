wymiary = (1920, 1080)
szerokosc, wysokosc = wymiary
print(f'Rozdzielczosc: {szerokosc}x{wysokosc}')
samotny = (42,)
print(type(samotny))
# samotny[0] = 100  # TypeError: tuple object does not support item assignment
print(samotny + (100, 200))
