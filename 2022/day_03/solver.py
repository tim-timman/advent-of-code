from string import ascii_lowercase, ascii_uppercase

index_priority = " " + ascii_lowercase + ascii_uppercase


def solve(puzzle_data: str) -> tuple[int, int | None]:
    rucksacks = puzzle_data.splitlines()

    priority_sum = 0
    for r in rucksacks:
        half_len = len(r) // 2
        common_type = set(r[:half_len]).intersection(r[half_len:]).pop()
        priority_sum += index_priority.index(common_type)

    badge_priority_sum = 0
    for r1, r2, r3 in zip(*[iter(rucksacks)] * 3, strict=True):
        badge_type = set(r1).intersection(r2).intersection(r3).pop()
        badge_priority_sum += index_priority.index(badge_type)

    return priority_sum, badge_priority_sum


TEST_EXPECTED = (157, 70)
TEST_INPUT = """\
vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw
"""
