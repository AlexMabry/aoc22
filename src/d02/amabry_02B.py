from aocd import models
from src.utils import parse_data

# create puzzle
puzzle = models.Puzzle(year=2022, day=2)

# format data
input_data = parse_data(puzzle.input_data)

############################
score = {
    ('B', 'X'): 1,
    ('C', 'X'): 2,
    ('A', 'X'): 3,
    ('A', 'Y'): 4,
    ('B', 'Y'): 5,
    ('C', 'Y'): 6,
    ('C', 'Z'): 7,
    ('A', 'Z'): 8,
    ('B', 'Z'): 9,
}

answer_to_submit = sum([score[tuple(row.split(' '))] for row in input_data])
############################

# submit answer
puzzle.answer_b = answer_to_submit
