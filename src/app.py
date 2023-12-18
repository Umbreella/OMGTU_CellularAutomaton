import random
from typing import Type

from pygame import Surface, display, event, locals
from pygame.time import Clock

from src.base.game import BaseGame
from src.games import HTree, Life, LiveFreeOrDie, Maze, Seeds


class App:
    _clock: Clock
    _screen: Surface
    _game: list[Type[BaseGame]] = [HTree, Life, LiveFreeOrDie, Maze, Seeds]

    def __init__(self, display_mode: tuple) -> None:
        self._screen = display.set_mode(display_mode)
        self._clock = Clock()

    def _get_game(self, index: int) -> Type[BaseGame]:
        return self._game[index]

    def run(self) -> None:
        # cur_game = random.randint(0, len(self._game) - 1)
        cur_game = 3
        game = self._get_game(cur_game)(self._screen)

        while True:
            self._clock.tick(60)

            game.draw_next_gen()

            display.set_caption('Game: %s (FPS: %s)' % (
                game.__class__.__name__,
                round(self._clock.get_fps(), 2),
            ))

            for _event in event.get():
                if _event.type == locals.QUIT:
                    quit()
                elif _event.type == locals.KEYDOWN:
                    match _event.key:
                        case locals.K_SPACE:
                            game = self._get_game(cur_game)(self._screen)

            display.update()
