import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import confusion_matrix

df = pd.read_csv("iris.csv")
all_inputs = df[['sepal.length', 'sepal.width', 'petal.length', 'petal.width']].values
all_classes = df['species'].values

(train_inputs, test_inputs, train_classes, test_classes) = train_test_split(all_inputs, all_classes, train_size=0.7, random_state=286143)


knc3 = KNeighborsClassifier(n_neighbors=3)
knc5 = KNeighborsClassifier(n_neighbors=5)
knc11 = KNeighborsClassifier(n_neighbors=11)
bayes = GaussianNB()

knc3.fit(train_inputs, train_classes)
knc5.fit(train_inputs, train_classes)
knc11.fit(train_inputs, train_classes)
bayes.fit(train_inputs, train_classes)

print(f"KNN k=3: {round(knc3.score(test_inputs, test_classes)*100, 2)}%")
print(f"KNN k=5: {round(knc5.score(test_inputs, test_classes)*100, 2)}%")
print(f"KNN k=11: {round(knc11.score(test_inputs, test_classes)*100, 2)}%")
print(f"Gaussian Naive Bayes: {round(bayes.score(test_inputs, test_classes)*100, 2)}%")


# dla random_state = 286143 (mój numer indeksu):
# Decision Tree: 97.78%
# KNN k=3: 95.56%
# KNN k=5: 95.56%
# KNN k=11: 97.78%
# Gaussian Naive Bayes: 95.56%

# Dane niewystarczająco duże aby uzyskać wiarygodny werdykt na to, który z klasyfikatorów
# jest najlepszy dla danych. KNN z k = 11 oraz klasyfikator drzew decyzyjnych najlepiej
# sprawdza się dla wybranej próbki.

knc3_pred = knc3.predict(train_inputs)
print(confusion_matrix(train_classes, knc3_pred, labels=["setosa", "versicolor", "virginica"]))
knc5_pred = knc5.predict(train_inputs)
print(confusion_matrix(train_classes, knc5_pred, labels=["setosa", "versicolor", "virginica"]))
knc11_pred = knc11.predict(train_inputs)
print(confusion_matrix(train_classes, knc11_pred, labels=["setosa", "versicolor", "virginica"]))
bayes_pred = bayes.predict(train_inputs)
print(confusion_matrix(train_classes, bayes_pred, labels=["setosa", "versicolor", "virginica"]))