VALID_CHOICES = ['R', 'r', 'S', 's', 'P', 'p']
REPLAY_CHOICES = ['Y', 'y']

def thatBeats(choice):
    return {
        'p': ['r', 'R', 's', 'S'],
        's': ['r', 'R'],
        'r': []
    }[choice]



def whoWins(player1, player1_choice, player2, player2_choice):
    if player1_choice == player2_choice:
        return "no one"
    else:
        if player2_choice in thatBeats(player1_choice.lower()):
            return player2
        else:
            return player1


player1 = input("Enter name for Player 1: ")
player2 = input("Enter name for Player 2: ")

print("Press R, S or P!")


while(True):
    while(True):
        player1_choice = input("{0}'s turn: ".format(player1))
        if player1_choice in VALID_CHOICES:
            break
        else:
            print("wrong choice!")

    while (True):
        player2_choice = input("{0}'s turn: ".format(player2))
        if player2_choice in VALID_CHOICES:
            break
        else:
            print("wrong choice!")

    winner = whoWins(player1, player1_choice, player2, player2_choice)

    print("{0} wins the game".format(winner))
    replay_choice = input("Press Y/y to play again. Any key to exit")
    if replay_choice not in REPLAY_CHOICES:
        print("Good bye!!!")
        break





