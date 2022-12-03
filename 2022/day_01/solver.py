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

TEST_RESULT = 24000


def main():
    assert solve(TEST_INPUT)[0] == TEST_RESULT

    from pathlib import Path
    puzzle_input = (Path(__file__).parent / "input.txt").read_text()
    answer_part_1, answer_part_2 = solve(puzzle_input)
    print(f"Answer part 1: {answer_part_1}\n"
          f"Answer part 2: {answer_part_2}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
