# John Leeds
# 3/18/2023
# cube.py
# Rubik's Cube class to interact with Herbert Kociemba's 2x2x2 solver
import random
import hkociembasolver.solver as sv
from rotations import *


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

    def scramble(self, moves = 100):
        """
        Scrambles the Rubik's Cube with random moves.
        """
        for _ in range(moves):
            direction = random.choice("RUFLDB")
            for i in range(random.randrange(1, 4)):
                self.move(direction)

    def get_distance(self) -> int:
        """
        Returns the number of moves it takes to solve the cube in its
        current state.
        """
        solution = sv.solve(self.get_cubestring())
        paren = "()"[0] # my editor was doing weird things with parenthesis
        start, end = solution.find(paren), solution.find("f")
        return int(solution[start + 1:end])

    def get_solution(self) -> [str]:
        """
        Returns an optimal solution to the cube
        """
        solution = sv.solve(self.get_cubestring())
        paren = "()"[0] # same as above, typing open paren does weird things
        return solution[:solution.find(paren)]

    def move(self, rotations: str) -> None:
        """
        Receives a string of rotations and applies the rotations to the cube.
        """
        moves = self.__parse_scramble(rotations)
        for move in moves:
            self.__rotate(move)

    def is_solved(self) -> bool:
        """
        Returns true if the cube is solved.
        """
        for i in range(0, 24, 4):
            if len(set(self.cube[i:i + 4])) != 1:
                return False
        return True

    def get_cubestring(self) -> str:
        """
        Returns a cubestring to be used with the solver
        """
        return "".join(self.cube)
    
    def __parse_scramble(self, scramble: str) -> [str]:
        """
        Receives a scramble
        Returns a list of each individual move in common notation.
        Ex: "R U R' U'" -> ["R", "U", "R'", "U'"]
        """
        res = []
        for i, c in enumerate(scramble[:-1]):
            if c in "RUFLDB": # valid moves
                # apply rotation once for clockwise, twice for double move,
                # three times for counterclockwise rotation
                res.append(c)
                if scramble[i + 1] in "2'":
                    res.append(c)
                if scramble[i + 1] == "'":
                    res.append(c)
        if scramble[-1] in "RUFLDB":
            res.append(scramble[-1])
        return res
    
    def __rotate(self, rotation: str) -> None:
        """
        Receives a string representing one move to the Rubik's Cube.
        Applies the move to the cube.
        """
        for pattern in ROTATIONS[rotation].patterns:
            temp = self.cube[pattern[3]]
            for i in range(3, 0, -1):
                self.cube[pattern[i]] = self.cube[pattern[i - 1]]
            self.cube[pattern[0]] = temp
    
    def __str__(self) -> None:
        """
        Overload to print visual representation of the Rubik's Cube
        """
        # please forgive my lazy programming. At least most of it what copy / pasted
        # print order
        po = [
                0, 1, 2, 3,
                16, 17, 8, 9, 4, 5, 20, 21, 18, 19, 10, 11, 6, 7, 22, 23,
                12, 13, 14, 15
                ]
        res = []
        res.append(f"{' ' * 9}-----")
        res.append(f"{' ' * 8}| {self.cube[po[0]]} {self.cube[po[1]]} |")
        res.append(f"{' ' * 8}| {self.cube[po[2]]} {self.cube[po[3]]} |")
        res.append(f"{' ' * 9}-----")
        res.append(" -----   -----   -----   -----")
        for i in [4, 12]:
            res.append(f"| {self.cube[po[i]]} {self.cube[po[i + 1]]} | | {self.cube[po[i + 2]]} {self.cube[po[i + 3]]} | | {self.cube[po[i + 4]]} {self.cube[po[i + 5]]} | | {self.cube[po[i + 6]]} {self.cube[po[i + 7]]} |")
        res.append(" -----   -----   -----   -----")
        res.append(f"{' ' * 9}-----")
        res.append(f"{' ' * 8}| {self.cube[po[20]]} {self.cube[po[21]]} |")
        res.append(f"{' ' * 8}| {self.cube[po[22]]} {self.cube[po[23]]} |")
        res.append(f"{' ' * 9}-----")
        return "\n".join(res)

john = Cube()
john.scramble()
john.get_solution()
