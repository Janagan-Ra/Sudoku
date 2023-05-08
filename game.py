# GUI.py
import pygame


class sudoku:
    def __init__ (self, rows, collums, size, display):
        self.rows = rows
        self.collums = collums
        self.size = size
        self.model = None
        self.display = display
    


width = 800
hight = 800

def main():
    board = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

    pygame.init()
    font = pygame.font.SysFont('arial',30)
    display = pygame.display.set_mode((width,hight))
    pygame.display.set_caption("Sudoku")
    display.fill((220,220,220))
    
    #grid
    for i in range(0,10):
        pygame.draw.line(display, (0,0,0), ((width/16) + (width/16)*i, (width/16)), ((hight/16) + (hight/16)*i, 500), 2)
        pygame.draw.line(display, (0,0,0), ((width/16), (width/16) + (width/16)*i), (500, (hight/16) + (hight/16)*i), 2)
        if (i % 3 == 0):
            pygame.draw.line(display, (0,0,0), ((width/16) + (width/16)*i, (width/16)), ((hight/16) + (hight/16)*i, 500), 5)
            pygame.draw.line(display, (0,0,0), ((width/16), (width/16) + (width/16)*i), (500, (hight/16) + (hight/16)*i), 5)
        pygame.display.update()

    for i in range(9):
        for j in range(9):
            value = font.render(str(board[i][j]),True,(0,200,0))
            display.blit(value,((j+1)*50 + 50, (i+1)*50 + 50))

    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

main()