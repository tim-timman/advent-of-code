def solve(puzzle_input: str) -> tuple[int, int | None]:
    fully_contained_assignments = 0

    for x in puzzle_input.splitlines():
        assignments = x.split(",")
        a1, a2 = [tuple(map(int, a.split("-"))) for a in assignments]

        for _ in range(2):
            if a1[0] <= a2[0] and a1[1] >= a2[1]:
                fully_contained_assignments += 1
                break
            a1, a2 = a2, a1

    return fully_contained_assignments, None


TEST_EXPECTED = (2, None)
TEST_INPUT = """\
2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8
"""
