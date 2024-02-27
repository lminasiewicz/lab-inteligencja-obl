import math
from random import randint
import matplotlib.pyplot as plt

MARGIN_OF_ERROR = 5
INITIAL_VELOCITY = 50
HEIGHT = 100
g = 9.81

def calculate_shot_distance(v0: int, h: int, a: float) -> float:
    a = math.radians(a)
    return v0 * math.cos(a) * ((v0 * math.sin(a) + math.sqrt( (v0 * math.sin(a))**2 + 2 * g * h )) / g)


def was_target_hit(target_distance: int, shot_distance: float) -> bool:
    if abs(target_distance - shot_distance) <= MARGIN_OF_ERROR:
        return True
    else: return False


def plot_trajectory(a, point):
    v0 = INITIAL_VELOCITY
    h = HEIGHT

    def f(x):
        a = math.radians(a)
        return (-g / ( 2 * v0 ** 2 * math.cos(a ** 2))) * x ** 2 + ( math.sin(a) / math.cos(a) ) * x + h
    
    x_values = range(0, 350, 5)
    y_values = [f(x) for x in x_values]

    plt.plot(x_values, y_values, color='blue')
    plt.scatter(point, 0, color='red', label='Target')
    plt.title('Function Plot')
    plt.xlabel('X')
    plt.ylabel('Function Line')
    plt.grid(True)

    plt.show()


def main() -> None:
    distance = randint(50, 340)
    target_hit = False
    attempts = 0
    while not target_hit:
        angle = float(input("Enter the angle of your shot: "))
        shot_distance = calculate_shot_distance(INITIAL_VELOCITY, HEIGHT, angle)
        target_hit = was_target_hit(distance, shot_distance)
        attempts += 1
        if target_hit: 
            print(f"Cel trafiony! \n Liczba prób: {attempts}")
            plot_trajectory(angle, distance)
        else: print("Chybienie!")





if __name__ == "__main__":
    main()