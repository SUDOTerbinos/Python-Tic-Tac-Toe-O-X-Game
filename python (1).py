def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    # Check rows, columns, and diagonals
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True
    if board[0][0] == board[1][1] == board[2][2] == player or board[0][2] == board[1][1] == board[2][0] == player:
        return True
    return False

def is_full(board):
    return all(board[i][j] != " " for i in range(3) for j in range(3))

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    turn = 0
    
    while True:
        print_board(board)
        player = players[turn % 2]
        print(f"Player {player}, enter row and column (0-2) separated by space: ")
        
        try:
            row, col = map(int, input().split())
            if board[row][col] != " ":
                print("Cell already occupied! Try again.")
                continue
        except (ValueError, IndexError):
            print("Invalid input! Enter two numbers between 0 and 2.")
            continue
        
        board[row][col] = player
        
        if check_winner(board, player):
            print_board(board)
            print(f"🎉 Player {player} wins! 🎉")
            break
        if is_full(board):
            print_board(board)
            print("It's a draw! 🤝")
            break
        
        turn += 1

if __name__ == "__main__":
    tic_tac_toe()
