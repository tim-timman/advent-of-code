from __future__ import annotations

from functools import total_ordering
from operator import itemgetter
from typing import get_type_hints


@total_ordering
class Move:
    loses_to: Move

    def __lt__(self, other):
        return isinstance(other, get_type_hints(self, globals())["loses_to"])

    def __eq__(self, other):
        return isinstance(other, type(self))


class Rock(Move):
    loses_to: Paper


class Paper(Move):
    loses_to: Scissors


class Scissors(Move):
    loses_to: Rock


POINTS_PER_MOVE = {
    Rock: 1,
    Paper: 2,
    Scissors: 3,
}

KEY_MOVE_MAP = {
    "A": Rock(),
    "B": Paper(),
    "C": Scissors(),
    "X": Rock(),
    "Y": Paper(),
    "Z": Scissors(),
}


def solve(strategy_guide: str) -> tuple[int, int | None]:
    rounds = [itemgetter(*round.split())(KEY_MOVE_MAP)
              for round in strategy_guide.splitlines()]

    total_score = 0
    for opponent_move, my_move in rounds:
        total_score += POINTS_PER_MOVE[type(my_move)]

        if opponent_move < my_move:  # win
            total_score += 6
        elif opponent_move > my_move:  # loss
            total_score += 0
        else:  # draw
            total_score += 3

    return total_score, -1


TEST_EXPECTED = 15
TEST_INPUT = """\
A Y
B X
C Z
"""
