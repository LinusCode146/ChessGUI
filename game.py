import pygame

from consts import *
from board import Board
from dragger import Dragger


class Game:

    def __init__(self) -> None:
        self.board = Board()
        self.dragger = Dragger()

    def show_bg(self, surface) -> None:
        for row in range(ROWS):
            for col in range(COLS):
                if (row + col) % 2 == 0:
                    color = (234, 235, 200)  # lightgreen
                else:
                    color = (119, 154, 88)  # dark green

                rect = (col * SQR_SIZE, row * SQR_SIZE, SQR_SIZE, SQR_SIZE)

                pygame.draw.rect(surface, color, rect)

    def show_pieces(self, surface):
        for row in range(ROWS):
            for col in range(COLS):
                # piece ?
                if self.board.squares[row][col].has_piece():
                    piece = self.board.squares[row][col].piece

                    # all pieces except dragger piece
                    if piece is not self.dragger.piece:
                        piece.set_texture(size=80)
                        img = pygame.image.load(piece.texture)
                        img_center = col * SQR_SIZE + SQR_SIZE // 2, row * SQR_SIZE + SQR_SIZE // 2
                        piece.texture_rect = img.get_rect(center=img_center)
                        surface.blit(img, piece.texture_rect)
