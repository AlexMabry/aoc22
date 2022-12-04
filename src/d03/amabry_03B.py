from aocd import models
from src.utils import parse_data

# create puzzle
puzzle = models.Puzzle(year=2022, day=3)

# format data
input_data = parse_data(puzzle.input_data)

############################
# Solve puzzle
numbers = [[ord(c) - (96 if c.islower() else 38) for c in row] for row in input_data]
groups = [[set(numbers[n+r]) for r in range(3)] for n in range(0, len(numbers), 3)]
badges = [set.intersection(*g).pop() for g in groups]

answer_to_submit = sum(badges)
############################

# submit answer
puzzle.answer_b = answer_to_submit
