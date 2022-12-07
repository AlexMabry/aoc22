import re
from typing import Optional

from aocd import models
from src.utils import parse_data
from dataclasses import dataclass, field

# create puzzle
puzzle = models.Puzzle(year=2022, day=7)

# format data
input_data = parse_data(puzzle.input_data)

############################
# Solve puzzle
@dataclass
class Directory:
    parent: Optional['Directory'] = None
    children: dict['Directory'] = field(default_factory=lambda: dict())
    file_size: int = 0

    @property
    def size(self):
        return self.file_size + sum([child.size for child in self.children.values()])

dirs = [Directory()]

for cmd in input_data:
    match re.match(r"\$ cd (?P<cd>.*)|\$ ls|dir (?P<dir>.*)|(?P<size>\d+) .*", cmd).groupdict():
        case {"cd": '/'}:
            cwd = dirs[0]
        case {"cd": '..'}:
            cwd = cwd.parent
        case {"cd": dir_name} if dir_name:
            cwd = cwd.children[dir_name]
        case {"dir": dir_list} if dir_list:
            cwd.children[dir_list] = Directory(parent=cwd)
            dirs.append(cwd.children[dir_list])
        case {"size": size} if size:
            cwd.file_size += int(size)

answer_to_submit = sum([d.size for d in dirs if d.size <= 100000])
############################

# submit answer
puzzle.answer_a = answer_to_submit
