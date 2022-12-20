import re
from collections import deque
from dataclasses import dataclass, astuple

from aocd import models
from src.utils import parse_data

# create puzzle
puzzle = models.Puzzle(year=2022, day=19)

# format data
input_data = parse_data(puzzle.input_data)

############################
# Solve puzzle
pattern = re.compile(r'Blueprint (?P<id>\d+): Each ore robot costs (?P<ore_ore>\d+) ore. Each clay robot costs (?P<clay_ore>\d+) ore. Each obsidian robot costs (?P<obs_ore>\d+) ore and (?P<obs_clay>\d+) clay. Each geode robot costs (?P<geo_ore>\d+) ore and (?P<geo_obs>\d+) obsidian.')
matches = [pattern.match(cmd).groupdict() for cmd in input_data]

blueprints = {int(m['id']): {k: int(v) for k, v in m.items() if k != 'id'} for m in matches}

@dataclass(frozen=True, unsafe_hash=True)
class RS:
    ore: int = 0
    clay: int = 0
    obsidian: int = 0
    geode: int = 0

    def __add__(self, other):
        return RS(*[a + b for a, b in zip(astuple(self), astuple(other))])

    def __sub__(self, other):
        return RS(*[a - b for a, b in zip(astuple(self), astuple(other))])

    def __ge__(self, other):
        return all(a >= b for a, b in zip(astuple(self), astuple(other)))

def get_most_geodes(cost: dict):
    q = deque([(RS(), RS(ore=1), 24)])
    skip = set()
    best = 0

    max_rs = RS(ore=max([c.ore for c in cost.values()]),
                clay=max([c.clay for c in cost.values()]),
                obsidian=max([c.obsidian for c in cost.values()]),
                geode=1000)

    # Heavily inspired by Jonathan Paulson's solution:
    #   https://github.com/jonathanpaulson/AdventOfCode/blob/master/2022/19.py

    while q:
        rs, rb, ticks = q.popleft()
        best = max(best, rs.geode)

        # We are done
        if ticks == 0:
            continue

        # too many robots -- off track
        if rb.ore > max_rs.ore or rb.clay > max_rs.clay or rb.obsidian > max_rs.obsidian:
            continue

        # trim unneeded resources to save time
        rs = RS(
            ore=min(rs.ore, ticks*max_rs.ore-(ticks-1)*rb.ore),
            clay=min(rs.clay, ticks*max_rs.clay-(ticks-1)*rb.clay),
            obsidian=min(rs.obsidian, ticks*max_rs.obsidian-(ticks-1)*rb.obsidian),
            geode=rs.geode
        )

        # Skip if we have already seen this state to save time
        if (rs, rb, ticks) in skip:
            continue

        skip.add((rs, rb, ticks))

        if rs >= cost['geode']:  # Buy geode robot
            q.append((rs+rb-cost['geode'], rb+RS(geode=1), ticks-1))
        if rs >= cost['obsidian']:  # Buy obsidian robot
            q.append((rs+rb-cost['obsidian'], rb+RS(obsidian=1), ticks-1))
        if rs >= cost['clay']:  # Buy clay robot
            q.append((rs+rb-cost['clay'], rb+RS(clay=1), ticks-1))
        if rs >= cost['ore']:  # Buy ore robot
            q.append((rs+rb-cost['ore'], rb+RS(ore=1), ticks-1))
        q.append((rs+rb, rb, ticks-1))

    return best


answer_to_submit = 0
for bid, b in blueprints.items():
    robot_cost = {
        'ore': RS(ore=b['ore_ore']),
        'clay': RS(ore=b['clay_ore']),
        'obsidian': RS(ore=b['obs_ore'], clay=b['obs_clay']),
        'geode': RS(ore=b['geo_ore'], obsidian=b['geo_obs'])
    }
    bp_high = get_most_geodes(robot_cost)
    print(f'Blueprint {bid}: {bp_high}')

    answer_to_submit += bid * bp_high
############################

# submit answer
puzzle.answer_a = answer_to_submit
