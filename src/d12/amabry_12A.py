import numpy as np
from aocd import models
from src.utils import parse_data
import networkx as nx

# create puzzle
puzzle = models.Puzzle(year=2022, day=12)

# format data
input_data = parse_data(puzzle.input_data)

############################
# Solve puzzle
nodes = np.array([np.array([(ord(char)-ord('a')) if char >= 'a' else -1 if char == 'S' else 26 for x, char in enumerate(row)]) for y, row in enumerate(input_data)])

start = end = (-1, -1)
for y, row in enumerate(input_data):
    for x, char in enumerate(row):
        if char == "S":
            start = np.ravel_multi_index((y, x), nodes.shape)
        elif char == "E":
            end = np.ravel_multi_index((y, x), nodes.shape)

# Create adjacency matrix
adj = np.zeros((nodes.size, nodes.size))
for y in range(nodes.shape[0]):
    for x in range(nodes.shape[1]):
        step_limit = nodes[y, x]+1
        i = np.ravel_multi_index((y, x), nodes.shape)

        if x > 0:
            adj[i, i-1] = 1 if nodes[y, x-1] <= step_limit else 0
        if x < nodes.shape[1]-1:
            adj[i, i+1] = 1 if nodes[y, x+1] <= step_limit else 0
        if y > 0:
            adj[i, i-nodes.shape[1]] = 1 if nodes[y-1, x] <= step_limit else 0
        if y < nodes.shape[0]-1:
            adj[i, i+nodes.shape[1]] = 1 if nodes[y+1, x] <= step_limit else 0

G = nx.from_numpy_matrix(adj, parallel_edges=False, create_using=nx.DiGraph)

answer_to_submit = nx.shortest_path_length(G, start, end)
############################

# submit answer
puzzle.answer_a = answer_to_submit
