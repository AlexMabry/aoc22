from aocd import models
from src.utils import parse_data

# create puzzle
puzzle = models.Puzzle(year=2022, day=17)

# format data
# input_data = parse_data(puzzle.input_data)
input_data = parse_data(puzzle.example_data)

############################
# Solve puzzle
print(input_data)

answer_to_submit = None
############################

# submit answer
puzzle.answer_a = answer_to_submit
