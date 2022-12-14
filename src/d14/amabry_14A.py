from itertools import pairwise, product

from aocd import models
from src.utils import parse_data

# create puzzle
puzzle = models.Puzzle(year=2022, day=14)

# format data
input_data = parse_data(puzzle.input_data)

############################
# Solve puzzle
endpoints = [[tuple(int(n) for n in pair.split(',')) for pair in row.split(' -> ')] for row in input_data]
paths = [pair for points in endpoints for pair in pairwise(points)]
rocks = {pd for path in paths for pd in product(*[{n for n in range(min(p), max(p) + 1)} for p in zip(*path)])}
max_depth = max(r[1] for r in rocks)
sand = set()

def move_grain(g):
    moves = [(g[0], g[1]+1), (g[0]-1, g[1]+1), (g[0]+1, g[1]+1)]
    return next((m for m in moves if g[1] < max_depth and m not in sand and m not in rocks), None)

grain = (500, 0)
while grain[1] < max_depth:
    while new_pos := move_grain(grain):
        grain = new_pos

    if grain[1] < max_depth:
        sand.add(grain)
        grain = (500, 0)

answer_to_submit = len(sand)
############################

# submit answer
puzzle.answer_a = answer_to_submit
