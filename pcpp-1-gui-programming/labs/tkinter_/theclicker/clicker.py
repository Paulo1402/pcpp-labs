from enum import Enum

from .classic import ClassicClicker
from .time import TimeBoundClicker


class GameMode(Enum):
    classic = 0
    time_bound = 1


class TheClicker:
    GAME_VARIANTS = {
        GameMode.classic: ClassicClicker,
        GameMode.time_bound: TimeBoundClicker
    }
    
    def __init__(self, game_mode: GameMode = GameMode.classic, /, **game_options):
        if game_mode not in self.GAME_VARIANTS:
            raise ValueError("Game mode not found")
        
        game = self.GAME_VARIANTS[game_mode]
        self._game = game(**game_options)
    
    def run(self):
       return self._game.run()