# GUI.py
import pygame
import requests
import Solver

WIDTH = 800
HIGHT = 800
BGC = (220,220,220)
CORRECTION = 15
SCALE = 16

def insert(legal, board, display, position, font):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if legal[int(position[1]-1)][int(position[0]-1)] != 0:
                    return
                if board[int(position[1]-1)][int(position[0]-1)] != 0:
                    pygame.draw.rect(display, BGC, (position[0]*50 + CORRECTION, position[1]*50+ CORRECTION,50 -CORRECTION , 50 - CORRECTION))
                    pygame.display.update()
                if (0 < event.key - 48 < 10):
                    value = font.render(str(event.key-48), True, (0,0,0))
                    display.blit(value, (position[0]*50 + CORRECTION, position[1]*50 + CORRECTION))
                    board[position[1]-1][position[0]-1] = event.key - 48
                    drawLines(display)
                    pygame.display.update()
                    return 
                return
            
def drawLines(display):
    for i in range(0,10):
        pygame.draw.line(display, (0,0,0), ((WIDTH/SCALE) + (WIDTH/SCALE)*i, (WIDTH/SCALE)), ((HIGHT/SCALE) + (HIGHT/SCALE)*i, 500), 2)
        pygame.draw.line(display, (0,0,0), ((WIDTH/SCALE), (WIDTH/SCALE) + (WIDTH/SCALE)*i), (500, (HIGHT/SCALE) + (HIGHT/SCALE)*i), 2)
        if (i % 3 == 0):
            pygame.draw.line(display, (0,0,0), ((WIDTH/SCALE) + (WIDTH/SCALE)*i, (WIDTH/SCALE)), ((HIGHT/SCALE) + (HIGHT/SCALE)*i, 500), 5)
            pygame.draw.line(display, (0,0,0), ((WIDTH/SCALE), (WIDTH/SCALE) + (WIDTH/SCALE)*i), (500, (HIGHT/SCALE) + (HIGHT/SCALE)*i), 5)
        pygame.display.update()

def drawBoard(board, display, font):
    pygame.display.set_caption("Sudoku")
    display.fill(BGC)
    #grid
    drawLines(display)
    for i in range(9):
        for j in range(9):
            if (board[i][j] != 0):
                value = font.render(str(board[i][j]),True,(1,150,32))
                display.blit(value,((j+1)*(WIDTH/SCALE) + 15, (i+1)*(HIGHT/SCALE) + 15))
    pygame.display.update()


def main():
    sugokuAPI = requests.get("https://sugoku.onrender.com/board?difficulty=easy")
    board = sugokuAPI.json()['board']
    pygame.init()
    font = pygame.font.SysFont('arial',30)
    display = pygame.display.set_mode((WIDTH,HIGHT))
    drawBoard(board,display,font)
    legal = Solver.copy.deepcopy(board)
    solution = Solver.solveSudoku(board)
    while True:
        
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                position = pygame.mouse.get_pos()

                insert(legal,board, display, (position[0]//50, position[1]//50),font)
            if event.type == pygame.QUIT:
                pygame.quit()
                return

main()