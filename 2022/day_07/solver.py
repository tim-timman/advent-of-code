from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import PurePath


@dataclass
class File:
    path: PurePath
    size: int


@dataclass
class Dir:
    path: PurePath
    size: int = 0
    contents: dict[PurePath, Dir | File] = field(default_factory=dict)


def construct_file_system(input_str: str):
    root = Dir(PurePath("/"))
    directories = {root.path: root}
    dir_stack = []
    for line in input_str.splitlines():
        match line.split():
            case ["$", "cd", arg]:
                if arg == "..":
                    dir_stack.pop()
                elif arg == "/":
                    dir_stack = [root]
                else:
                    path = dir_stack[-1].path / arg
                    # if path not in directories:
                    #     directories[path] = Dir(path)
                    dir_stack.append(directories[path])
            case ["dir", name]:
                path = dir_stack[-1].path / name
                if path not in directories:
                    directories[path] = dir_stack[-1].contents[path] = Dir(path)
            case [str(size), name] if size.isnumeric():
                f = File(dir_stack[-1].path / name, int(size))
                dir_stack[-1].contents[f.path] = f
                for d in dir_stack:
                    d.size += f.size

    return directories


TOTAL_SPACE = 70000000
MIN_REQUIRED = 30000000


def solve(puzzle_input: str) -> tuple[int, int | None]:
    directories = construct_file_system(puzzle_input)
    answer_part_1 = sum(d.size for d in directories.values() if d.size <= 100000)

    root_size = directories[PurePath("/")].size
    answer_part_2 = next(size for size in sorted(d.size for d in directories.values())
                         if TOTAL_SPACE - root_size + size >= MIN_REQUIRED)

    return answer_part_1, answer_part_2


TEST_EXPECTED = (95437, None)
TEST_INPUT = """\
$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k
"""
