from collections import deque
import re


Stacks = list[deque]
Moves = list[tuple[int, int, int]]


def parse_stacks(stack_str: str) -> Stacks:
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


def parse_moves(move_str: str) -> Moves:
    # Note: convert stack to stack indices
    moves = [(int(m[0]), int(m[1]) - 1, int(m[2]) - 1)
             for m in move_re.findall(move_str)]
    return moves


def print_stacks(stacks: list[deque]):
    for idx, stack in enumerate(stacks):
        print(f"{idx + 1} ", *(f"[{v}]" for v in stack), sep="")
    print("---")


def apply_moves_part1(stacks: Stacks, moves: Moves) -> Stacks:
    for num, from_stack, to_stack in moves:
        for _ in range(num):
            stacks[to_stack].append(stacks[from_stack].pop())

    return stacks


def apply_moves_part2(stacks: Stacks, moves: Moves) -> Stacks:
    for num, from_stack, to_stack in moves:
        stacks[to_stack].extend([stacks[from_stack].pop() for _ in range(num)][::-1])

    return stacks


def extract_top(stacks: Stacks) -> str:
    return "".join(x[-1] for x in stacks)


def solve(puzzle_input: str) -> tuple[str, str | None]:
    stack_str, _, move_str = puzzle_input.partition("\n\n")

    stacks_part1 = parse_stacks(stack_str)
    stacks_part2 = parse_stacks(stack_str)
    moves = parse_moves(move_str)

    apply_moves_part1(stacks_part1, moves)
    answer_part_1 = extract_top(stacks_part1)
    apply_moves_part2(stacks_part2, moves)
    answer_part_2 = extract_top(stacks_part2)
    return answer_part_1, answer_part_2


TEST_EXPECTED = ("CMZ", "MCD")
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
