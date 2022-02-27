from countries import *
import random
import keyboard
from countryinfo import CountryInfo
from colorama import Fore



names = []
score_round1 = []
score_round2 = []
score_round3 = []
score_round4 = []
used_countries = []

def game_results(number):
    zipped_lists = zip(score_round1, score_round2, score_round3, score_round4)
    total_score = [x + y + z for (x, y, z) in zipped_lists]
    result = {}
    for i,j in zip(names,total_score):
        result[i] = j
    print(result)
    

def number_of_players(names):
    """
    This function will give the user the option to select the amount of 
    players and their names
    """
    print("\n")
    print(Fore.YELLOW + "Welcome to CAPITAL TRIVIA!")
    print("********************************")
    print("\n")
    print("Did you actually learn something in school? :)")
    print("\n")
    print("Prove it by guessing as many capitals as you can!\n")
    players = input(Fore.LIGHTMAGENTA_EX + "How many players will be playing? (min 1 / max 9) ")
    print("\n")
    contador = 1
    for i in range(int(players)):
        name = input(f"What is your name player {contador}? \n")
        print("\n")
        names.append(name)
        contador += 1

    name_list = names
    return name_list
"""    
def check_country():
    while (validate): 
        count_test = random.choice(list(countries))
        country = count_test
        used_countries.append(country)
        if country in used_countries:
            validate = False
        else:
            validate = True   

def validating_input():    
   while True:
    try:
        players == (2,9)
        print(f'Number is {x}')
    except ValueError:
        print('Not a valid number. Please chose a number between 2 and 9')
"""            
def questions(number, rounds_attempts):
    """
    This function will chose from a list of countries a random country
    """
    positive_feedback = random.choice(list(random_good_phrases))
    negative_feedback = random.choice(list(random_bad_phrases))
    for n in number:
        score = 0
        print(Fore.YELLOW + f"It's your turn {n}  \n")
        #Validate question
        #Colors for answer
        continues = True
        while (continues):
            validate = True
            country = ""
            while (validate): 
                count_test = random.choice(list(countries))
                country = count_test
                used_countries.append(country)
                if country in used_countries:
                    validate = False
                else:
                    validate = True   
            print(Fore.LIGHTMAGENTA_EX + f"What is the capital of {country}\n")
            answer = input('Write your answer: \n')
            print("\n")
            capital = CountryInfo(country).capital()
            if answer == capital:
                continues = True
                print(Fore.GREEN + f'CORRECT!  {positive_feedback}\n')
                
                score += 1
                if rounds_attempts == 1:
                    score_round1.append(int(score))
                elif rounds_attempts == 2:
                    score_round2.append(int(score))
                elif rounds_attempts == 3:
                    score_round3.append(int(score))    
                if score == 1:
                    print(f"Your currently have {score} point {n}")
                    print("************************************\n")
                    print("\n")
                else:
                    print(f"Your currently have {score} points {n}")
                    print("******************************************\n")
            else:
                continues = False
                print(Fore.RED + f'INCORRECT! {negative_feedback} The correct answer is {capital}')
                print("************************************************************************************\n")
                

            
def newgame(number):
    """
    This function will ask the user if it wants to start a new game 
    or if it wants to exit the app
    """
    new_game_question = input("Play Again? (Y/N)")
    if new_game_question  == 'Y':
        number_of_players(names)
        count_questions = 1
        for q in range(3):
            questions(number, count_questions)
            count_questions += 1
    elif new_game_question == 'N':   
        print("Have a great day! See you next time!")

def main():
    """
    This function runs the game
    """
    number = number_of_players(names)
    count_questions = 1
    for q in range(3):
        questions(number, count_questions)
        count_questions += 1
    game_results(number)
    newgame(number)
#
    
main()


