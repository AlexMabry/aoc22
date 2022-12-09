from aocd import models
from src.utils import parse_data
import numpy as np

# create puzzle
puzzle = models.Puzzle(year=2022, day=8)

# format data
input_data = parse_data(puzzle.input_data)
# input_data = parse_data(puzzle.example_data)

############################
# Solve puzzle
trees = np.array([np.array([int(n) for n in row]) for row in input_data])
vis = np.zeros(trees.shape, dtype=int)

def look_for_tree(tallest, x, y):
    if trees[x, y] > tallest:
        vis[x, y] = 1
    return max(tallest, trees[x, y])


for x in range(trees.shape[0]):
    max_tree = -1
    for y in range(trees.shape[1]):
        max_tree = look_for_tree(max_tree, x, y)

    max_tree = -1
    for y in range(trees.shape[1] - 1, -1, -1):
        max_tree = look_for_tree(max_tree, x, y)

for y in range(trees.shape[1]):
    max_tree = -1
    for x in range(trees.shape[0]):
        max_tree = look_for_tree(max_tree, x, y)

    max_tree = -1
    for x in range(trees.shape[0] - 1, -1, -1):
        max_tree = look_for_tree(max_tree, x, y)

answer_to_submit = vis.sum()
############################

# submit answer
puzzle.answer_a = answer_to_submit
