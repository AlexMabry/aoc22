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

values = np.cumsum(register) * np.arange(1, len(register)+1)

answer_to_submit = int(sum([values[r] for r in range(19, len(values), 40)]))
############################

# submit answer
puzzle.answer_a = answer_to_submit
