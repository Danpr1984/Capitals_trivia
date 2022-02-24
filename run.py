from countries import *
import random
from countryinfo import CountryInfo



names = []
total_score = []
used_countries = []


def number_of_players(names):
    """
    This function will give the user the option to select the amount of 
    players and their names
    """
    welcome = ("Welcome to Capital Trivia!\n")
    print(welcome)
    teasing_message = ("Did you actually learn something at school? :)\nProve it by getting correct answers!\n")
    print(teasing_message)
    players = input("How many players will be playing? ")
    contador = 1
    for i in range(int(players)):
        name = input(f"What is your name player {contador} \n")
        names.append(name)
        contador += 1

    name_list = names
    return name_list




def compare(country):
    """This function checks if any country is repeating in the questions
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
        score = 0
        print(f"It's your turn {n}  \n")
        continues = True
        while (continues):
            count_test = random.choice(list(countries))
            country = count_test
            used_countries.append(country)
            used = compare(country)
            compare(country)
            print(f"What is the capital of {country}\n")
            answer = input('Choose a capital: \n')
            capital = CountryInfo(country).capital()
            if answer == capital:
                print(f'Correct!  {positive_feedback}\n')
                score += 1
                continues = True
                if score == 1:
                    print(f"Your currently have {score} point")
                else:
                    print(f"Your currently have {score} points")
            else:
                print(f'Incorrect! {negative_feedback} The correct answer is {capital}\n')
                continues = True
    print("Rounds are over!")        
    total_score.append(int(score))
            #If return is True continue if not repeat como?


    
    

            
#Newgame()

def main():
    """
    This function runs the game
    """
    number = number_of_players(names)
    questions(number)
    #result = {names[i]: total_score[i] for i in range(len(names))} 
    #print(result)
    
main()


#funcion para comparar y volver a ejectutar
