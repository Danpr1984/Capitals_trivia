from countries import *
import random
import keyboard
from countryinfo import CountryInfo
from colorama import Fore

names = []
score_round1 = []
score_round2 = []
score_round3 = []
used_countries = []

def game_results():
    """
    This app will grab the scores of each round for each player and will 
    return the total scores with the outcome of the game
    
    
    print(score_round1)
    print(score_round2)
    print(score_round3)
    total_score = []
    for i in range(len(names)):
        score = score_round1[i] + score_round2[i] + score_round3[i]
        name = names[i]
        print(name + " scored " + str(score))
    """    
    zipped_lists = zip(score_round1, score_round2, score_round3)
    total_score = [x + y + z for (x, y, z) in zipped_lists]
    result = {}
    for i,j in zip(names,total_score):
        result[i] = j
    print(result)    
    #run a winner player with whoever got more points or ask for rematch in case there is a tie. 
    

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
    play = "n"
    while play == "n":   
        try:
            players = input(Fore.LIGHTMAGENTA_EX + "How many players will be playing? (min 1 / max 4)\n")
            if (players != "1") and (players != "2") and (players != "3") and (players != "4"):
                raise Exception()
            else:    
                players_count = 1
                for i in range(int(players)):
                    name = input(f"What is your name player {players_count}? \n")
                    print("\n")
                    names.append(name)
                    players_count += 1
                name_list = names
                play = "y"
                return name_list
        except Exception:
            print("You have to pick a number between 1-4\n")
            play = "n"
    
"""
def players_list(number):
    for i in range(int(players)):
        name = input(f"What is your name player {contador}? \n")
        print("\n")
        names.append(name)
        contador += 1
    name_list = names
    return name_list
"""    
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
    print("Let's get ready to RUMBLE!")
    print("*****************************\n")
    global score_round1
    global score_round2
    global score_round3
    positive_feedback = random.choice(list(random_good_phrases))
    negative_feedback = random.choice(list(random_bad_phrases))
    for n in number:
        score = 0
        print(Fore.YELLOW + f"It's your turn {n}  \n")
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
            print(Fore.LIGHTMAGENTA_EX + f"What is the capital of {country}?\n")
            answer = input('Write your answer: \n')
            answer = answer.lower()
            print("\n")
            capital = CountryInfo(country).capital()
            if answer == capital.lower():
                continues = True
                print(Fore.GREEN + f'CORRECT!  {positive_feedback}\n')
                score += 1
               
            else:
                continues = False
                print(Fore.RED + f'INCORRECT! {negative_feedback} The correct answer is {capital}')
                print("*****************************************************************\n")
                score += 0
                if rounds_attempts == 1:
                     score_round1.append(int(score))
                elif rounds_attempts == 2:
                     score_round2.append(int(score))
                elif rounds_attempts == 3:
                     score_round3.append(int(score))

            
def newgame(number):
    """
    This function will ask the user if it wants to start a new game 
    or if it wants to exit the app
    """
    new_game_question = input(Fore.YELLOW + "Play Again? (Y/N)")
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
    #players_list(number)
    for q in range(3):
        questions(number, count_questions)
        count_questions += 1
    game_results()
    newgame(number)
#
    
main()


