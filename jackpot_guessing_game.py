#--------------------------------
#----------Jackpot guessing game----------

import random
import time
import os

player_score = 0
bot_choice = 0

# a function that displays a greeting and alllows the user pick a mode
def greet_intro():
    print("----welcome to Nova's Jackpot guessing game----")


#this function  lets the player select the modes
def modes_on():
    print("----Difficulty----")
    print("1.  Easy (1 to 10)")
    print("2.  medium (1 to 20)")
    print("3.  hard (1 to 30)")

# this function checks if the input for the difficulty might raise a Valueerror(input should be an integer)
def get_player_difficulty():
    global player_difficulty
    modes_on()
    try:
        player_difficulty = int(input("Select Your Difficulty:   "))
    except ValueError:
        print("wrong input")
        get_player_difficulty()
    else:
        confirm_difficulty()

#this function further confirms if the input is in the difficulties options(input must be an integer in [1,2,3])
def confirm_difficulty():
    options_list = [1,2,3]
    if player_difficulty in options_list:
        #call load screen here
        game_start()
    else:
        print("thats not an option")
        get_player_difficulty()

# a simple load screen that erases the terminal
def load_screen():
    print("...Loading...")
    time.sleep(2.0)
    os.system('cls' if os.name =='nt' else 'clear')

#bot difficulty choice
# the code for the bot ton pick a number
def bot_pick():
     global bot_choice
     global player_difficulty
     if player_difficulty == 1:
        bot_choice = random.randint(1,10)
     elif player_difficulty == 2:
        bot_choice = random.randint(1,20)
     else:
        bot_choice = random.randint(1,30)

"""the function for the entire game

it checks for a value error and ensures the correct input is received with a try-except block
and then it uses and if and else statement in a while loop to check if the player is right or wrong while keeping account of the number of times the player can guess(player_lives)
and finally when the while loop is finished it askes for a rematch with another if statement
"""
def game_start():
    global player_score
    print("the bot is choosing a number...")
    bot_pick()
    load_screen()
    # global player_chances #I wanted the player to be able to guess like 3 times before the option to end the game or rematch comes up
    # player_chances = 0
    player_lives = 3
    while player_lives > 0:
        global player_guess
        try:
            player_guess = int(input(f"Guess the number (you have {player_lives} tries):   "))
        except ValueError:
            print("wrong input")
            continue
        if player_guess == bot_choice:
            print("You are correct")
            player_score += 1
            player_lives = 3
            rematch_game()
            break
        else:   
            print("You are wrong")
            player_lives -= 1
            continue
    
    if player_lives == 0:
        print("game Over")
        rematch_game()


#create a function to ask player for rematch
# this function asks the player for a rematch using a while loop and calls the get_player_diffulty fucntion if yes which has the game_start fucntion called within it and if no ends the code using the exit command
# a final else statement checks for input and ensures the while loop wrongs if it is not in the provided options
def rematch_game():
    global player_wants_rematch
    global rematch_confirm
    rematch_confirm = False
    while rematch_confirm != True:
        player_wants_rematch = input("Would You like to play again??(Y for Yes, N for No):   ")
        if player_wants_rematch in ["y", "Y",]:
            rematch_confirm = True
            get_player_difficulty()   #lets player change difficulty
        elif player_wants_rematch in ["n", "N",]:
            print(f"Game over")
            goodbye_message()
            rematch_confirm == False
            exit()
        else:
            print("wrong input")
            continue

#the goodbye message which is called  in the rematch_game function
def goodbye_message():
    print("----------THANKS FOR PLAYING----------")
    print("--------------------------------------")

#call the functions like the avengers
greet_intro()
get_player_difficulty()




