import re
from collections import defaultdict, deque

from aocd import models
from src.utils import parse_data

# create puzzle
puzzle = models.Puzzle(year=2022, day=5)

# format data
input_data = parse_data(puzzle.input_data)

############################
# Solve puzzle
# find the top rows
input_row = 0
top = []
while input_data[input_row]:
    top.append(input_data[input_row])
    input_row += 1

# populate the stacks
stacks = defaultdict(deque)
for level in range(input_row - 2, -1, -1):
    for col in range(1, 10):
        if top[level][col*4-3] != ' ':
            stacks[col].append(top[level][col * 4 - 3])

# skip empty line
input_row += 1

# read the moves
moves = []
pattern = re.compile(r'move ([0-9]+) from ([1-9]) to ([1-9]+)')
for r in range(input_row, len(input_data)):
    moves.append([int(n) for n in pattern.search(input_data[r]).groups()])

# perform the moves
for num_to_move, from_stack, to_stack in moves:
    to_move = deque([stacks[from_stack].pop() for _ in range(num_to_move)])
    stacks[to_stack].extend(reversed(to_move))

# get answer
answer_to_submit = ''.join(stack.pop() for col, stack in stacks.items())
############################

# submit answer
puzzle.answer_b = answer_to_submit
