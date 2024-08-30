from cube import *
from collections import Counter

def most_repeated_count(lst):
    if not lst:
        return 0
    tupled_lst = [tuple(item) if isinstance(item, list) else item for item in lst]
    count = Counter(tupled_lst)
    return max(count.values())

def max_counts(input_list):
    output = []
    for sublist in input_list:
        if sublist:  # Check if the sublist is not empty
            max_count = max(sublist.count(item) for item in sublist)
            output.append(max_count)
        else:
            output.append(0)  # For empty sublists, append 0
    return output

def find_first_occurrence(input_list, x):
    for i, sublist in enumerate(input_list):
        if x in sublist:
            return i
    return -1

class Solver:
    def __init__(self, cube) -> None:
        self.cube = cube

    def is_solved(self):
        if (
                self.cube.face_colors[0] == self.cube.face_colors[1] == self.cube.face_colors[2] == self.cube.face_colors[3] and
                self.cube.face_colors[16] == self.cube.face_colors[17] == self.cube.face_colors[18] == self.cube.face_colors[19] and
                self.cube.face_colors[14] == self.cube.face_colors[15] == self.cube.face_colors[12] == self.cube.face_colors[13] and
                self.cube.face_colors[20] == self.cube.face_colors[21] == self.cube.face_colors[22] == self.cube.face_colors[23] and
                self.cube.face_colors[5] == self.cube.face_colors[4] == self.cube.face_colors[6] == self.cube.face_colors[7] and
                self.cube.face_colors[8] == self.cube.face_colors[9] == self.cube.face_colors[10] == self.cube.face_colors[11]
            ):
            return True

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
        if self.is_solved():
            return ''
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

    
    def load_faces(self):
        self.front_face = [self.cube.face_colors[0], self.cube.face_colors[1], self.cube.face_colors[2], self.cube.face_colors[3]]
        self.right_face = [self.cube.face_colors[20], self.cube.face_colors[21], self.cube.face_colors[22], self.cube.face_colors[23]]
        self.left_face = [self.cube.face_colors[16], self.cube.face_colors[17], self.cube.face_colors[18], self.cube.face_colors[19]]
        self.back_face = [self.cube.face_colors[5], self.cube.face_colors[4], self.cube.face_colors[6], self.cube.face_colors[7]]

    def t_perm(self):
        self.load_faces()
        instructions = ""
        if self.is_solved(): return '' 
        if most_repeated_count(self.front_face) == 4:
            if self.cube.face_colors[5] != self.cube.face_colors[4]:
                instructions = "BUbubRBBubuBUbr"
                print('1,1')
            else:
                instructions = 'BDbdbLBBdbdBDbl'
                print('1,2')

        elif most_repeated_count(self.right_face) == 4:
            if self.cube.face_colors[0] != self.cube.face_colors[1]:
                instructions = "LUlulBLLuluLUlb"
                print('2,1')
            else:
                instructions = 'LDldlFLLdldLUlf'
                print('2,2')
            
        elif most_repeated_count(self.back_face) == 4:
            if self.cube.face_colors[20] != self.cube.face_colors[21]:
                instructions = "FUfufLFFufuFUfl"
                print('3,1')
            else:
                instructions = 'FDfdfRFFdfdFDfr'
                print('3,2')
            
        elif most_repeated_count(self.left_face) == 4:
            if self.cube.face_colors[0] != self.cube.face_colors[1]:
                instructions = "RUrurFRRuruRUrf"
                print('4,1')
            else:
                instructions = "RDrdrBRRdrdRDrb"
                print('4,2')                

        return instructions

    def algorithm_4(self):
            self.load_faces()
            instructions = ""
            if self.is_solved(): return '' 
            if most_repeated_count(self.front_face) == 4:
                if self.cube.face_colors[5] != self.cube.face_colors[4]:
                    instructions = "BUbubRBBubuBUbr"
                    print('1,1')

            elif most_repeated_count(self.right_face) == 4:
                if self.cube.face_colors[0] != self.cube.face_colors[1]:
                    instructions = "LUlulBLLuluLUlb"
                    print('2,1')
                
            elif most_repeated_count(self.back_face) == 4:
                if self.cube.face_colors[20] != self.cube.face_colors[21]:
                    instructions = "FUfufLFFufuFUfl"
                    print('3,1')
                
            elif most_repeated_count(self.left_face) == 4:
                if self.cube.face_colors[0] != self.cube.face_colors[1]:
                    instructions = "RUrurFRRuruRUrf"
                    print('4,1')                

            return instructions

    def pbl(self):
        if self.is_solved(): return ''
        counts = []
        for _ in range(4):
            self.load_faces()
            counts.append(max_counts([self.front_face, self.right_face, self.back_face, self.left_face]))
            self.cube.turn_top_clockwise()
            if self.is_solved(): return ''
        x = find_first_occurrence(counts, 4)
        if x != -1:
            for _ in range(x):
                self.cube.turn_top_clockwise()
            y = counts[x]
            y.remove(4)
            print(y)
            if y == [2,2,2]:
                print('option 4')
                return self.algorithm_4()
            else:
                print('option 1 ')
                return self.t_perm()
        x = find_first_occurrence(counts, 3)
        if x != -1: 
            for _ in range(x):
                self.cube.turn_top_clockwise()       
            if counts[x] == [3,3,3,3]:
                print('y-perm')
            else:
                print('option 5')
        else: print('option 3')
        return ''
        
        #return self.recognize_algorithms_pbl()

