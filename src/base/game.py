from abc import abstractmethod

from numpy import array, int8
from pygame import Surface, draw

from src.config import config
from src.const import COLOR_WHITE


class BaseGame:
    _screen: Surface

    def __init__(self, screen: Surface) -> None:
        screen.fill(COLOR_WHITE)

        self._screen = screen
        self._gen = self._get_clear_matrix()

    def _get_clear_matrix(self) -> array:
        return array([
            [0] * (self._screen.get_width() // config.PIXELS_IN_POINT)
            for _ in range(self._screen.get_height() // config.PIXELS_IN_POINT)
        ], int8)

    def _get_neighbors_by_point(self, width: int, height: int) -> array:
        data, row, col = self._gen, len(self._gen), len(self._gen[0])

        t_row = -1 if height == 0 else height - 1
        b_row = 0 if height == row - 1 else height + 1
        l_col = -1 if width == 0 else width - 1
        r_col = 0 if width == col - 1 else width + 1

        return array([
            [data[t_row][l_col], data[t_row][width], data[t_row][r_col]],
            [data[height][l_col], data[height][width], data[height][r_col]],
            [data[b_row][l_col], data[b_row][width], data[b_row][r_col]],
        ], int8)

    def draw_next_gen(self) -> None:
        next_get = self._get_clear_matrix()

        for i in range(len(next_get)):
            for j in range(len(next_get[0])):
                next_value = self._get_next_value(width=j, height=i)

                if self._gen[i][j] != next_value:
                    draw.rect(self._screen, self._get_color(next_value), (
                        j * config.PIXELS_IN_POINT, i * config.PIXELS_IN_POINT,
                        config.PIXELS_IN_POINT, config.PIXELS_IN_POINT,
                    ))

                next_get[i][j] = next_value

        self._gen = next_get

    @abstractmethod
    def _get_next_value(self, width: int, height: int):
        pass

    @abstractmethod
    def _get_color(self, value: int) -> tuple:
        pass
