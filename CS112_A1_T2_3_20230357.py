# File: CS112_A1_T2_3_20230357
# Purpose: This is a two-player game. is played by pile of coins between them. The players take turns removing a non-zero square number such as (1,4,9,16,25,...) from the pile and the player who removes the last coin wins.  
# Author: Mohamed Mustapha Badry Abdullah
# ID: 20230357
#Display the initial game status.
print("Hello everyone this is subtract a square game.")
n_coins = int(input("Enter the number of coins.\n"))
#To make sure that the original number of coins not negative and not equals to zero and not a square number.
while n_coins <= 0 or n_coins**0.5 - int(n_coins**0.5) == 0:
    n_coins = int(input("Wrong, please Enter the number of coins again\n"))
turn_count = 0
while 1:
    if turn_count % 2 == 0:
        turn = int(input("Player 1 enter a non-zero square number: "))
        #To make sure that play is correct.
        while turn > n_coins or turn == 0 or turn < 0 or turn**0.5 - int(turn**0.5) > 0:
            turn = int(input("Wrong, please enter again: "))
    elif turn_count % 2 != 0:
        turn = int(input("Player 2 enter a non-zero square number: "))
        #To make sure that play is correct.
        while turn > n_coins or turn == 0 or turn < 0 or turn**0.5 - int(turn**0.5) > 0:
            turn = int(input("Wrong, please enter again: "))
    #Update the game status.
    n_coins -= turn
    turn_count += 1
    #Display the new status.
    print("The new number of coins is:",n_coins)
    if n_coins == 0 and turn_count % 2 != 0:
        print("Player 1 is the winner, congratulations!")
        break
    elif n_coins == 0 and turn_count % 2 == 0:
        print("Player 2 is the winner, congratulations!")
        break