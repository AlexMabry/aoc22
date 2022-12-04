from aocd import models
from src.utils import parse_data

# create puzzle
puzzle = models.Puzzle(year=2022, day=4)

# format data
input_data = parse_data(puzzle.input_data, regex=r'([0-9]+)-([0-9]+),([0-9]+)-([0-9]+)')

############################
# Solve puzzle
numbers = [[int(n) for n in row] for row in input_data]
overlaps = [1 for (a, b, c, d) in numbers if (a <= c <= b) or (a <= d <= b) or (c <= a <= d) or (c <= b <= d)]

answer_to_submit = sum(overlaps)
############################

# submit answer
puzzle.answer_b = answer_to_submit
