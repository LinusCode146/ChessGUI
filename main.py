import pygame
import sys

from consts import *
from game import Game


class Main:
    def __init__(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('Chess')
        self.game = Game()

    def mainloop(self) -> None:

        game = self.game
        screen = self.screen

        while True:
            game.show_bg(screen)
            game.show_pieces(screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit(0)

            pygame.display.update()


main = Main()
main.mainloop()
