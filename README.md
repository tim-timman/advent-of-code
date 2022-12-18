# advent-of-code

Repo for solutions to [Advent of Code][aoc] challenges.

[aoc]:

Includes a small little framework to generate some boilerplate code for solving
the challenges and test/running them in an organized manner.

**Usage:**

```
usage: aoc.py [-h] [--generate] [-y YEAR] [-d DAY]

options:
  -h, --help            show this help message and exit
  --generate            generate templates for the given day
  -y YEAR, --year YEAR  Advent of Code year (default: 2022)
  -d DAY, --day DAY     challenge day (defaults to latest)
```

**Generate boilerplate for the next challenge:**
```
$ ./aoc.py --generate
Generated: /<repo-path>/advent-of-code/2022/day_07/solver.py
```

**Running the latest challenge:**

```
$ ./aoc.py
Advent of Code 2022 – Day 7
  Part 1: 1583951
  Part 2: 214171
```
