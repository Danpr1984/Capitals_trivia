from countries import *
import random
from countryinfo import CountryInfo

names = []
used_countries = [] 
total_score = []
result = [used_countries + total_score]


def number_of_players():
    """
    This function will give the user the option to select the amount of 
    players and their names
    """
    welcome = ("Welcome to Capital Trivia!\nThe game which shows if you actually learned something at school :) \n")
    print(welcome)
    players = input("How many players will be playing?")
    contador = 1
    for i in range(int(players)):
        name = input(f"What is your name player {contador} ")
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


def main():
    """
    This function runs the game
    """
    number = number_of_players()
    questions(number)
    print(result)


    
main()

#funcion para comparar y volver a ejectutar
