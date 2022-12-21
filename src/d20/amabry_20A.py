from dataclasses import dataclass
from itertools import pairwise

from aocd import models
from src.utils import parse_data

# create puzzle
puzzle = models.Puzzle(year=2022, day=20)

# format data
input_data = parse_data(puzzle.input_data)

############################
# Solve puzzle
@dataclass
class LinkedNode:
    value : int
    next : "LinkedNode" = None
    prev : "LinkedNode" = None

class CircularLinkedList:
    def __init__(self, values):
        self.nodes = {ix: LinkedNode(x) for ix, x in enumerate(values)}
        self.length = len(values)

        for a, b in pairwise([*range(len(values)), 0]):
            self.nodes[a].next = self.nodes[b]
            self.nodes[b].prev = self.nodes[a]

    def mix(self):
        for n in range(self.length):
            node = self.nodes[n]

            # remove node
            node.prev.next = node.next
            node.next.prev = node.prev

            after = node.prev
            for _ in range(abs(node.value) % (self.length - 1)):
                after = after.next if node.value > 0 else after.prev

            # insert node
            node.next = after.next
            node.prev = after
            after.next.prev = node
            after.next = node

    def value_after_zero(self, places):
        # find node with value 0
        node = self.nodes[0]
        while node.value != 0:
            node = node.next

        for _ in range(places % self.length):
            node = node.next
        return node.value

clist = CircularLinkedList([int(n) for n in input_data])
clist.mix()

answer_to_submit = sum(clist.value_after_zero(n*1000) for n in range(1, 4))
############################

# submit answer
puzzle.answer_a = answer_to_submit
