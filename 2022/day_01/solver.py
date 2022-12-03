def solve(puzzle_input: str) -> tuple[int, int]:
    elf_calories = sorted([
        sum(map(int, foods.split("\n")))
        for foods in puzzle_input.strip().split("\n\n")
    ], reverse=True)
    return elf_calories[0], sum(elf_calories[:3])


TEST_INPUT = """\
1000
2000
3000

4000

5000
6000

7000
8000
9000

10000
"""

TEST_EXPECTED = 24000
