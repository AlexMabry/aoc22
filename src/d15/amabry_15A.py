import re

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

LINE = 2_000_000
close_sensors = [range(s[1] - w, s[1] + w + 1) for s, d in zip(sensors, distances) if (w := d - abs(s[0]-LINE)) >= 0]
taken = {x for sensor_range in close_sensors for x in sensor_range}

answer_to_submit = len(taken - {x for [y, x] in beacons if y == LINE})
############################

# submit answer
puzzle.answer_a = answer_to_submit
