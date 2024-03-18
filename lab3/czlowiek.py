import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

df = pd.read_csv("iris.csv")
(train_set, test_set) = train_test_split(df.values, train_size=0.7, random_state=286143)

def classify_iris_old(iris: np.ndarray) -> str:
    sl = iris[0]
    pl = iris[2]
    if sl > 4: 
        return "Setosa"
    elif pl <= 5:
        return "Virginica"
    else:
        return "Versicolor"


def classify_iris(iris: np.ndarray) -> str:
    pl = iris[2]
    avg_setosa = np.average([iris[2] for iris in train_set if iris[4].lower() == "setosa"])
    avg_virginica = np.average([iris[2] for iris in train_set if iris[4].lower() == "virginica"])
    avg_versicolor = np.average([iris[2] for iris in train_set if iris[4].lower() == "versicolor"])
    distances = [abs(pl - avg_setosa), abs(pl - avg_virginica), abs(pl - avg_versicolor)]
    if min(distances) == distances[0]:
        return "Setosa"
    elif min(distances) == distances[1]:
        return "Virginica"
    else:
        return "Versicolor"



good_predictions = 0
length = test_set.shape[0]

for i in range(length):
    if classify_iris(test_set[i]).lower() == test_set[i][4].lower():
        good_predictions += 1

print(length, good_predictions)
print(round(good_predictions / length * 100, 2), "%", sep="")