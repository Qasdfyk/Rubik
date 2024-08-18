import pygame
from cube import Cube
from pygame.locals import *


class Game:
    def __init__(self):
        pygame.init()
        self.width, self.height = 800, 600
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("3D Cube Rotation")
        self.clock = pygame.time.Clock()
        self.cube = Cube()
        self.angle_x = 0
        self.angle_y = 0
        self.dragging = False

    def run(self):
        running = True
        while running:
            self.screen.fill((0, 0, 0))

            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
                elif event.type == MOUSEBUTTONDOWN:
                    self.dragging = True
                    pygame.mouse.get_rel()
                elif event.type == MOUSEBUTTONUP:
                    self.dragging = False

            if self.dragging:
                mx, my = pygame.mouse.get_rel()
                self.angle_x -= my * 0.01
                self.angle_y -= mx * 0.01

            self.cube.draw(self.screen, self.width, self.height, self.angle_x, self.angle_y)

            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()


if __name__ == "__main__":
    game = Game()
    game.run()