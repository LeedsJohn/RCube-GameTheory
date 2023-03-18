import random
import cube

def smartVrandom(n = 2):
    rcube = cube.Cube()
    rcube.scramble()
    count = 1
    while True:
        solution = rcube.get_solution()
        solution = solution.split()
        if len(solution) < n:
            solution = "".join(solution)
        else:
            solution = "".join(solution[:n])
        rcube.move(solution)
        if rcube.is_solved():
            return count

        count += 1
        prev = ""
        moves = "RUFLDB"
        for i in range(n):
            while True:
                rotation = random.choice(moves)
                if rotation != prev:
                    break
            prev = rotation
            for _ in range(1, random.randrange(4)):
                rcube.move(rotation)
        if rcube.is_solved():
            return count
        count += 1
