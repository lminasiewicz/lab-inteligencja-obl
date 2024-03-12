from math import e as E

dataset = [((23, 75, 176), True),
           ((25, 67, 180), True),
           ((28, 120, 175), False),
           ((22, 65, 165), True),
           ((46, 70, 187), True),
           ((50, 68, 180), False),
           ((48, 97, 178), False)]


def activation(x: float) -> float:
    return (1 + E**(-x))**(-1)


def forward_pass(age: int, weight: int, height: int) -> float:
    hidden1 = age*(-0.46122) + weight*(0.97314) + height*(-0.39203) + 0.80109
    hidden1_active = activation(hidden1)
    hidden2 = age*(0.78548) + weight*(2.10584) + height*(0.57847) + 0.43529
    hidden2_active = activation(hidden2)
    return hidden1_active * (-0.81546) + hidden2_active * (1.03775) + -0.2368


def true_or_false(x: float):
    if abs(x-1) > abs(x-0):
        return False
    return True


def main() -> None:
    correct = 0
    for person in dataset:
        predicted = true_or_false(forward_pass(person[0][0], person[0][1], person[0][2]))
        real = person[1]
        if predicted == real:
            correct += 1
        print(f"predicted: {predicted}, real: {real}")
    accuracy = round(correct / len(dataset), 3) * 100
    print(f"accuracy: {accuracy}%")


if __name__ == "__main__":
    main()