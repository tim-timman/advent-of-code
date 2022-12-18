from functools import reduce
from itertools import islice
from operator import or_


def count_bits(num: int):
    return sum(num & (1 << i) > 0 for i in range(ord("z")))


def first_unique_chars(data: list[int], num) -> int | None:
    offset = num - 1
    for idx in range(offset, len(data)):
        val = reduce(or_, islice(data, idx - offset, idx + 1))
        if count_bits(val) == num:
            return idx + 1


def solve(puzzle_input: str) -> tuple[int, int | None]:
    data: list[int] = []
    for char in puzzle_input:
        if char == "\n":
            break
        data.append(1 << (ord(char) - ord("a")))

    answer_part_1 = first_unique_chars(data, 4)
    answer_part_2 = first_unique_chars(data, 14)
    return answer_part_1, answer_part_2


TEST_EXPECTED = (7, 19)
TEST_INPUT = """\
mjqjpqmgbljsphdztnvjfqwrcgsmlb
"""
