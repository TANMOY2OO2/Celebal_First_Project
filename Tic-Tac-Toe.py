# Tic-Tac-Toe

# Create the board
board = [' ' for _ in range(9)]

# Function to display the board
def display_board():
    print('-------------')
    print('|', board[0], '|', board[1], '|', board[2], '|')
    print('-------------')
    print('|', board[3], '|', board[4], '|', board[5], '|')
    print('-------------')
    print('|', board[6], '|', board[7], '|', board[8], '|')
    print('-------------')

# Function to check for a win
def check_win():
    # Rows
    if board[0] == board[1] == board[2] != ' ':
        return True
    if board[3] == board[4] == board[5] != ' ':
        return True
    if board[6] == board[7] == board[8] != ' ':
        return True

    # Columns
    if board[0] == board[3] == board[6] != ' ':
        return True
    if board[1] == board[4] == board[7] != ' ':
        return True
    if board[2] == board[5] == board[8] != ' ':
        return True

    # Diagonals
    if board[0] == board[4] == board[8] != ' ':
        return True
    if board[2] == board[4] == board[6] != ' ':
        return True

    return False

# Function to check for a draw
def check_draw():
    return ' ' not in board

# Function to play the game
def play_game():
    current_player = 'X'
    game_over = False

    while not game_over:
        display_board()

        position = int(input("Enter a position (1-9): ")) - 1

        if board[position] == ' ':
            board[position] = current_player

            if check_win():
                display_board()
                print("Congratulations! Player", current_player, "wins!")
                game_over = True
            elif check_draw():
                display_board()
                print("It's a draw!")
                game_over = True
            else:
                current_player = 'O' if current_player == 'X' else 'X'
        else:
            print("That position is already filled. Try again.")

# Start the game
play_game()
