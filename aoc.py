#!/usr/bin/env python3

import argparse
import importlib
from pathlib import Path
from textwrap import dedent


def generate_template(year: int, day: int) -> int:
    assert 0 < day <= 25

    script_dir = Path(__file__).parent
    challenge_path = script_dir / f"{year}/day_{day:02d}"
    challenge_path.mkdir(parents=True, exist_ok=True)
    challenge_solver = challenge_path / "solver.py"

    try:
        with challenge_solver.open("x") as f:
            f.write(dedent('''\
            def solve(puzzle_input: str) -> tuple[int, int | None]:
                raise NotImplementedError
                # return answer_part_1, answer_part_2
            
            TEST_EXPECTED = None
            TEST_INPUT = ""
            '''))
        (challenge_path / "input.txt").touch()
    except FileExistsError:
        print(f"ERROR: Challenge {challenge_solver} already generated.")
        return 1
    else:
        print(f"Generated: {challenge_solver}")
        return 0


def load_and_run_solver(year: int, day: int) -> int:
    module_name = f"{year}.day_{day:02d}.solver"
    try:
        challenge = importlib.import_module(module_name)
    except (ImportError, AttributeError):
        print(f"ERROR: A solver for challenge {module_name} not found.")
        return 1

    test_result = challenge.solve(challenge.TEST_INPUT)[0]
    test_expected = challenge.TEST_EXPECTED
    assert test_result == test_expected, f"{test_result=} {test_expected=}"

    puzzle_input = (Path(challenge.__file__).parent / "input.txt").read_text()
    answer_part_1, answer_part_2 = challenge.solve(puzzle_input)
    print(f"Advent of Code {year} – Day {day}\n"
          f"  Part 1: {answer_part_1}")
    if answer_part_2 is not None:
        print(f"  Part 2: {answer_part_2}")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--generate", action="store_true",
                        help="generate templates for the given day")
    parser.add_argument("-y", "--year", type=int, default="2022",
                        help="Advent of Code year (default: %(default)s)")
    parser.add_argument("-d", "--day", type=int, default=None,
                        help="challenge day (defaults to latest")

    args = parser.parse_args()

    year = args.year
    use_latest_day = args.day is None

    if use_latest_day:
        day = int(sorted(Path(str(year)).glob("day_??"))[-1].name[4:])
    else:
        day = args.day

    if args.generate:
        return generate_template(year, day + 1 if use_latest_day else 1)
    else:
        return load_and_run_solver(year, day)


if __name__ == "__main__":
    raise SystemExit(main())
