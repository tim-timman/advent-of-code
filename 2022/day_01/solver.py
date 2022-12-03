def solve(puzzle_input: str):
    return max([
        sum(map(int, foods.split("\n")))
        for foods in puzzle_input.strip().split("\n\n")
    ])


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
    assert solve(TEST_INPUT) == TEST_RESULT

    from pathlib import Path
    puzzle_input = (Path(__file__).parent / "input.txt").read_text()
    print(f"Answer part 1: {solve(puzzle_input)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
