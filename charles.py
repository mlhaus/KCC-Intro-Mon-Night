from helpers import *
def gimme_a_roulette_color(user_number):
    if user_number == 0 :
        print("Your pocket is green!")
    elif (user_number >= 1 and user_number <= 10) and user_number % 2 == 0 :
        print("Your pcket is black!")
    elif (user_number >= 1 and user_number <= 10) and user_number % 2 != 0 :
        print("Your pocket is red!")
    elif (user_number >= 11 and user_number <= 18) and user_number % 2 == 0 :
        print("Your pocket is red!")
    elif (user_number >= 11 and user_number <= 18) and user_number % 2 != 0 :
        print("Your pocket is black!")
    elif (user_number >= 19 and user_number <= 28) and user_number % 2 == 0 :
        print("Your pocket is black!")
    elif (user_number >= 19 and user_number <= 28) and user_number % 2 != 0 :
        print("Your pocket is red!")
    elif (user_number >= 29 and user_number <= 36) and user_number % 2 == 0 :
        print("Your pocket is red!")
    elif (user_number >= 29 and user_number <= 36) and user_number % 2 != 0 :
        print("Your pocket is black!")
    else : 
        print("Error! Try again! Make sure to use a number 0-36!")

roulette_number = getNum("Pick a roulette number", 0, 36, 3, True, "That number doesn't exist")
gimme_a_roulette_color(roulette_number)