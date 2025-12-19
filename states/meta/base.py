from __future__ import annotations

from game_state import State

__all__ = ("BaseState",)


class BaseState(State["BaseState"]):
    def process_update(self, dt: float | None) -> None:  # pyright: ignore[reportIncompatibleMethodOverride]
        ...
