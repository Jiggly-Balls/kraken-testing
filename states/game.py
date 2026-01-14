from __future__ import annotations

from typing import TYPE_CHECKING

from states.meta import BaseState, StateEnum

if TYPE_CHECKING:
    from pykraken import Event


class GameState(BaseState, state_name=StateEnum.GAME):
    def process_update(self, dt: float) -> None:
        self.player.process_update(dt)
        self.player.process_render()

    def process_event(self, event: Event, dt: float) -> None:
        pass
