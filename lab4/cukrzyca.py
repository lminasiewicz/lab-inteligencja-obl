import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import confusion_matrix

MAX_ITER = 500

df = pd.read_csv("diabetes 1.csv")
all_inputs = df[["pregnant-times","glucose-concentr","blood-pressure","skin-thickness",
                 "insulin","mass-index","pedigree-func","age"]].values
all_classes = df['class'].values

(train_inputs, test_inputs, train_classes, test_classes) = train_test_split(all_inputs, all_classes, train_size=0.7, random_state=286143)

mlp = MLPClassifier(hidden_layer_sizes=(6, 3), max_iter=MAX_ITER, activation='relu')
mlp.fit(train_inputs, train_classes)
print(f"Multi-Layer Perceptron Classifier: {round(mlp.score(test_inputs, test_classes)*100, 2)}%")

mlp_optimized = MLPClassifier(hidden_layer_sizes=(8, 4), max_iter=MAX_ITER, activation='tanh')
mlp_optimized.fit(train_inputs, train_classes)
print(f"Multi-Layer Perceptron Classifier 2: {round(mlp_optimized.score(test_inputs, test_classes)*100, 2)}%")

predictions1 = mlp.predict(train_inputs)
print(confusion_matrix(train_classes, predictions1, labels=["tested_positive", "tested_negative"]))

predictions2 = mlp_optimized.predict(train_inputs)
print(confusion_matrix(train_classes, predictions2, labels=["tested_positive", "tested_negative"]))

# e) Nie poradziła sobie lepiej. Zapewne sieć ma źle dopasowane parametry, w szczególności
# spodziewam się że MAX_ITER powinien być o wiele większy.

# f) Sądzę, że czy FP czy FN jest gorszym błędem zależy od problemu. W tym przypadku myślę,
# że FN, czyli nieumiejętność zdiagnozowania poważnej chorobym która silnie wpływa
# na dalsze życie człowieka, brzmi jak gorszy błąd.

# Przy większości parametrów, które próbowałem, więcej było błędów FP
