# GUI.py
import pygame
import requests
import Solver

WIDTH = 800
HIGHT = 800
BGC = (220,220,220)

def insert(board, display, postion, font):

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if board[postion[1]-1][postion[0]-1] != 0:
                    return
                if (0 < event.key - 48 < 10):
                    pygame.draw.rect(display,BGC,(postion[0]*(HIGHT/16) + 15, postion[1]*(WIDTH/16) + 15, (HIGHT/16)-15,(WIDTH/16))-15)
                    value = font.render(str(event.key - 48),True,(0,0,0))
                    display.blit(value, (postion[0]*(HIGHT/16),postion[1]*(WIDTH/16)))
                    board[postion[1]-1][postion[0]-1] = event.key - 48
                    pygame.display.update()
                return
def drawBoard(board, display, font):
    pygame.display.set_caption("Sudoku")
    display.fill(BGC)
    #grid
    for i in range(0,10):
        pygame.draw.line(display, (0,0,0), ((WIDTH/16) + (WIDTH/16)*i, (WIDTH/16)), ((HIGHT/16) + (HIGHT/16)*i, 500), 2)
        pygame.draw.line(display, (0,0,0), ((WIDTH/16), (WIDTH/16) + (WIDTH/16)*i), (500, (HIGHT/16) + (HIGHT/16)*i), 2)
        if (i % 3 == 0):
            pygame.draw.line(display, (0,0,0), ((WIDTH/16) + (WIDTH/16)*i, (WIDTH/16)), ((HIGHT/16) + (HIGHT/16)*i, 500), 5)
            pygame.draw.line(display, (0,0,0), ((WIDTH/16), (WIDTH/16) + (WIDTH/16)*i), (500, (HIGHT/16) + (HIGHT/16)*i), 5)
        pygame.display.update()

    for i in range(9):
        for j in range(9):
            if (board[i][j] != 0):
                value = font.render(str(board[i][j]),True,(0,0,0))
                display.blit(value,((j+1)*(WIDTH/16) + 15, (i+1)*(HIGHT/16) + 15))
    pygame.display.update()


def main():
    sugokuAPI = requests.get("https://sugoku.onrender.com/board?difficulty=medium")
    board = sugokuAPI.json()['board']
    pygame.init()
    font = pygame.font.SysFont('arial',30)
    display = pygame.display.set_mode((WIDTH,HIGHT))
    #solution = Solver.solveSudoku(board)
    drawBoard(board,display,font)

    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                postion = pygame.mouse.get_pos()
                insert(board, display, (postion//(WIDTH/16)),font)
            if event.type == pygame.QUIT:
                pygame.quit()
                return

main()