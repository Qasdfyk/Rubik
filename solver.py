from cube import *
from collections import Counter

def most_repeated_count(lst):
    if not lst:
        return 0
    tupled_lst = [tuple(item) if isinstance(item, list) else item for item in lst]
    count = Counter(tupled_lst)
    return max(count.values())

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

    def is_full_side(self):
        if most_repeated_count(self.front_face) == 4 or most_repeated_count(self.back_face) == 4 or most_repeated_count(self.right_face) == 4 or most_repeated_count(self.left_face) == 4:
            return True
        else:
            return False
    
    def load_faces(self):
        self.front_face = [self.cube.face_colors[0], self.cube.face_colors[1], self.cube.face_colors[2], self.cube.face_colors[3]]
        self.right_face = [self.cube.face_colors[20], self.cube.face_colors[21], self.cube.face_colors[22], self.cube.face_colors[23]]
        self.left_face = [self.cube.face_colors[16], self.cube.face_colors[17], self.cube.face_colors[18], self.cube.face_colors[19]]
        self.back_face = [self.cube.face_colors[5], self.cube.face_colors[4], self.cube.face_colors[6], self.cube.face_colors[7]]

    def recognize_algorithms_pbl(self):
        self.load_faces()
        instructions = ""
        if not self.is_full_side():
            self.cube.turn_top_clockwise()
            self.load_faces()
            if not self.is_full_side():
                self.cube.turn_top_clockwise()
                self.load_faces()
                if not self.is_full_side():
                    self.cube.turn_top_clockwise()
                    self.load_faces()

        if self.is_full_side():
            if most_repeated_count(self.front_face) == 4:
                instructions = "RURRRUUURRRFRRUUURRRUUURURRRFFF"
                print('1')
            if most_repeated_count(self.right_face) == 4:
                instructions = "RURRRUUURRRFRRUUURRRUUURURRRFFF"
                print('2')
            if most_repeated_count(self.back_face) == 4:
                instructions = "RURRRUUURRRFRRUUURRRUUURURRRFFF"
                print('3')
            if most_repeated_count(self.left_face) == 4:
                if self.cube.face_colors[0] != self.cube.face_colors[1]:
                    instructions = "RURRRUUURRRFRRUUURRRUUURURRRFFF"
                else:
                    instructions = "RRRUUURURFRRURURRRUUURF"

        else:
            instructions = "RRRUUURURFRRURURRRUUURF"
            print(':(')
        return instructions

    def pbl(self):
        return self.recognize_algorithms_pbl()

