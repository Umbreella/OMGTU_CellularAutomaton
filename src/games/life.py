import random

from pygame import Surface

from src.base.game import BaseGame
from src.const import COLOR_BLACK, COLOR_WHITE
from src.enum import GameLife


class Life(BaseGame):
    def __init__(self, screen: Surface) -> None:
        super().__init__(screen)

        for i in range(len(self._gen)):
            for j in range(len(self._gen[0])):
                value = random.randint(1, 10)

                self._gen[i][j] = int(value < 4)

    def _get_next_value(self, width: int, height: int) -> int:
        neighbors = self._get_neighbors_by_point(width, height)

        sum_live = 0

        for i in range(3):
            for j in range(3):
                if i == 1 and j == 1:
                    continue

                sum_live += neighbors[i][j]

        center = neighbors[1][1]

        if center == GameLife.EMPTY.value and sum_live == 3:
            return GameLife.LIVE.value

        if center == GameLife.LIVE.value and sum_live in (2, 3):
            return GameLife.LIVE.value

        return GameLife.EMPTY.value

    def _get_color(self, value: int) -> tuple:
        match value:
            case GameLife.EMPTY.value:
                return COLOR_WHITE
            case GameLife.LIVE.value:
                return COLOR_BLACK
