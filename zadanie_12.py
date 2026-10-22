rekord = ('setosa', 5.1, 3.5, 1.4, 0.2)
gatunek, sl, sw, pl, pw = rekord
rekord_slownik = {'species': gatunek, 'sepal_length': sl, 'sepal_width': sw, 'petal_length': pl, 'petal_width': pw}
print(f"{'species':<13}: {rekord_slownik['species']}")
print(f"{'sepal_length':<13}: {rekord_slownik['sepal_length']:>5.1f}")
print(f"{'sepal_width':<13}: {rekord_slownik['sepal_width']:>5.1f}")
print(f"{'petal_length':<13}: {rekord_slownik['petal_length']:>5.1f}")
print(f"{'petal_width':<13}: {rekord_slownik['petal_width']:>5.1f}")
print('Suma cech:', sum(rekord[1:]))
