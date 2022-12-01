from aocd import models
from src.utils import parse_data

# create puzzle
puzzle = models.Puzzle(year=2022, day=1)

# format data
input_data = parse_data(puzzle.input_data)

############################
# Solve puzzle
calories = [0]
for row in input_data:
    if row == '':
        calories.append(0)
    else:
        calories[-1] += int(row)

answer_to_submit = sum(sorted(calories)[-3:])
############################

# submit answer
puzzle.answer_b = answer_to_submit
