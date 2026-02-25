def checkWIn(board):
    wins = [[0,1,2], [3,4,5], [6,7,8],  
            [0,3,6], [1,4,7], [2,5,8],  
            [0,4,8], [2,4,6]]
    for combo in wins:
        a, b, c = combo
        if board[a] == board[b] == board[c] and board[a] != ' ':
            return board[a]
    return None

def print_board(board):
    print(board[0], "|", board[1], "|", board[2])
    print(board[3], "|", board[4], "|", board[5])
    print(board[6], "|", board[7], "|", board[8])

def is_board_full(board):
    return ' ' not in board

def minimax(board, is_maximizing):
    
    winner = checkWIn(board)
    if winner == 'X': return 1    
    if winner == 'O': return -1   
    if is_board_full(board): return 0

    if is_maximizing:
        bestScore = -float('inf')
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                score = minimax(board, False)
                board[i] = ' '
                bestScore = max(bestScore,score)
        return bestScore
    else:
        bestScore = float('inf')
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                score = minimax(board, True)
                board[i] = ' '
                bestScore = min(bestScore,score)
        return bestScore

def bestMove(board):
    bestScore = -float('inf')
    move = -1
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'X'
            score = minimax(board,False)
            board[i] = ' '
            if score > bestScore:
                bestScore = score
                move = i
    return move

board = [' '] * 9  

while True:
    
    ai_move = bestMove(board)
    board[ai_move] = 'X'
    print(f"AI played at position {ai_move}")

    if checkWIn(board):
        print_board(board)
        print("AI wins!")
        break
    if is_board_full(board):
        print_board(board)
        print("Draw!")
        break

    print_board(board)
    human_move = int(input("Your move (0-8): "))
    if board[human_move] != ' ':
        print("That cell is taken!")
        continue
    board[human_move] = 'O'

    if checkWIn(board):
        print_board(board)
        print("You win!")
        break
    if is_board_full(board):
        print_board(board)
        print("Draw!")
        break
    
    