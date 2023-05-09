
import copy

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

    for i in range(x,x+3):
        for j in range(y,y+3):
            if board[i][j] == check:
                return True
    return False

def valid(board,x,y):
    if (board[x][y] !=0  and y + 1 < 9):
        return valid(board,x,y+1)
    if (board[x][y] !=0  and x + 1 < 9):
        return valid(board,x+1,0)
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
    copyBoard = copy.deepcopy(board)
    valid(copyBoard,0,0)
    if (solved(copyBoard)):  
        return copyBoard
    return board