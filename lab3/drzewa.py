import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import tree
from sklearn.metrics import confusion_matrix

# a)
df = pd.read_csv("iris.csv")
all_inputs = df[['sepal.length', 'sepal.width', 'petal.length', 'petal.width']].values
all_classes = df['species'].values

(train_inputs, test_inputs, train_classes, test_classes) = train_test_split(all_inputs, all_classes, train_size=0.7, random_state=286143)

# b)
dtc = tree.DecisionTreeClassifier()

# c)
dtc.fit(train_inputs, train_classes)

# d) nie wiem dlaczego nie działa
tree.plot_tree(dtc)

# e)
print(f"Decision Tree: {round(dtc.score(test_inputs, test_classes)*100, 2)}%")

# f)
predictions = dtc.predict(train_inputs)
print(confusion_matrix(train_classes, predictions, labels=["setosa", "versicolor", "virginica"]))