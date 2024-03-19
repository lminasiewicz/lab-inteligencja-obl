import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier

MAX_ITER = 4000

df = pd.read_csv("../lab3/iris.csv")
all_inputs = df[['sepal.length', 'sepal.width', 'petal.length', 'petal.width']].values
all_classes = df['species'].values

(train_inputs, test_inputs, train_classes, test_classes) = train_test_split(all_inputs, all_classes, train_size=0.7, random_state=286143)

mlp1_2 = MLPClassifier(hidden_layer_sizes=(2), max_iter=MAX_ITER, activation='tanh')
mlp1_3 = MLPClassifier(hidden_layer_sizes=(3), max_iter=MAX_ITER, activation='tanh')
mlp2_3 = MLPClassifier(hidden_layer_sizes=(3, 3), max_iter=MAX_ITER, activation='tanh')

mlp1_2.fit(train_inputs, train_classes)
mlp1_3.fit(train_inputs, train_classes)
mlp2_3.fit(train_inputs, train_classes)

print(f"1 Hidden Layer, 2 Neurons: {round(mlp1_2.score(test_inputs, test_classes)*100, 2)}%")
print(f"1 Hidden Layer, 3 Neurons: {round(mlp1_3.score(test_inputs, test_classes)*100, 2)}%")
print(f"2 Hidden Layers, 3 Neurons Each: {round(mlp2_3.score(test_inputs, test_classes)*100, 2)}%")

# Nie wiem który jest najlepszy. Zależy od próby, oraz MAX_ITER.