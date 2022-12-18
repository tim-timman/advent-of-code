def count_bits(num: int):
    return sum(num & (1 << i) > 0 for i in range(ord("z")))


def solve(puzzle_input: str) -> tuple[int, int | None]:
    data: list[int] = []
    for char in puzzle_input:
        if char == "\n":
            break
        data.append(1 << (ord(char) - ord("a")))

    answer_part_1 = - 1
    for idx in range(3, len(data)):
        if count_bits(data[idx - 3] | data[idx - 2] | data[idx - 1] | data[idx]) == 4:
            answer_part_1 = idx + 1
            break

    answer_part_2 = None
    return answer_part_1, answer_part_2


TEST_EXPECTED = (7, None)
TEST_INPUT = """\
mjqjpqmgbljsphdztnvjfqwrcgsmlb
"""
