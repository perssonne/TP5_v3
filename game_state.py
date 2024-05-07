from enum import Enum

class GameState(Enum):

    NOT_STARTED = 0
    ROUND_DONE = 2
    GAME_OVER = 3
    VICTORY = 4
    ROUND_ACTIVE = 1