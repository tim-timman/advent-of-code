from string import ascii_lowercase, ascii_uppercase

index_priority = " " + ascii_lowercase + ascii_uppercase


def solve(rucksacks: str) -> tuple[int, int | None]:
    priority_sum = 0
    for r in rucksacks.splitlines():
        half_len = len(r) // 2
        common_type = set(r[:half_len]).intersection(r[half_len:]).pop()
        priority_sum += index_priority.index(common_type)

    return priority_sum, None


TEST_EXPECTED = (157, None)
TEST_INPUT = """\
vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw
"""
