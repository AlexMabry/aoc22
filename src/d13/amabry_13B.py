from aocd import models
from src.utils import parse_data
from functools import cmp_to_key

# create puzzle
puzzle = models.Puzzle(year=2022, day=13)

# format data
input_data = parse_data(puzzle.input_data)

############################
# Solve puzzle
packets = [eval(packet) for packet in input_data if packet]
packets.append([[2]])
packets.append([[6]])

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

ordered = list(sorted(packets, key=cmp_to_key(compare)))

answer_to_submit = (ordered.index([[2]])+1) * (ordered.index([[6]])+1)
############################

# submit answer
puzzle.answer_b = answer_to_submit
