#start 15:27 koniec 15:44, czas: 17min

# PROMPT:
# Hi, could you write me a python program to calculate a user's biorhythms? They are as follows:
# - Physical Wave: sin( (2pi / 23) * t )
# - Emotional Wave: sin( (2pi / 28) * t )
# - Intellectual Wave: sin( (2pi / 33) * t )
# where t is the number of days from the user's birth.

# The program should ask the user for their name, and their year, month, and day of birth. 
#Then it should greet the user and display their biorhythms calculated with the formulae above.

# Additionally, the program should display messages to congratulate the user on each biorhythm over 0.5
# (which means the user is feeling well), and cheer the user up on each biorhythm below -0.5 
#(which means the user is not feeling good). When cheering the user up due to a low biorhythm, 
#the program should also calculate the same biorhythm for the next day, and if it's higher than today, 
#it should mention that the next day will be better.



# KOD POSIADAŁ BŁĘDY, OTO PROMPT KTÓRY JE NAPRAWIŁ:

# It seems like there is an error in the code you provided. 
#The values next_physical, next_emotional, and next_intellectual attempt to use the variable days_since_birth, 
#which is not defined in the scope of the function main(). 
#It is a variable that is defined within the scope of the function calculate_biorhythms.

#Additionally, the style could use a little bit of work. The next_physical, next_emotional, and next_intellectual 
#variables attempt to calculate tomorrow's biorhythms on the spot with the formula, 
#instead of using a dedicated function, for instance by refactoring the calculate_biorhythms() function defined above.

#Could you improve the code with the above guidelines in mind?

import math
import datetime

def calculate_biorhythms(year, month, day, offset=0):
    birth_date = datetime.date(year, month, day)
    today = datetime.date.today() + datetime.timedelta(days=offset)
    days_since_birth = (today - birth_date).days
    
    physical = math.sin(2 * math.pi / 23 * days_since_birth)
    emotional = math.sin(2 * math.pi / 28 * days_since_birth)
    intellectual = math.sin(2 * math.pi / 33 * days_since_birth)
    
    return physical, emotional, intellectual

def main():
    name = input("Please enter your name: ")
    year = int(input("Enter the year of your birth (YYYY): "))
    month = int(input("Enter the month of your birth (MM): "))
    day = int(input("Enter the day of your birth (DD): "))
    
    physical, emotional, intellectual = calculate_biorhythms(year, month, day)
    
    print(f"\nHello, {name}!")
    print("Here are your biorhythms:")
    print(f"Physical Wave: {physical:.2f}")
    print(f"Emotional Wave: {emotional:.2f}")
    print(f"Intellectual Wave: {intellectual:.2f}")
    
    if physical > 0.5:
        print("Congratulations! You are feeling physically well.")
    elif physical < -0.5:
        print("Cheer up! You are not feeling physically well.")
        next_physical = calculate_biorhythms(year, month, day, offset=1)[0]
        if next_physical > physical:
            print("Tomorrow will be better for you physically.")
    
    if emotional > 0.5:
        print("Congratulations! You are feeling emotionally well.")
    elif emotional < -0.5:
        print("Cheer up! You are not feeling emotionally well.")
        next_emotional = calculate_biorhythms(year, month, day, offset=1)[1]
        if next_emotional > emotional:
            print("Tomorrow will be better for you emotionally.")
    
    if intellectual > 0.5:
        print("Congratulations! You are feeling intellectually well.")
    elif intellectual < -0.5:
        print("Cheer up! You are not feeling intellectually well.")
        next_intellectual = calculate_biorhythms(year, month, day, offset=1)[2]
        if next_intellectual > intellectual:
            print("Tomorrow will be better for you intellectually.")

if __name__ == "__main__":
    main()