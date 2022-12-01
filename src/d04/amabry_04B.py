from aocd import models
from src.utils import parse_data

# create puzzle
puzzle = models.Puzzle(year=2022, day=4)

# format data
input_data = parse_data(puzzle.input_data)

############################
# Solve puzzle
print(input_data)

answer_to_submit = None
############################

# submit answer
puzzle.answer_b = answer_to_submit
