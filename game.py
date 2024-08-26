import pygame
from cube import RubiksCube
from button import ShuffleButton
from pygame.locals import *
from rotation_functions import get_orientation

class Game:
    def __init__(self):
        pygame.init()
        self.width, self.height = 800, 600
        self.screen = pygame.display.set_mode((self.width, self.height))
        bg = pygame.image.load("images/background.jpg")
        pygame.display.set_caption("3D Cube Rotation")
        self.clock = pygame.time.Clock()
        self.cube = RubiksCube()
        self.angle_x = 0
        self.angle_y = 0
        self.dragging = False

        self.background = pygame.image.load("images/background.jpg").convert()
        self.background = pygame.transform.scale(self.background, (self.width, self.height))

        self.shuffle_button = ShuffleButton()

    def run(self):
        running = True
        orientation = 'front'
        while running:
            self.screen.fill((0, 0, 0))

            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
                elif event.type == MOUSEBUTTONDOWN:
                    self.dragging = True
                    pygame.mouse.get_rel()
                    if self.shuffle_button.is_clicked(event):
                        self.cube.shuffle()
                elif event.type == MOUSEBUTTONUP:
                    orientation = get_orientation(self.angle_y, self.angle_x)
                    self.dragging = False

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_t:
                        self.cube.turn_top_clockwise()
                    elif event.key == pygame.K_r:
                        self.cube.turn_right_clockwise()
                    elif event.key == pygame.K_f:
                        self.cube.turn_front_clockwise()

            if self.dragging:
                mx, my = pygame.mouse.get_rel()
                self.angle_x -= my * 0.01
                self.angle_y -= mx * 0.01

            self.screen.blit(self.background, (0, 0))

            self.cube.draw(self.screen, self.width, self.height, self.angle_x, self.angle_y, orientation)
            self.shuffle_button.draw(self.screen)
            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()


if __name__ == "__main__":
    game = Game()
    game.run()