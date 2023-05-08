
def solved(board):
    for i in range(9):
        for j in range(9):
            if not board[i][j]:
                return False
    return True

#checks for duplicate numbers in row/col/3x3 grid
def checkExisting(board,x,y,check):
    for i in range(9):
        if (board[x][i] == check) or (board[i][y] == check):
            return True
    #finds 3x3 grid to check based on x and y
    x = 0 if x < 3 else 3 if x < 6 else 6
    y = 0 if y < 3 else 3 if y < 6 else 6
    i = x
    while i < x+3:
        j = y
        while j < y+3:
            if board[i][j] == check:
                return True
            j + 1
        i + 1
    return False

def valid(board,x,y):
    if (board[x][y] !=0  and y + 1 < 9):
        return valid(board,x,y+1)
    elif (board[x][y] !=0  and x + 1 < 9):
        return valid(board,x+1,y)
    elif (board[x][y] != 0):
        return False
    
    if (board[x][y] == 0 and x < 9 and y < 9):
        for possibleValue in range(1,10):
            if not checkExisting(board, x, y, possibleValue):
                board[x][y] = possibleValue
                if (not valid(board,x,y)):
                    return False
                else:
                    board[x][y] = 0
        return True
    return False

def solveSudoku(board):
    copy = board.copy()
    valid(copy,0,0)
    if (solved(copy)):
        board = copy.copy()
    
