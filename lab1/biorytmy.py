import datetime
import math

def calculate_day_of_life(birth_date: datetime.date, modifier: int = 0) -> int:
    result = (datetime.date.today() - birth_date).days + modifier
    if result < 0:
        raise ValueError("User was not born yet.")
    else: return result


def calculate_physwave(t: int) -> float:
    return math.sin( t * ((2 * math.pi) / 23) )


def calculate_emotwave(t: int) -> float:
    return math.sin( t * ((2 * math.pi) / 28) )


def calculate_intwave(t: int) -> float:
    return math.sin( t * ((2 * math.pi) / 33) )


def main() -> None:
    name = input("Enter your name: ")
    year = int(input("Your year of birth: "))
    month = int(input("Your month of birth: "))
    day = int(input("Your day of birth: "))

    birth_date = datetime.date(year, month, day)
    day_of_life = calculate_day_of_life(birth_date)

    physwave = calculate_physwave(day_of_life)
    emotwave = calculate_emotwave(day_of_life)
    intwave = calculate_intwave(day_of_life)

    additional_messages = []
    # positives
    if physwave > 0.5: additional_messages.append("Seems like you're full of energy today!")
    if emotwave > 0.5: additional_messages.append("Feeling good?")
    if intwave > 0.5: additional_messages.append("Quite a productive day, isn't it?")
    if len(additional_messages) == 3:
        additional_messages = []
        additional_messages.append("It seems like you're having a fantastic day today!")
    
    # negatives
    if physwave < -0.5: 
        additional_messages.append("We're all tired sometimes.")
        if calculate_physwave(calculate_day_of_life(birth_date, modifier=1)) > physwave:
            additional_messages[-1] += " It'll be better tomorrow."
    if emotwave < -0.5: 
        additional_messages.append("I hope you don't feel too down.")
        if calculate_emotwave(calculate_day_of_life(birth_date, modifier=1)) > emotwave:
            additional_messages[-1] += " I'm sure you'll feel better tomorrow."
    if intwave < -0.5: 
        additional_messages.append("Burnout hits everyone, don't blame yourself.")
        if calculate_intwave(calculate_day_of_life(birth_date, modifier=1)) > intwave:
            additional_messages[-1] += " Rest easy, the next day will be better."
    if physwave + emotwave + intwave < -1.5:
        additional_messages = []
        additional_messages.append("I understand it's a very tough time for you. Don't get discouraged, power through it. Good luck!")
    
    message = "\n".join(additional_messages)
    

    print(f"Hello, {name}!\n")
    print(f"Your biorhythms are:")
    print(f"Physical: {physwave}")
    print(f"Emotional: {emotwave}")
    print(f"Intellectual: {intwave}")
    print(f"\n{message}")



if __name__ == "__main__":
    main()

# start 14:45, koniec 15:21, czas: 37min.




# CHATGPT 3.5 REFACTOR OF THE PROGRAM


# import datetime
# import math

# PHYSICAL_PERIOD = 23
# EMOTIONAL_PERIOD = 28
# INTELLECTUAL_PERIOD = 33

# def calculate_day_of_life(birth_date: datetime.date, modifier: int = 0) -> int:
#     result = (datetime.date.today() - birth_date).days + modifier
#     if result < 0:
#         raise ValueError("Invalid birth date")
#     return result

# def calculate_wave(t: int, period: int) -> float:
#     return math.sin(t * ((2 * math.pi) / period))

# def main() -> None:
#     name = input("Enter your name: ")
#     year = int(input("Your year of birth: "))
#     month = int(input("Your month of birth: "))
#     day = int(input("Your day of birth: "))

#     birth_date = datetime.date(year, month, day)
#     day_of_life = calculate_day_of_life(birth_date)

#     physwave = calculate_wave(day_of_life, PHYSICAL_PERIOD)
#     emotwave = calculate_wave(day_of_life, EMOTIONAL_PERIOD)
#     intwave = calculate_wave(day_of_life, INTELLECTUAL_PERIOD)

#     additional_messages = []

#     # positives
#     positive_messages = [
#         ("Seems like you're full of energy today!", physwave),
#         ("Feeling good?", emotwave),
#         ("Quite a productive day, isn't it?", intwave)
#     ]
#     additional_messages.extend(message for message, wave_value in positive_messages if wave_value > 0.5)

#     # negatives
#     negative_messages = [
#         ("We're all tired sometimes. It'll be better tomorrow.", physwave),
#         ("I hope you don't feel too down. I'm sure you'll feel better tomorrow.", emotwave),
#         ("Burnout hits everyone, don't blame yourself. Rest easy, the next day will be better.", intwave)
#     ]
#     additional_messages.extend(message for message, wave_value in negative_messages if wave_value < -0.5)

#     if physwave + emotwave + intwave < -1.5:
#         additional_messages = ["I understand it's a very tough time for you. Don't get discouraged, power through it. Good luck!"]

#     message = "\n".join(additional_messages)

#     print(f"Hello, {name}!\n")
#     print("Your biorhythms are:")
#     print(f"Physical: {physwave}")
#     print(f"Emotional: {emotwave}")
#     print(f"Intellectual: {intwave}")
#     print(f"\n{message}")

# if __name__ == "__main__":
#     main()