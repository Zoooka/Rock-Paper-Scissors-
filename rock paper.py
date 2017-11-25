import sys
import getpass

# Creates two users, and for users to enter their names
User1 = input("Player one, what is your name? ")
User2 = input("Player two, What is your name? ")

# Counts users wins
User1_wincount = 0
User2_wincount = 0


# Prompts users to enter rock paper scissors etc...
User1_answer = input("%s, do you want to choose rock, paper or scissors? " % User1)
User2_answer = input("%s, do you want to choose rock, paper or scissors? " % User2)

# Compares user ones and user twos inputs and calculates winner
def compare(u1, u2):
    if u1 == u2:
        return("It's a tie!")
    elif u1 == 'rock':
        if u2 == 'scissors':
            return("Rock wins!")
            User1_wincount + 1
        else:
            return('Paper wins!')
    elif u1 == 'scissors':
        if u2 == 'paper':
            return("Scissors wins!")
        else:
            return("Rock wins!")
    elif u1 == 'paper':
        if u2 == 'rock':
            return("Paper wins!")
        else:
            return("Scissors wins!")
    else:
        return("Invalid input. Don't try and get fancy.")
        sys.exit()

# Prints who won to console
print(compare(User1_answer, User2_answer))
# print(User1_wincount, User2_wincount)