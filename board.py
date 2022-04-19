# Tic Tac Toe Rough Draft Template 2
# Joseph Nater (@jnater)
# for CSC_120 Group 7

game_started = [False]

player_1 = ["X", "Player 1"]
player_2 = ["O", "Player 2"]

# When a player marks a position, we assign it to the
# appropriate list so we know which players have
# which positions assigned.
# Positions in this case are numbered 0-9, so when the
# actual game logic runs, these lists will determine
# which player has which position.


def setup_board():
    # Because lists are mutable, we can easily manipulate selections
    # and treat it like a game.

    board = [
        '-','-','-',
        '-','-','-',
        '-','-','-'
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
            for char in ["O", "X"]:
                pattern = (char, char, char)
                # Capture "XXX" or "OOO" pattern
                # TODO: Add all different winning patterns (possible options of winning)
                # e.g check for each row, and also check diagonally |X|
                #                                                     |X|
                #                                                       |X|
                if pattern == (board[0], board[1], board[2]):
                    if char == "O":
                        print("Player 2 wins!")
                    if char == "X":
                        print("Player 1 wins!")
                    return
            
            retry = True
            # Wait for an actual choice from the player
            while retry:
                try:
                    choice = int(input(f"{p[1]}, make a selection (1-9): "))-1
                except ValueError:
                    print("Please make a valid selection from 1-9.")
                    continue
                except KeyboardInterrupt:
                    game_started[0] = False
                    print()
                    break
                if choice+1 not in range(1,10):
                    print("Please make a valid selection from 0-9.")
                    continue
                if board_assigned[choice] != False:
                    print("That choice has already been selected.")
                    print_board(board)
                    # Retry to get the player's choice if it is invalid
                    retry = True
                else:
                    board_assigned[choice] = True
                    board[choice] = p[0]
                    retry = False
            if not game_started[0]:
                break
        if not game_started[0]:
            break




def main():
    # print main board
    # Logic can then be done anytime before the board is printed
    # and each time we request an input from player 1 or 2.
    # Game logic can either start randomly (player 2 starts first)
    # (or player 1 starts first)

    game_started[0] = True

    while game_started[0]:
        loop_game()
        game_started[0] = input("Would you like to play again? (y/n): ") == 'y' and True or False


main()
