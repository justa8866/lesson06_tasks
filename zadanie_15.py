wyniki = {'LogReg': {'acc': 0.9667, 'prec': 0.9673, 'rec': 0.9667, 'f1': 0.9667}, 'DecisionTree': {'acc': 0.9333, 'prec': 0.9342, 'rec': 0.9333, 'f1': 0.9332}, 'RandomForest': {'acc': 0.9600, 'prec': 0.9610, 'rec': 0.9600, 'f1': 0.9601}}

tabela = {
    'acc': {'LogReg': wyniki['LogReg']['acc'], 'DecisionTree': wyniki['DecisionTree']['acc'], 'RandomForest': wyniki['RandomForest']['acc']},
    'prec': {'LogReg': wyniki['LogReg']['prec'], 'DecisionTree': wyniki['DecisionTree']['prec'], 'RandomForest': wyniki['RandomForest']['prec']},
    'rec': {'LogReg': wyniki['LogReg']['rec'], 'DecisionTree': wyniki['DecisionTree']['rec'], 'RandomForest': wyniki['RandomForest']['rec']},
    'f1': {'LogReg': wyniki['LogReg']['f1'], 'DecisionTree': wyniki['DecisionTree']['f1'], 'RandomForest': wyniki['RandomForest']['f1']}
}
najlepszy_acc = max(tabela['acc'], key=tabela['acc'].get)
najlepszy_prec = max(tabela['prec'], key=tabela['prec'].get)
najlepszy_rec = max(tabela['rec'], key=tabela['rec'].get)
najlepszy_f1 = max(tabela['f1'], key=tabela['f1'].get)
print(f"acc: {najlepszy_acc} ({tabela['acc'][najlepszy_acc]:.4f})")
print(f"prec: {najlepszy_prec} ({tabela['prec'][najlepszy_prec]:.4f})")
print(f"rec: {najlepszy_rec} ({tabela['rec'][najlepszy_rec]:.4f})")
print(f"f1: {najlepszy_f1} ({tabela['f1'][najlepszy_f1]:.4f})")
print('Najlepsze modele:', {najlepszy_acc, najlepszy_prec, najlepszy_rec, najlepszy_f1})
