import random

from pygame import Surface

from src.base.game import BaseGame
from src.config import config
from src.const import COLOR_BLACK, COLOR_WHITE
from src.enum import GameLife


class HTree(BaseGame):
    def __init__(self, screen: Surface) -> None:
        super().__init__(screen)

        start_width = (
            (self._screen.get_width() // config.PIXELS_IN_POINT - 5) // 2
        )
        start_height = (
            (self._screen.get_height() // config.PIXELS_IN_POINT - 5) // 2
        )

        for i in range(5):
            for j in range(5):
                value = random.randint(1, 3)

                self._gen[start_height + i][start_width + j] = int(value < 2)

    def _get_next_value(self, x: int, y: int) -> int:
        neighbors = self._get_neighbors_by_point(x, y)

        sum_live = 0

        for i in range(3):
            for j in range(3):
                if i == 1 and j == 1:
                    continue

                sum_live += neighbors[i][j]

        center = neighbors[1][1]

        if center == GameLife.EMPTY.value and sum_live == 1:
            return GameLife.LIVE.value

        return center

    def _get_color(self, value: int) -> tuple:
        match value:
            case GameLife.EMPTY.value:
                return COLOR_WHITE
            case GameLife.LIVE.value:
                return COLOR_BLACK
