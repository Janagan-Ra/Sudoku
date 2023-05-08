# GUI.py
import pygame
pygame.font.init()


class sudoku:
    def __init__ (self, rows, collums, display):
        self.rows = rows
        self.collums = collums




def main():
    display = pygame.display.set_mode((800,800))
    pygame.display.set_caption("Sudoku")
    board = sudoku(9, 9,display)
    key = None
    run = True
  
main()
pygame.quit()