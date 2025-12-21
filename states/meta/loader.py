from __future__ import annotations

from typing import TYPE_CHECKING

from pykraken import AnimationController, SheetStrip, Vec2

from core.constants import (
    ASSET_HUMAN_IDLE,
    ASSET_HUMAN_RUNNING,
    ASSET_HUMAN_WALKING,
    PLAYER_ANIMATION_FPS,
)
from entities.player import Player, PlayerStates
from states.meta.base_state import BaseState
from states.meta.state_enums import StateEnum

if TYPE_CHECKING:
    from typing import TypedDict

    class AnimationData(TypedDict):
        frames: int
        path: str


class LoaderState(BaseState, state_name=StateEnum.LOADER):
    def __init__(self) -> None:
        self.player_animation_data: dict[PlayerStates, AnimationData] = {
            PlayerStates.IDLE: {
                "frames": 9,
                "path": ASSET_HUMAN_IDLE,
            },
            PlayerStates.WALKING: {
                "frames": 8,
                "path": ASSET_HUMAN_WALKING,
            },
            PlayerStates.RUNNING: {
                "frames": 8,
                "path": ASSET_HUMAN_RUNNING,
            },
        }

    def _load_player(self) -> None:
        player_animations: dict[PlayerStates, AnimationController] = {}

        for state, state_data in self.player_animation_data.items():
            player_animations[state] = AnimationController()
            sheet = (
                SheetStrip(state, state_data["frames"], PLAYER_ANIMATION_FPS),
            )
            player_animations[state].load_sprite_sheet(
                state_data["path"], Vec2(96, 64), sheet
            )

        BaseState.player = Player(player_animations, PlayerStates.IDLE)

    def on_enter(self, previous_state: None | BaseState) -> None:
        self._load_player()

        self.manager.change_state(self.manager.post_init_state)
