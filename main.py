import pykraken as kn
from game_state import StateManager
from pykraken import Vec2

from core.constants import WINDOW_HEIGHT, WINDOW_WIDTH
from states.meta import BaseState


def main() -> None:
    manager = StateManager(bound_state_type=BaseState)
    manager.load_states()

    kn.init()
    kn.window.create("Kraken Example", Vec2(WINDOW_WIDTH, WINDOW_HEIGHT))

    while kn.window.is_open():
        ...


if __name__ == "__main__":
    main()
