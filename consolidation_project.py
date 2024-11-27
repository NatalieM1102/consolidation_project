# this is my amazing project!
##### “Tuple Out” Dice Game!!!
# For this project, you will implement a simulation of a simple dice game with the following rules:
# The object of the game is to score the most points, or to be the first to reach a certain score.
# Players take turns rolling dice to score points, as described below.
# Each turn, the active player rolls three dice:
# If all three dice are rolled with the same number, the player has “tupled out”, and ends their
# turn with zero points. (For example, rolling three “4”s at the same time.)
# If two dice have the same value, they are “fixed”, and they cannot be re-rolled.
# During their turn, the player can re-roll any dice that are not “fixed”, as often as they would
# like, until they decide to stop, or until they “tuple out” (get three of the same number).
# When a player decides to stop, they score points equal to the total of the three dice, and then
# their turn ends.
# If a player “tuples out”, their turn ends and they score 0 points for that turn.

import random
# make a function for three dice
def roll_dice():
    # roll the dice
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    die3 = random.randint(1, 6)
    return die1, die2, die3

# make a function for "tupling out"
def tuple_out(dice):
    # make a dictionary to store the roll values
    count_dict = {}
    # go through the dice and see if any are the same
    for die in dice:
        if die in count_dict:
            # increase the count for that value if it is being repeated
            count_dict[die] += 1
        else:
            # otherwise keep the value 1
            count_dict[die] = 1
    # return true if all the dice are the same?
    return len(count_dict) == 1 and list(count_dict.values())[0] == 3        

    # calculate the score
def score_calculator(dice):
    # return the score
    return sum(dice)

# how a turn should look 
def individual_turn(high_score):
    # track the score for the turn
    overall_turn_score = 0
    while True:
        # role the dice
        die1, die2, die3 = roll_dice()
        # tell the player what was rolled for each dice
        print(f"You rolled: Dice 1: {die1}, Dice 2: {die2}, Dice 3: {die3}")
        # if the player "tuples out"
        if tuple_out([die1, die2, die3]):
            # tell them
            print("You tupled out! Score: 0")
            # do not change the high score
            return 0, high_score

        # make the calculated score the actual score
        roll_score = score_calculator([die1, die2, die3])
        # add the score to the total score
        overall_turn_score += roll_score

        # print out the score for the user
        print(f"You just rolled: {roll_score}")
        # tell them the overall score for the round
        print (f"Your total score for the round is: {overall_turn_score}")

        keep_rolling = input("Do you want to roll again? Please enter [y/n]: ").lower()
        while keep_rolling not in ['y', 'n']:  # Ensure valid input
            print("Invalid input. Please enter 'y' to continue rolling or 'n' to stop.")
            keep_rolling = input("Do you want to roll again? (y/n): ").lower()
    
        # If the player decides not to roll again
        if keep_rolling != 'y': 
            break

    # handle high scores
    if overall_turn_score > high_score:
        # if the score is higher than the existing high score, make it the new high score
        high_score = overall_turn_score
        # tell the player
        print (f"You got a high score! {high_score}")
    else:
        # tell the player they did not get a high score
        print(f"Your high score is still {high_score}")

    # return the score and high score
    return overall_turn_score, high_score

# basic framework for the game
def game():
    # start with the high score set as 0
    high_score = 0
    while True: 
        # ask if the player wants to play
        print ("\nNew Turn!")
        score, high_score = individual_turn(high_score)

        # ask if they want to continue
        another_turn = input("Do you want to play another round? Please enter [y/n]: ").lower()
        while another_turn not in ['y', 'n']:
            # if they dont enter y or n
            print("Invalid input. Please enter 'y' to continue or 'n' to stop.")
            # ask again
            another_turn = input("Do you want to play another round? Please enter [y/n]: ").lower()
        if another_turn != 'y':
            break
    print(f"Game over! Your final high score is: {high_score}")
# run the game
game()



    
        