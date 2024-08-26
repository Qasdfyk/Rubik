from cube import *

class Solver:
    def __init__(self, cube) -> None:
        self.cube = cube

    def check_bottom_side(self):
        if self.cube.face_colors[8] == self.cube.face_colors[9] == self.cube.face_colors[10] == self.cube.face_colors[11] == [255, 255, 0]:
            return True

    def do_bottom_side(self):
        while not self.check_bottom_side():
            self.cube.random_move()
    
    
