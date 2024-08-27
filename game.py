import pygame
from cube import RubiksCube
from buttons import ShuffleButton, SolveButton
from pygame.locals import *
from solver import Solver
import time

class Game:
    def __init__(self):
        pygame.init()
        self.width, self.height = 800, 600
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("3D Cube Rotation")
        self.clock = pygame.time.Clock()
        self.cube = RubiksCube()
        self.angle_x = 0
        self.angle_y = 0
        self.dragging = False

        self.background = pygame.image.load("images/background.jpg").convert()
        self.background = pygame.transform.scale(self.background, (self.width, self.height))

        self.shuffle_button = ShuffleButton()
        self.solve_button = SolveButton()
        self.solver = Solver(self.cube)

    def run(self):
        running = True
        shuffle_counter = 0
        instructions = ''
        instructions2 = ''

        while running:
            self.screen.fill((0, 0, 0))
            for event in pygame.event.get():

                if event.type == QUIT:
                    running = False
                elif event.type == MOUSEBUTTONDOWN:
                    self.dragging = True
                    pygame.mouse.get_rel()
                    if self.shuffle_button.is_clicked(event):
                        x = 20                     
                        shuffle_counter = x
                    if self.solve_button.is_clicked(event):
                        instructions = self.solver.oll()

                elif event.type == MOUSEBUTTONUP:
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

            if shuffle_counter != 0:
                self.cube.random_move()
                shuffle_counter -= 1
                time.sleep(0.1)
            
            if instructions != '':
                instruction = instructions[0]
                instructions = instructions[1:]
                if instruction == 'R':
                    self.cube.turn_right_clockwise()
                elif instruction == 'U':
                    self.cube.turn_top_clockwise()
                elif instruction == 'F':
                    self.cube.turn_front_clockwise()
                time.sleep(0.1)


            self.screen.blit(self.background, (0, 0))
            self.cube.draw(self.screen, self.width, self.height, self.angle_x, self.angle_y)
            self.shuffle_button.draw(self.screen)
            self.solve_button.draw(self.screen)
            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()


if __name__ == "__main__":
    game = Game()
    game.run()