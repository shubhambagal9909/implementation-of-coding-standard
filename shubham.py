def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_win(board, player):
    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True

    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    # Check diagonals
    if all(board[i][i] == player for i in range(3)) or \
       all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def check_draw(board):
    return all(cell != ' ' for row in board for cell in row)

def tic_tac_toe():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'

    print("Welcome to Tic-Tac-Toe!")
    print_board(board)

    while True:
        try:
            move = input(f"Player {current_player}, enter your move (row and column: 1 1): ")
            row, col = map(int, move.strip().split())
            row -= 1
            col -= 1

            if board[row][col] != ' ':
                print("That cell is already taken. Try again.")
                continue

            board[row][col] = current_player
            print_board(board)

            if check_win(board, current_player):
                print(f"🎉 Player {current_player} wins!")
                break

            if check_draw(board):
                print("It's a draw!")
                break

            current_player = 'O' if current_player == 'X' else 'X'

        except (ValueError, IndexError):
            print("Invalid input. Please enter row and column as two numbers from 1 to 3.")

if __name__ == "__main__":
    tic_tac_toe()
