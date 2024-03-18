import numpy as np
import pandas as pd
import math

def numerize(data: pd.DataFrame) -> pd.DataFrame:
    df = data.copy(deep=True)
    for val in df.values[0]:
        if type(val) == "str":
            if val.isnumeric():
                val = float(val)
    for val in df.values[1]:
        if type(val) == "str":
            if val.isnumeric():
                val = float(val)
    return df


def check_correctness(arr: np.ndarray) -> bool:
    if len(arr) != 5: return False
    petal_array = [arr[0], arr[1], arr[2], arr[3]]
    species = arr[4]
    try:
        for measurement in petal_array:
            measurement = float(measurement)
    except:
        return False
    for measurement in petal_array:
        if math.isnan(float(measurement)): return False
    if species not in {"Setosa", "Versicolor", "Virginica"}:
        return False
    return True


def check_feasibility(arr: np.ndarray) -> bool:
    petal_array = [arr[0], arr[1], arr[2], arr[3]]

    for petal in petal_array:
        try:
            petal = float(petal)
        except:
            return False
        if float(petal) < 0 or float(petal) > 15:
            return False
    return True


def mean(arr: list[float]) -> float:
    sum = 0
    for elem in arr:
        sum += elem
    return sum / len(arr)


def calculate_avg_from_data(data: pd.DataFrame) -> list:
    df = data.transpose().values
    def get_values(df, index):
        return [elem for elem in df[index] if isinstance(elem, float) and not math.isnan(elem)]
    return [mean(get_values(df, 0)), mean(get_values(df, 1)), mean(get_values(df, 2)), mean(get_values(df, 3))]


def correct_unfeasible_data(data: pd.DataFrame) -> pd.DataFrame:
    df = numerize(data)
    avgs = calculate_avg_from_data(df)
    for iris in df.values:
        for i in range(len(iris)):
            if isinstance(iris[i], float) and not math.isnan(iris[i]):
                if iris[i] < 0 or iris[i] > 15:
                    iris[i] = avgs[i]
    return df



df = pd.read_csv("./iris_with_errors.csv")

correct_data = [iris for iris in df.values if check_correctness(iris) and check_feasibility(iris)]
outliers = [iris for iris in df.values if check_correctness(iris) and not check_feasibility(iris)]
incorrect_data = [iris for iris in df.values if not check_correctness(iris)]
print(f"Correct datapoints: {len(correct_data)}\nIncorrect datapoints: {len(incorrect_data)}")

corrected = correct_unfeasible_data(df)
c_outliers = [iris for iris in corrected.values if check_correctness(iris) and not check_feasibility(iris)]
print(c_outliers)

print(numerize(df))