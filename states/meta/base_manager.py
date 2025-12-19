from __future__ import annotations

from typing import TYPE_CHECKING

from game_state import StateManager

from states.meta.base_state import BaseState

if TYPE_CHECKING:
    from typing import Any

    from states.meta.state_enums import StateEnum


class BaseManager(StateManager[BaseState]):
    def __init__(
        self,
        *,
        post_init_state: StateEnum,
        bound_state_type: type[BaseState],
        **kwargs: Any,
    ) -> None:
        super().__init__(bound_state_type=bound_state_type, **kwargs)  # pyright: ignore[reportUnknownMemberType]

        self.post_init_state: StateEnum = post_init_state
