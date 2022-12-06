from aocd import models
from src.utils import parse_data

# create puzzle
puzzle = models.Puzzle(year=2022, day=6)

# format data
input_data = parse_data(puzzle.input_data)[0]
# input_data = parse_data(puzzle.example_data)[0]

############################
# Solve puzzle
marker = 4
for i in range(len(input_data)-marker):
    if len(set(input_data[i:i+marker])) == marker:
        break

answer_to_submit = i+marker
############################

# submit answer
puzzle.answer_a = answer_to_submit
