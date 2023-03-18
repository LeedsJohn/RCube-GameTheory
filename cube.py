# John Leeds
# 3/18/2023
# cube.py
# Rubik's Cube class to interact with Herbert Kociemba's 2x2x2 solver

class Cube:
    # Representation of the cube (taken from Herbert Kociemba's enums.py)
    """""
    The names of the facelet positions of the cube
              |********|
              |*U1**U2*|
              |********|
              |*U3**U4*|
              |********|
     |********|********|********|********|
     |*L1**L2*|*F1**F2*|*R1**R2*|*B1**B2*|
     |********|********|********|********|
     |*L3**L4*|*F3**F4*|*R3**R4*|*B3**B4*|
     |********|********|********|********|
              |********|
              |*D1**D2*|
              |********|
              |*D3**D4*|
              |********|
     
    A cube definition string "UBL..." means for example: In position U1 we have the U-color, in position U2 we have the
    B-color, in position U3 we have the L color etc. according to the order U1, U2, U3, U4, R1, R2, R3, R4, F1, F2, F3,
    F4, D1, D2, D3, D4, L1, L2, L3, L4, B1, B2, B3, B4 of the enum constants.
    """
    def __init__(self):
        self.cube = []
        for side in "URFDLB":
            self.cube.extend([side] * 4)

    def scramble(self):
        """
        Scrambles the Rubik's Cube with random moves.
        """
        return

    def move(self, rotations: str) -> None:
        """
        Receives a string of rotations and applies the rotations to the cube.
        """
        return
    
    def __parse_scramble(self, scramble: str) -> [str]:
        """
        Receives a scramble
        Returns a list of each individual move in common notation.
        Ex: "R U R' U'" -> ["R", "U", "R'", "U'"]
        """
        return
    
    def __rotate(self, rotation: str) -> None:
        """
        Receives a string representing one move to the Rubik's Cube.
        Applies the move to the cube.
        """
        return
    
    def __str__(self) -> None:
        """
        Overload to print visual representation of the Rubik's Cube
        """
