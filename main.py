import random

def main():
    show_header()

    player = "You"
    robot = "Computer"

    play_game(player, robot)

def show_header():
    print("---------------------------------")  
    print("----Rock, Paper, Scissors v1-----")  
    print("---------------------------------")  

def play_game(player_1, player_2):


    rolls = ['rock', 'paper', 'scissors']

    roll1 = input(f"{player_1}, what is your roll? [rock, paper, scissors]: ")
    roll1 = roll1.lower().strip()
    if roll1 not in rolls:
        print(f"Sorry {player_1}, {roll1} is not a valid play!")


    roll2 = random.choice(rolls)



    #
    #  roll2 = input(f"{player_2}, what is your roll? [rock, paper, scissors]: ")
    # roll2 = roll2.lower().strip()
    # if roll1 not in rolls:
    #     print(f"Sorry {player_2}, {roll2} is not a valid play!")


    print(f"{player_1} rolls {roll1}")
    print(f"{player_2} rolls {roll2}")

    # Test for a winner

    # Rock
    #   Rock -> tie
    #   Paper -> lose
    #   Scissors -> win

    # Paper
    #   Rock -> win
    #   Paper -> tie
    #   Scissors -> lose

    # Scissors
    #   Rock -> lose
    #   Paper -> win
    #   Scissors -> tie

    winner = None

    if roll1 == roll2:
        print("The play was tied!")
    elif roll1 == 'rock':
        if roll2 == 'paper':
            winner = player_2
        elif roll2 == 'scissors':
            winner = player_1 

    elif roll1 == 'paper':
        if roll2 == 'scissors':
            winner = player_2
        elif roll2 == 'rock':
            winner = player_1

    elif roll1 == 'scissors':
        if roll2 == 'rock':
            winner = player_2
        elif roll2 == 'paper':
            winner = player_1

    print("The game is over!")
    if winner is None:
        print("It was a tie!")
    else:
        print(f'{winner} takes the game!')



if __name__ == '__main__':
    main()