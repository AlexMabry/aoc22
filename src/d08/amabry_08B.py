from itertools import takewhile

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

def count_trees(h, view):
    seen = 0
    for tree in view:
        seen += 1
        if tree >= h:
            break

    return seen

def count_all_trees():
    for y in range(trees.shape[1]):
        for x in range(trees.shape[0]):
            vis[y, x] = count_trees(trees[y, x], np.flip(trees[:y, x]))
            vis[y, x] *= count_trees(trees[y, x], trees[y+1:, x])
            vis[y, x] *= count_trees(trees[y, x], np.flip(trees[y, :x]).flatten())
            vis[y, x] *= count_trees(trees[y, x], trees[y, x+1:].flatten())

count_all_trees()

answer_to_submit = np.max(vis)
############################

# submit answer
puzzle.answer_b = answer_to_submit
