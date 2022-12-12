from dataclasses import dataclass
from math import prod

from aocd import models

# create puzzle
puzzle = models.Puzzle(year=2022, day=11)

############################
@dataclass
class Monkey:
    items: list[int]
    operation: lambda x: int
    divisible: int
    target: dict[bool, int]
    count: int = 0

    def test(self) -> tuple[int, int]:
        self.count += 1
        inspected = self.operation(self.items.pop(0)) % 9699690
        return self.target[not inspected % self.divisible], inspected

monkeys = {
    0: Monkey([50, 70, 54, 83, 52, 78], lambda x: x * 3, 11, {True: 2, False: 7}),
    1: Monkey([71, 52, 58, 60, 71], lambda x: x * x, 7, {True: 0, False: 2}),
    2: Monkey([66, 56, 56, 94, 60, 86, 73], lambda x: x + 1, 3, {True: 7, False: 5}),
    3: Monkey([83, 99], lambda x: x + 8, 5, {True: 6, False: 4}),
    4: Monkey([98, 98, 79], lambda x: x + 3, 17, {True: 1, False: 0}),
    5: Monkey([76], lambda x: x + 4, 13, {True: 6, False: 3}),
    6: Monkey([52, 51, 84, 54], lambda x: x * 17, 19, {True: 4, False: 1}),
    7: Monkey([82, 86, 91, 79, 94, 92, 59, 94], lambda x: x + 7, 2, {True: 5, False: 3}),
}

for r in range(10000):
    for m in monkeys.values():
        while m.items:
            monkey, item = m.test()
            monkeys[monkey].items.append(item)

answer_to_submit = prod(sorted([m.count for m in monkeys.values()])[-2:])
############################

# submit answer
puzzle.answer_b = answer_to_submit
