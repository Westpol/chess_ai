import pygame
import time

screen = pygame.display.set_mode((800, 800))
width, height = screen.get_size()


class Chess:

    def __init__(self):
        pass

    def grid(self):
        flip = True
        for i in range(8):
            flip = not flip
            for k in range(8):
                if flip:
                    pygame.draw.rect(screen, (125, 125, 125), (i * 100, k * 100, 100, 100))
                    flip = not flip
                else:
                    pygame.draw.rect(screen, (0, 0, 0), (i * 100, k * 100, 100, 100))
                    flip = not flip

    def draw(self):
        self.grid()
        pygame.display.flip()


if __name__ == '__main__':
    chess = Chess()
    chess.draw()
    time.sleep(2)
