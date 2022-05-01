# Tic Tac Toe  - for CSC_120 Group 7
# __________________________________
# Team members (add your names below)
# Joseph Nater (@jnater)
# Prince Varghese
# Mariam Ahmed
# Michael Whitley

game_started = [False]

player_1 = ["X", "Player 1"]
player_2 = ["O", "Player 2"]


# When a player marks a position, we assign it to the
# appropriate list, so we know which players have
# which positions assigned.
# Positions in this case are numbered 0-9, so when the
# actual game logic runs, these lists will determine
# which player has which position.


def setup_board():
    # Because lists are mutable, we can easily manipulate selections
    # and treat it like a game.

    board = [
        '-', '-', '-',
        '-', '-', '-',
        '-', '-', '-'
    ]

    # Create a default mapping of a clean board where 0-9 are
    # set to False when the game starts.

    board_assigned = [False for _ in board]
    return board, board_assigned


def print_board(n):
    """
    To make reading the code easier, all the values of
    the tictactoe list are assigned to n
    from left to right, the positions are set 0-8, where 0
    is the 1st position
    """
    board = f"""
        {n[0]}|{n[1]}|{n[2]}
        {n[3]}|{n[4]}|{n[5]}
        {n[6]}|{n[7]}|{n[8]}
    """
    print(board)


def loop_game():
    # Setup a clean board to work with
    board, board_assigned = setup_board()

    # Start the actual game logic
    while True:
        # Cycle between player 1, and player 2
        for p in [player_1, player_2]:

            # Print the actual board
            print_board(board)
            # Check for any winning patterns
            # winner_chosen = check_win(board, p)
            winner_chosen = check_win(board, player_1) and check_win(board, player_2)
            tie = check_tie(board)
            if winner_chosen:
                break
            if not winner_chosen:
                if tie:
                    break
            # for char in ["O", "X"]:
            # pattern = (char, char, char)
            # Capture "XXX" or "OOO" pattern
            # I didnt use this for loop - Prince

            retry = True
            # Wait for an actual choice from the player
            while retry and not winner_chosen and not tie:
                if winner_chosen:
                    break
                if not winner_chosen:
                    if tie:
                        break
                try:
                    choice = input(f"{p[1]}, make a selection (1-9) or enter Q to quit: ")
                    if choice.upper() == "Q":
                        exit()
                    else:
                        choice = int(choice) - 1
                except ValueError:
                    print("Please make a valid selection from 1-9 or enter Q to quit.")
                    continue
                except KeyboardInterrupt:
                    game_started[0] = False
                    print()
                    break
                if choice + 1 not in range(1, 10):
                    print("Please make a valid selection from 1-9 or enter Q to quit.")
                    continue
                if board_assigned[choice]:
                    print("That choice has already been selected.")
                    print_board(board)
                    # Retry to get the player's choice if it is invalid
                    retry = True
                else:
                    board_assigned[choice] = True
                    board[choice] = p[0]
                    retry = False
            if winner_chosen:
                break
            if not winner_chosen:
                if tie:
                    break
            if not game_started[0]:
                break
        if winner_chosen:
            break
        if not winner_chosen:
            if tie:
                break
        if not game_started[0]:
            break


# Prince check win
def check_win(board, playerinfo):
    player = playerinfo[0]
    name = playerinfo[1]

    if board[0] == player and board[1] == player and board[2] == player \
            or board[3] == player and board[4] == player and board[5] == player \
            or board[6] == player and board[7] == player and board[8] == player \
            or board[0] == player and board[3] == player and board[6] == player \
            or board[1] == player and board[4] == player and board[7] == player \
            or board[2] == player and board[5] == player and board[8] == player \
            or board[0] == player and board[4] == player and board[8] == player \
            or board[2] == player and board[4] == player and board[6] == player:
        print(f"{name} wins")
        return True
    else:
        return False


def check_tie(board):
    if "-" not in board:
        print("Tie!")
        return True


def main():
    # print main board
    # Logic can then be done anytime before the board is printed
    # and each time we request an input from player 1 or 2.
    # Game logic can either start randomly (player 2 starts first)
    # (or player 1 starts first)

    game_started[0] = True
    print('Welcome to CSC 120 Tic Tac Toe Game')
    print('Player 1 = X and Player 2 = 0')
    while game_started[0]:
        loop_game()
        start = ''
        while start.lower() not in ['y', 'n']:
            start = input("Would you like to play again? (y/n): ")
        game_started[0] = start.lower() == 'y' and True or False


main()
