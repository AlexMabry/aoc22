from aocd import models
from src.utils import parse_data

# create puzzle
puzzle = models.Puzzle(year=2022, day=13)

# format data
input_data = parse_data(puzzle.input_data)
# input_data = parse_data(puzzle.example_data)

############################
# Solve puzzle
p_iter = iter([eval(packet) for packet in input_data if packet])

def compare(l, r):
    if (llist := isinstance(l, list)) != (rlist := isinstance(r, list)):
        return compare(l if llist else [l], r if rlist else [r])
    elif llist:
        while l and r:
            if (res := compare(l[0], r[0])) != 0:
                return res
            l, r = l[1:], r[1:]

        return 0 if not l and not r else -1 if not l else 1
    else:
        return -1 if l < r else 1 if l > r else 0

results = [compare(left, right) for left, right in zip(p_iter, p_iter)]

answer_to_submit = sum([pos+1 for pos, result in enumerate(results) if result == -1])
############################

# submit answer
puzzle.answer_a = answer_to_submit
