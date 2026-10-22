grupa_a = {'python', 'pandas', 'numpy', 'sql', 'tableau'}
grupa_b = {'python', 'r', 'sql', 'ggplot2', 'dplyr'}
print('Suma:', grupa_a | grupa_b, grupa_a.union(grupa_b))
print('Iloczyn:', grupa_a & grupa_b, grupa_a.intersection(grupa_b))
print('Roznica A-B:', grupa_a - grupa_b, grupa_a.difference(grupa_b))
print('Roznica symetryczna:', grupa_a ^ grupa_b, grupa_a.symmetric_difference(grupa_b))
print('Rozlaczne:', grupa_a.isdisjoint(grupa_b))
