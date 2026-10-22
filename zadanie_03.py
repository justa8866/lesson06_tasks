metryki = {'accuracy': 0.94, 'precision': 0.91, 'recall': 0.89, 'f1_score': 0.90}
print('Maksimum:', max(metryki.values()), 'Minimum:', min(metryki.values()))
print(f"Srednia: {sum(metryki.values()) / len(metryki):.3f}")
print(sorted(metryki))
print(sorted(metryki.values()))
