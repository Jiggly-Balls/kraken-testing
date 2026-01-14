from __future__ import annotations

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

from game_state import State
from game_state.utils import MISSING

if TYPE_CHECKING:
    from pykraken import Event

    from entities.player import Player
    from states.meta.base_manager import BaseManager


__all__ = ("BaseState",)


class BaseState(State["BaseState"], ABC):
    manager: BaseManager  # pyright: ignore[reportIncompatibleVariableOverride]
    player: Player = MISSING

    @abstractmethod
    def process_update(self, dt: float) -> None: ...

    @abstractmethod
    def process_event(self, event: Event, dt: float) -> None: ...
