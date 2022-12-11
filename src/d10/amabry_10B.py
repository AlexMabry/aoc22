import re

import numpy as np
from aocd import models
from src.utils import parse_data

# create puzzle
puzzle = models.Puzzle(year=2022, day=10)

# format data
input_data = parse_data(puzzle.input_data)

############################
# Solve puzzle
register = np.array([0, 1], dtype=int)

for cmd in input_data:
    match re.match(r"(?P<noop>noop).*|addx (?P<addx>[-0-9]+)", cmd).groupdict():
        case {"noop": noop} if noop:
            register = np.append(register, [0])
        case {"addx": addx}:
            register = np.append(register, [int(addx), 0])

for cycle, val in enumerate(np.cumsum(register)):
    pos = cycle % 40
    print("###" if pos-1 <= val <= pos+1 else "   ", end="")
    if pos == 39:
        print()

answer_to_submit = None
############################

# submit answer
puzzle.answer_b = answer_to_submit
