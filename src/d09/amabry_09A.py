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
T = np.zeros(2, dtype=int)
positions = set()

for h in np.cumsum(moves, axis=0):
    diff = h - T
    if np.max(np.abs(diff)) >= 2:
        T += np.sign(diff)
    positions.add(tuple(T))

answer_to_submit = len(positions)
############################

# submit answer
puzzle.answer_a = answer_to_submit
