from aocd import models
from src.utils import parse_data

# create puzzle
puzzle = models.Puzzle(year=2022, day=2)

# format data
input_data = parse_data(puzzle.input_data)

############################
score = {
    ('B', 'X'): 1,
    ('C', 'Y'): 2,
    ('A', 'Z'): 3,
    ('A', 'X'): 4,
    ('B', 'Y'): 5,
    ('C', 'Z'): 6,
    ('C', 'X'): 7,
    ('A', 'Y'): 8,
    ('B', 'Z'): 9,
}

answer_to_submit = sum([score[tuple(row.split(' '))] for row in input_data])
############################

# submit answer
puzzle.answer_a = answer_to_submit
