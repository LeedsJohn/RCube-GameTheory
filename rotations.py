# John Leeds
# 3/18/2023
# rotations.py
# Define rotation patterns

from hkociembasolver.enums import Facelet as Fc

class Rotation:
    def __init__(self, side, pattern, shift = 1):
        """
        Receives the side that rotates (for example, with an R rotation, every
        piece on the R face rotates clockwise)
        And a rotation pattern. Ex: for a right move: U2 -> B4 -> D2 -> F2
        Creates the move patterns which represent the indices that rotate
        """ 
        def nextPiece(val):
            # helper function to find the last rotation pattern
            facelet = val % 4
            start_point = val - facelet
            return start_point + (facelet + shift) % 4
            return val + shift if val % 4 != 3 else val - 3

        self.patterns = []
        self.patterns.append(list(range(side.value, side.value + 4)))
        self.patterns.append([facelet.value for facelet in pattern])
        self.patterns.append([nextPiece(self.patterns[-1][i]) for i in range(4)])


ROTATIONS = {
        "R": Rotation(Fc.R1, [Fc.U2, Fc.B4, Fc.D2, Fc.F2], 2),
        "U": Rotation(Fc.U1, [Fc.F1, Fc.L1, Fc.B1, Fc.R1]),
        "F": Rotation(Fc.F1, [Fc.U3, Fc.R3, Fc.D1, Fc.L2], 2),
        "L": Rotation(Fc.L1, [Fc.U1, Fc.F1, Fc.D1, Fc.B3], 2),
        "D": Rotation(Fc.D1, [Fc.F3, Fc.R3, Fc.B3, Fc.L3]),
        "B": Rotation(Fc.B1, [Fc.U1, Fc.L4, Fc.D3, Fc.R2])
        }
