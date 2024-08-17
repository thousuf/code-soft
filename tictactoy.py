def print_board(board):
    """Prints the Tic Tac Toe board."""
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_win(board, player):
    """Checks if the current player has won."""
    # Check rows
    for row in board:
        if all([cell == player for cell in row]):
            return True
    # Check columns
    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True
    # Check diagonals
    if all([board[i][i] == player for i in range(3)]) or all([board[i][2-i] == player for i in range(3)]):
        return True
    return False

def is_board_full(board):
    """Checks if the board is full."""
    for row in board:
        for cell in row:
            if cell == ' ':
                return False
    return True

def tic_tac_toe():
    """Main function to start the Tic Tac Toe game."""
    board = [[' ' for _ in range(3)] for _ in range(3)]  # Initialize empty board
    current_player = 'X'
    
    while True:
        print_board(board)
        print(f"Player {current_player}'s turn.")
        
        # Get player input
        row = int(input("Enter row (0, 1, 2): "))
        col = int(input("Enter column (0, 1, 2): "))
        
        # Check if the chosen cell is empty
        if board[row][col] == ' ':
            board[row][col] = current_player
            
            # Check if the current player wins
            if check_win(board, current_player):
                print_board(board)
                print(f"Player {current_player} wins!")
                break
            
            # Check if the board is full (tie)
            if is_board_full(board):
                print_board(board)
                print("It's a tie!")
                break
            
            # Switch to the other player
            current_player = 'O' if current_player == 'X' else 'X'
        else:
            print("That cell is already taken. Try again.")

if __name__ == "__main__":
    tic_tac_toe()
