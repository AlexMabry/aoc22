import numpy as np
from aocd import models
from src.utils import parse_data

# create puzzle
puzzle = models.Puzzle(year=2022, day=9)

# format data
input_data = parse_data(puzzle.input_data)

############################
# Solve puzzle
delta = {"R": (1, 0), "L": (-1, 0), "U": (0, 1), "D": (0, -1)}
moves = [np.array(delta[x[0]], dtype=int) for x in input_data for _ in range(int(x[2:]))]
tails = np.zeros((9, 2), dtype=int)
positions = set()

for h in np.cumsum(moves, axis=0):
    for i in range(9):
        diff = (h if not i else tails[i - 1]) - tails[i]
        if np.max(np.abs(diff)) >= 2:
            tails[i] += np.sign(diff)
    positions.add(tuple(tails[8]))

answer_to_submit = len(positions)
############################

# submit answer
puzzle.answer_b = answer_to_submit
