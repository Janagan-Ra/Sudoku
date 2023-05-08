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
    pygame.init()
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
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

main()