from cube import *

class Solver:
    def __init__(self, cube) -> None:
        self.cube = cube

    def check_bottom_side(self):
        if self.cube.face_colors[8] == self.cube.face_colors[9] == self.cube.face_colors[10] == self.cube.face_colors[11] == [255, 255, 0]:
            return True

    def recognize_algorithm(self):
        if self.cube.face_colors[12] == self.cube.face_colors[1] == self.cube.face_colors[21] == self.cube.face_colors[4] == [255, 255, 255]:
            return '1'
        elif self.cube.face_colors[15] == self.cube.face_colors[16] == self.cube.face_colors[20] == self.cube.face_colors[0] == [255, 255, 255]:
            return '2'
        elif self.cube.face_colors[15] == self.cube.face_colors[13] == self.cube.face_colors[16] == self.cube.face_colors[17] == [255, 255, 255]:
            return '3'
        elif self.cube.face_colors[15] == self.cube.face_colors[13] == self.cube.face_colors[0] == self.cube.face_colors[4] == [255, 255, 255]:
            return '4'
        elif self.cube.face_colors[12] == self.cube.face_colors[15] == self.cube.face_colors[16] == self.cube.face_colors[1] == [255, 255, 255]:
            return '5'
        elif self.cube.face_colors[16] == self.cube.face_colors[17] == self.cube.face_colors[5] == self.cube.face_colors[1] == [255, 255, 255]:
            return '6'
        elif self.cube.face_colors[1] == self.cube.face_colors[0] == self.cube.face_colors[5] == self.cube.face_colors[4] == [255, 255, 255]:
            return '7'
        else:
            return 'U'

    def oll(self):
        while not self.check_bottom_side():
            self.cube.random_move()
        instructions = ''
        if self.recognize_algorithm() == 'U':
            self.cube.turn_top_clockwise()
            if self.recognize_algorithm() == 'U':
                self.cube.turn_top_clockwise()
                if self.recognize_algorithm() == 'U':
                    self.cube.turn_top_clockwise()
        if self.recognize_algorithm() == '1':
            instructions = 'RURRRURUURRR'
        if self.recognize_algorithm() == '2':
            instructions = 'RUURRRUUURUUURRR'
        if self.recognize_algorithm() == '3':
            instructions = 'FRURRRUUUFFF'
        if self.recognize_algorithm() == '4':
            instructions = 'RURRRUUURRRFRFFF'
        if self.recognize_algorithm() == '5':
            instructions = 'FFFRURRRUUURRRFR'
        if self.recognize_algorithm() == '6':
            instructions = 'FRURRRUUURURRRUUUFFF'
        if self.recognize_algorithm() == '7':
            instructions = 'RRUURUURR'
        return instructions

    def pbl(self):
        pass

