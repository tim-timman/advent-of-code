from collections import deque
import re


def parse_stacks(stack_str: str) -> list[deque]:
    stack_lines = stack_str.splitlines()
    # Note: convert stack to stack index
    stack_map = {i: int(v) - 1 for i, v in enumerate(stack_lines[-1][1::4])}
    stacks: list[deque] = [deque() for _ in stack_map]

    for line in stack_lines[:-1]:
        for idx, char in enumerate(line[1::4]):
            if char != " ":
                stacks[stack_map[idx]].appendleft(char)

    return stacks


move_re = re.compile(r"^move (\d+) from (\d) to (\d)$", re.MULTILINE)


def parse_moves(move_str: str) -> list[tuple[int, int, int]]:
    # Note: convert stack to stack indices
    moves = [(int(m[0]), int(m[1]) - 1, int(m[2]) - 1)
             for m in move_re.findall(move_str)]
    return moves


def print_stacks(stacks: list[deque]):
    for idx, stack in enumerate(stacks):
        print(f"{idx + 1} ", *(f"[{v}]" for v in stack), sep="")
    print("---")


def solve(puzzle_input: str) -> tuple[str, str | None]:
    stack_str, _, move_str = puzzle_input.partition("\n\n")

    stacks = parse_stacks(stack_str)
    moves: list[tuple[int, int, int]] = parse_moves(move_str)

    for num, from_stack, to_stack in moves:
        for _ in range(num):
            stacks[to_stack].append(stacks[from_stack].pop())

    answer_part_1 = "".join(x[-1] for x in stacks)
    answer_part_2 = None
    return answer_part_1, answer_part_2


TEST_EXPECTED = ("CMZ", None)
TEST_INPUT = """\
    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2
"""
