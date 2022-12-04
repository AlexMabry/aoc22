from aocd import models
from src.utils import parse_data

# create puzzle
puzzle = models.Puzzle(year=2022, day=3)

# format data
input_data = parse_data(puzzle.input_data)


############################
# Solve puzzle
numbers = [[ord(c) - (96 if c.islower() else 38) for c in row] for row in input_data]
compartments = [[set(n[:len(n)//2]), set(n[len(n)//2:])] for n in numbers]
priorities = [set.intersection(*c).pop() for c in compartments]

answer_to_submit = sum(priorities)
############################

# submit answer
puzzle.answer_a = answer_to_submit
