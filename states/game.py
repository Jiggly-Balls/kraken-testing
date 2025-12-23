from __future__ import annotations

from states.meta import BaseState, StateEnum


class GameState(BaseState, state_name=StateEnum.GAME):
    def process_update(self, dt: float) -> None:
        self.player.process_update(dt)
        self.player.process_render()
