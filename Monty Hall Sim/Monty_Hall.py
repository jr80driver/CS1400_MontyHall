# Jacob Smith
# A01476417
# Assn8
# This program will simulate the game 100,000 times

from random import randint

again = 'y'
while again == 'y':
    print("")
    print(" Behold my new evil scheme", '\n', "The Monty Hall Problem Solvinator!", '\n')
    print("S)witch doors")
    print("K)eep original pick", '\n')
    switch = str.lower((input("Which strategy, 'S' or 'K', will you play in this simulation? ")))
    print("")
    sumWins = 0
    winner = 0
    goatOne = 0
    goatTwo = 0
    for count in range(1, 100001):
        count += 1
        player = randint(1, 3)
        winner = randint(1, 3)
        # possible combinations of winner and goats
        if winner == 1:
            goatOne = 2
            goatTwo = 3
        elif winner == 2:
            goatOne = 1
            goatTwo = 3
        elif winner == 3:
            goatOne = 2
            goatTwo = 1



        # outcomes for player switches
        if player == winner and switch == 's':
            sumWins += 0
        elif player == goatTwo and switch == 's':
            sumWins += 1
        elif player == goatOne and switch == 's':
            sumWins += 1
    #    # The only other outcomes are if the switch != 'k'
        if player == winner and switch == 'k':
            sumWins += 1
        else:
            sumWins += 0

    percentage = str(round((100 * (sumWins / 100000)), 2))
    sign = str('%')

    print("After 100,000 plays, you won ", sumWins, "times. Congratulations!")
    print("Your winning percentage is ", percentage + sign, '\n')

    again = str.lower(input("Would you like to play again, Y or N? "))
print('\n', "Curse you Perry the Platypus!")
