from countries import *
import random
import keyboard
from countryinfo import CountryInfo
from colorama import Fore
import operator

names = []
score_round1 = []
score_round2 = []
score_round3 = []
used_countries = []


def game_results():
    """
    This app will grab the scores of each round for each player and will
    return the total scores with the outcome of the game
    """
    zipped_lists = zip(score_round1, score_round2, score_round3)
    total_score = [x + y + z for (x, y, z) in zipped_lists]
    result = {}
    for i, j in zip(names, total_score):
        result[i] = j
    print(f"And the final score is:\n {result}")
    mayor=total_score[0]
    index = 0
    tie = False
    for x in range(1,len(names)):
        if total_score[x] == mayor:
            tie = True
        if total_score[x]>mayor:
            mayor=total_score[x]
            index = x
            tie = False
    if tie: 
        print("It's a tie! You must play a REMATCH!")
    else:
        print(f" And the winner is.......{names[index]}!")      
    names.clear()
    score_round1.clear()
    score_round2.clear()
    score_round3.clear()
    used_countries.clear()


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
                    name = validate_name(players_count)
                    names.append(name)
                    players_count += 1
                name_list = names
                play = "y"
                print("Let's get ready to RUMBLE!")
                return name_list
        except Exception:
            print("Please pick a number between 1-4\n")
            play = "n"


def validate_name(players_count):
    """
    This function validates the input for players names
    so that they type a name with more than three characters
    """
    check_name = True
    name = ""
    while (check_name):
        name = input(f"What is your name player {players_count}? \n")
        print("\n")
        if name == '' or len(name) < 3:
            print("Please type a name with more than 3 letters")
            check_name = True
        else:
            check_name = False
    return name        


def check_country(countries):
    validate = True
    while (validate):
        count_test = random.choice(list(countries))
        country = count_test
        used_countries.append(country)
        if country in used_countries:
            validate = False
        else:
            validate = True
    return country


def validate_capital_input(country):
    check_capital = True
    answer = ''
    while (check_capital):
        print(Fore.LIGHTMAGENTA_EX + f"What is the capital of {country}?\n")
        answer = input('Write your answer: \n')
        if answer == '': 
            print("Please write an answer")
            check_capital = True
        else:
            check_capital = False
    return answer    


def questions(number, rounds_attempts):
    """
    This function will chose from a list of countries a random country
    """
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
            country = check_country(countries)
            answer = validate_capital_input(country)
            answer = answer.lower()
            print("\n")
            capital = CountryInfo(country).capital()
            if answer == capital.lower():
                continues = True
                print(Fore.GREEN + f'CORRECT!  {positive_feedback}\n')
                score += 1
                
            else:
                continues = False
                print(Fore.RED + f'INCORRECT! {negative_feedback}\
                The correct answer is {capital}')
                print ("*************************************************************\n"
                       
                      )
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
    rematch = "new"
    while rematch == "new":
        try:
            new_game_question = input(Fore.YELLOW + "Play Again? (Y/N)")
            if (new_game_question != 'Y') and (new_game_question != 'N'):
                raise Exception()
            else:
                if new_game_question  == 'Y':
                    number_of_players(names)
                    count_questions = 1
                    for q in range(3):
                        questions(number, count_questions)
                        count_questions += 1
                    game_results()    
                else:
                    new_game_question == 'N'
                    print("Have a great day! See you next time!")
                    rematch = "now"
        except Exception:
            print("Please type either Y or N")
            rematch = "new"


def main():
    """
    This function runs all the other functions in order to run the game
    """
    number = number_of_players(names)
    count_questions = 1
    for q in range(3):
        questions(number, count_questions)
        count_questions += 1
    game_results()
    newgame(number)


main()
