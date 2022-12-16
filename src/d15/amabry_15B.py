import re
from typing import Optional, Iterable

import numpy as np
from scipy.spatial.distance import cityblock
from aocd import models
from src.utils import parse_data

# create puzzle
puzzle = models.Puzzle(year=2022, day=15)

# format data
input_data = parse_data(puzzle.input_data)
# input_data = parse_data(puzzle.example_data)

############################
# Solve puzzle
pattern = re.compile(r'Sensor at x=(?P<x1>[-\d]+), y=(?P<y1>[-\d]+): closest beacon is at x=(?P<x2>[-\d]+), y=(?P<y2>[-\d]+)')
matches = [pattern.match(cmd).groupdict() for cmd in input_data]
sensors = [np.array([int(m['y1']), int(m['x1'])]) for m in matches]
beacons = [np.array([int(m['y2']), int(m['x2'])]) for m in matches]
distances = [cityblock(s, b) for s, b in zip(sensors, beacons)]
max_line = 4000000

def whats_missing(line) -> Optional[int]:
    merged = []
    for r in sorted(((max(0, s[1] - w), min(s[1] + w, max_line)) for s, d in zip(sensors, distances) if
     (w := d - abs(s[0] - line)) >= 0)):
        if not merged:
            merged.append(r)
        else:
            prev_start, prev_end = merged[-1]
            curr_start, curr_end = r
            if prev_end >= curr_start - 1:
                merged[-1] = (prev_start, max(prev_end, curr_end))
            else:
                merged.append(r)

        if len(merged) == 1 and merged[0][1] - merged[0][0] == max_line:
            return None

    return merged[1][0]-1

answer_to_submit = next(missing*max_line+line for line in range(max_line) if (missing := whats_missing(line)) is not None)
############################

# submit answer
puzzle.answer_b = answer_to_submit
