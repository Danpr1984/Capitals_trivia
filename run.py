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


def number_of_players(names):
    """
    Prints welcome messages. Runs a while loop
    for number of players input which is validated
    with try statement to get check input and repeats
    until data is valid.
    """
    print("\n")
    print(Fore.YELLOW + "  Welcome to CAPITAL TRIVIA!")
    print("  ********************************")
    print("\n")
    print("  Did you actually learn something in school? :)")
    print("\n")
    print("  Prove it by guessing as many capitals as you can!\n")
    play = "n"
    while play == "n":
        try:
            print(Fore.LIGHTMAGENTA_EX + "  min 1 / max 4")
            players = input("  How many players will be playing? ")
            print("\n")
            if ((players != "1") and
               (players != "2") and
               (players != "3") and
               (players != "4")):
                raise Exception()
            else:
                players_count = 1
                for i in range(int(players)):
                    name = validate_name(players_count)
                    names.append(name)
                    players_count += 1
                name_list = names
                play = "y"
                print(Fore.YELLOW + "  Let's get ready to RUMBLE!")
                print("  *****************************\n")
                return name_list
        except Exception:
            print("  Please pick a number between 1-4\n")
            play = "n"


def game_results():
    """
    With zip() grabs the scores from each round. Creates a
    dictionary that loops to get each player's name and score.
    With a loop it compares scores and gets the index with the
    highest score and prints a winner message or tie message
    All the lists are cleared in the end so that runs a new game
    without pasts game data.
    """
    zipped_lists = zip(score_round1, score_round2, score_round3)
    total_score = [x + y + z for (x, y, z) in zipped_lists]
    result = {}
    for i, j in zip(names, total_score):
        result[i] = j
    print(Fore.YELLOW + f"  And the final score is:\n  {result}")
    print("\n")
    highest_score = total_score[0]
    index = 0
    tie = False
    for x in range(1, len(names)):
        if total_score[x] == highest_score:
            tie = True
        if total_score[x] > highest_score:
            highest_score = total_score[x]
            index = x
            tie = False
    if tie:
        print(" It's a tie! You must play a REMATCH!")
        print("\n")
    else:
        print(f"  And the winner is.......{names[index]}!\n")
        print("\n")
    names.clear()
    score_round1.clear()
    score_round2.clear()
    score_round3.clear()
    used_countries.clear()


def validate_name(players_count):
    """
    Runs a while loop that validates correct input for names
    It will repeatedly ask for valid input until is valid.
    """
    check_name = True
    name = ""
    while (check_name):
        name = input(f"  What is your name player {players_count}? \n  ")
        print("\n")
        if name == '' or len(name) < 2:
            print(" Please type a name with more than 2 letters")
            check_name = True
        else:
            check_name = False
    return name


def check_country(countries):
    """
    Run a while loop that checks from used countries list
    if a country has been already guessed so it doesn't pop up
    again in the questions.
    """
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
    """
    Runs a while loop that checks an answer is typed and
    invalidates empty spaces to continue.
    """
    check_capital = True
    answer = ''
    while (check_capital):
        print(Fore.LIGHTMAGENTA_EX + f"  What is the capital of {country}?\n")
        answer = input('  Write your answer: \n  ')
        if answer == '':
            print("  Please write an answer")
            check_capital = True
        else:
            check_capital = False
    return answer


def questions(number, rounds_attempts):
    """
    This function controls the flow of the trivia game.
    Runs a for loop that iterates on each player for questions.
    Declares the validate_capital_input to.
    Runs a while loop to continue making questions if answer is
    correct and changes player if it's incorrect.
    Adds points on each round to score_rounds lists and prints messages
    with feedback depending on your answer.
    It sets the game rounds to three.
    """
    global score_round1
    global score_round2
    global score_round3
    positive_feedback = random.choice(list(random_good_phrases))
    negative_feedback = random.choice(list(random_bad_phrases))
    for n in number:
        score = 0
        print(Fore.YELLOW + f"  It's your turn {n}  \n")
        continues = True
        while (continues):
            country = check_country(countries)
            answer = validate_capital_input(country)
            answer = answer.lower()
            print("\n")
            capital = CountryInfo(country).capital()
            if answer == capital.lower():
                continues = True
                print(Fore.GREEN + f'  CORRECT! {positive_feedback}\n')
                score += 1
                if score == 1:
                    print(f"  You've scored {score} point this round {n}\n")
                else:
                    print(f"  You've scored {score} points this round {n}\n")
            else:
                continues = False
                print(Fore.RED + f"  INCORRECT! {negative_feedback}")
                print(f"  The correct answer is {capital}")
                score += 0
                if rounds_attempts == 1:
                    score_round1.append(int(score))
                    print(f"  Round 1 is over for you {n}")
                    print ("  *************************************\n")
                elif rounds_attempts == 2:
                    score_round2.append(int(score))
                    print(f"  Round 2 is over for you {n}")
                    print ("  *************************************\n")
                elif rounds_attempts == 3:
                    print(f"  Game is over for you {n}")
                    print ("  *************************************\n")
                    score_round3.append(int(score))


def newgame(number):
    """
    Runs a while loop that asks the users for a new game or to exit.
    It validates with a try statement if the input is correct and will
    repeatedly ask for valid input until is valid.
    Calls the functions that run the game to start a new game.
    """
    rematch = "new"
    while rematch == "new":
        try:
            new_game_question = input(Fore.YELLOW + "  Play Again? (y/n)")
            if (new_game_question != 'y') and (new_game_question != 'n'):
                raise Exception()
            else:
                if new_game_question == 'y':
                    number_of_players(names)
                    count_questions = 1
                    for q in range(3):
                        questions(number, count_questions)
                        count_questions += 1
                    game_results()
                else:
                    new_game_question == 'n'
                    print("\n  Have a great day! See you next time!")
                    rematch = "now"
        except Exception:
            print("  Please type either Y or N")
            rematch = "new"


def main():
    """
    Runs all program functions.
    """
    number = number_of_players(names)
    count_questions = 1
    for q in range(3):
        questions(number, count_questions)
        count_questions += 1
    game_results()
    newgame(number)


main()
