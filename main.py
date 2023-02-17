import pygame
import time
import math

screen = pygame.display.set_mode((800, 800))
width, height = screen.get_size()


class Chess:

    def __init__(self):
        self.row = 0
        self.coll = 0

    def grid(self):
        flip = True
        for i in range(8):
            flip = not flip
            for k in range(8):
                if flip:
                    pygame.draw.rect(screen, (125, 125, 125), (i * 100, k * 100, 100, 100))
                    if self.coll == i and self.row == k:
                        pygame.draw.rect(screen, (175, 175, 175), (i * 100, k * 100, 100, 100))
                    flip = not flip
                else:
                    pygame.draw.rect(screen, (0, 0, 0), (i * 100, k * 100, 100, 100))
                    if self.coll == i and self.row == k:
                        pygame.draw.rect(screen, (50, 50, 50), (i * 100, k * 100, 100, 100))
                    flip = not flip

    def mouseHover(self):
        pygame.event.pump()
        mouseX, mouseY = pygame.mouse.get_pos()
        self.coll = math.floor(mouseX / 100)
        self.row = math.floor(mouseY / 100)
        print(str(self.row) + str(self.coll))

    def update(self):
        self.mouseHover()

    def draw(self):
        self.mouseHover()
        self.grid()
        pygame.display.flip()


if __name__ == '__main__':
    while 1:
        chess = Chess()
        chess.draw()
        chess.update()
