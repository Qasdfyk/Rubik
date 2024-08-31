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
            else:
                instructions = 'BDbdbLBBdbdBDbl'
        elif most_repeated_count(self.right_face) == 4:
            if self.cube.face_colors[0] != self.cube.face_colors[1]:
                instructions = "LUlulBLLuluLUlb"
            else:
                instructions = 'LDldlFLLdldLUlf'           
        elif most_repeated_count(self.back_face) == 4:
            if self.cube.face_colors[20] != self.cube.face_colors[21]:
                instructions = "FUfufLFFufuFUfl"
            else:
                instructions = 'FDfdfRFFdfdFDfr'        
        elif most_repeated_count(self.left_face) == 4:
            if self.cube.face_colors[0] != self.cube.face_colors[1]:
                instructions = "RUrurFRRuruRUrf"
            else:
                instructions = "RDrdrBRRdrdRDrb"              
        return instructions

    def algorithm_4(self):
            self.load_faces()
            instructions = ""
            if self.is_solved(): return '' 
            if most_repeated_count(self.front_face) == 4:
                instructions = "LLuLLUUBBuLL"

            elif most_repeated_count(self.right_face) == 4:
                instructions = "FFuFFUULLuFF"
            
            elif most_repeated_count(self.back_face) == 4:
                instructions = "RRuRRUUFFuRR"
                
            elif most_repeated_count(self.left_face) == 4:
                instructions = "BBuBBUUBBuBB"             
            return instructions
    
    def y_perm(self):
        instructions = ''
        if self.cube.face_colors[0] == self.cube.face_colors[1]:
            if self.cube.face_colors[0] == self.cube.face_colors[2]:
                instructions = 'BRdrdRDrbRDrdrBRb'
            else: 
                instructions = 'RFdfdFDfrFDfdfRFr'
        else:
            if self.cube.face_colors[0] == self.cube.face_colors[2]:
                instructions = 'FRuruRUrfRUrurFRf'
            else:
                instructions = 'LFufuFUflFUfufLFl'
        return instructions

    def algorithm_3(self):
        return 'RRFFRR'
    
    def algorithm_5(self):
        self.load_faces()
        instructions = "" 
        if most_repeated_count(self.front_face) == 3:
            if self.cube.face_colors[0] == self.cube.face_colors[1]:
                if self.cube.face_colors[3] != self.cube.face_colors[1]:
                    self.cube.turn_bottom_clockwise()
                    self.cube.turn_bottom_clockwise()
                instructions = 'RuRFFrUr'
            else:
                if self.cube.face_colors[3] != self.cube.face_colors[1]:
                    self.cube.turn_bottom_clockwise()
                    self.cube.turn_bottom_clockwise()
                instructions = "RdRBBrDr"

        elif most_repeated_count(self.right_face) == 3:
            if self.cube.face_colors[20] == self.cube.face_colors[21]:
                if self.cube.face_colors[23] != self.cube.face_colors[21]:
                    self.cube.turn_bottom_clockwise()
                    self.cube.turn_bottom_clockwise()
                instructions = 'BuBRRbUb'
            else:
                if self.cube.face_colors[23] != self.cube.face_colors[21]:
                    self.cube.turn_bottom_clockwise()
                    self.cube.turn_bottom_clockwise()
                instructions = 'BdBLLbDb'
        
        elif most_repeated_count(self.back_face) == 3:
            if self.cube.face_colors[5] == self.cube.face_colors[4]:
                if self.cube.face_colors[4] != self.cube.face_colors[6]:
                    self.cube.turn_bottom_clockwise()
                    self.cube.turn_bottom_clockwise()
                instructions = 'LuLBBlUl'
            else:
                if self.cube.face_colors[4] != self.cube.face_colors[6]:
                    self.cube.turn_bottom_clockwise()
                    self.cube.turn_bottom_clockwise()
                instructions = 'LdLFFlDl'
            
        elif most_repeated_count(self.left_face) == 3:
            if self.cube.face_colors[16] == self.cube.face_colors[17]:
                if self.cube.face_colors[17] != self.cube.face_colors[19]:
                    self.cube.turn_bottom_clockwise()
                    self.cube.turn_bottom_clockwise()
                instructions = 'FuFLLfUf'
            else:
                if self.cube.face_colors[17] != self.cube.face_colors[19]:
                    self.cube.turn_bottom_clockwise()
                    self.cube.turn_bottom_clockwise()
                instructions = 'FdFRRfDf'        
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
        y = find_first_occurrence(counts, 3)
        if x != -1:
            for _ in range(x):
                self.cube.turn_top_clockwise()
            y = counts[x]
            y.remove(4)
            if y == [2,2,2]:
                return self.algorithm_4()
            else:
                return self.t_perm() 
        elif y != -1: 
            for _ in range(y):
                self.cube.turn_top_clockwise()       
            if counts[y] == [3,3,3,3]:
                return self.y_perm()
            else:
                return self.algorithm_5()               
        else: 
            return self.algorithm_3()

