# Tic Tac Toe Rough Template
# Stage 1 Submission - Joseph Nater (@jnater)
# for CSC_120 Group 7

# Because lists are mutable, we can easily manipulate selections
# and treat it like a game.

tictactoe = [
    '-','-','-',
    '-','-','-',
    '-','-','-'
]

# Create a default mapping of a clean board where 0-9 are
# set to False when the game starts.

tictactoe_assigned = [False for _ in tictactoe]

player_1, player_1_name = "X", "Player 1"
player_2, player_2_name = "O", "Player 2"

# When a player marks a position, we assign it to the
# appropriate list so we know which players have
# which positions assigned.
# Positions in this case are numbered 0-9, so when the
# actual game logic runs, these lists will determine
# which player has which position.

p1_assigned = []
p2_assigned = []


def print_board():
    """
    To make reading the code easier, all the values of
    the tictactoe list are assigned to n
    from left to right, the positions are set 0-8, where 0
    is the 1st position
    """
    n = tictactoe
    board = f"""
        {n[0]}|{n[1]}|{n[2]}
        {n[3]}|{n[4]}|{n[5]}
        {n[6]}|{n[7]}|{n[8]}
    """
    return board


def main():
    # print main board
    # Logic can then be done anytime before the board is printed
    # and each time we request an input from player 1 or 2.
    # Game logic can either start randomly (player 2 starts first)
    # (or player 1 starts first)
    print(print_board())


main()
