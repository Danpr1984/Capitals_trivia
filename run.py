from countries import *
import random
import keyboard
from countryinfo import CountryInfo



names = []
total_score = []
used_countries = []
rounds_attempts = []


def number_of_players(names):
    """
    This function will give the user the option to select the amount of 
    players and their names
    """
    welcome = ("Welcome to CAPITAL TRIVIA!\n")
    print(welcome)
    teasing_message = ("Did you actually learn something in school? :)\nProve it by guessing as many capitals as you can!\n")
    print(teasing_message)
    players = input("How many players will be playing? ")
    contador = 1
    for i in range(int(players)):
        name = input(f"What is your name player {contador}? \n")
        names.append(name)
        contador += 1

    name_list = names
    return name_list
def validate(country):
    """
    This function checks if any country is repeating in the questions and that the input
    is correct. Validation needed for number of players, for str and not numbers when guessing 
    a capital.
    """
    if country in used_countries:
        return True
    else:
        return False

def questions(number):
    """
    This function will chose from a list of countries a random country
    """
    positive_feedback = random.choice(list(random_good_phrases))
    negative_feedback = random.choice(list(random_bad_phrases))
    for n in number:
        attempts = 0
        score = 0
        print(f"It's your turn {n}  \n")
        continues = True
        while (continues): 
            count_test = random.choice(list(countries))
            country = count_test
            used_countries.append(country)
            used = validate(country)
            validate(country)
            print(f"What is the capital of {country}\n")
            answer = input('Choose a capital: \n')
            capital = CountryInfo(country).capital()
            if answer == capital:
                continues = True
                print(f'Correct!  {positive_feedback}\n')
                score += 1
                total_score.append(int(score))
                if score == 1:
                    print(f"Your currently have {score} point")
                else:
                    print(f"Your currently have {score} points")
            else:
                continues = False
                print(f'Incorrect! {negative_feedback} The correct answer is {capital}\n')
                attempts += 1                    
                
                
            #If return is True continue if not repeat como?

            
def newgame():
    """
    This function will ask the user if it wants to start a new game 
    or if it wants to exit the app
    """
    new_game_question = input("Press ENTER to start a new game or ESC to exit")
    if new_game_question  == '':
         number_of_players(names)
         print("It's a rematch!") 
    elif new_game_question == 'ESCAPE':   
        print("Have a great day! See you next time!")
def main():
    """
    This function runs the game
    """
    number = number_of_players(names)
    questions(number)
    #result = {names[i]: total_score[i] for i in range(len(names))} 
    #print(result)
    newgame()
   
    
main()


#funcion para comparar y volver a ejectutar
