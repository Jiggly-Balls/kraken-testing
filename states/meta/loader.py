from __future__ import annotations

from enum import StrEnum
from typing import TYPE_CHECKING

import pykraken as kn
from pykraken import (
    InputAction,
    Texture,
    TextureScaleMode,
    Vec2,
)

from core.animator import Animator, PlayerCosmeticAnimator
from core.constants import (
    ASSET_HUMAN_BASE_DIR,
    ASSET_HUMAN_IDLE,
    ASSET_HUMAN_RUN,
    ASSET_HUMAN_WALK,
    PLAYER_ANIMATION_FPS,
)
from core.player_data import MovementBinding, PlayerHair, PlayerStates
from entities.player import Player
from states.meta.base_state import BaseState
from states.meta.state_enums import StateEnum

if TYPE_CHECKING:
    from core.types import AnimationData


class LoaderState(BaseState, state_name=StateEnum.LOADER):
    def _fetch_asset(self, path: str) -> Texture:
        return Texture(path, TextureScaleMode.PIXEL_ART)

    def _load_player(self) -> None:
        animation_data: dict[StrEnum, AnimationData] = {
            PlayerStates.IDLE: {
                "texture": self._fetch_asset(ASSET_HUMAN_IDLE),
                "frames": 9,
            },
            PlayerStates.WALK: {
                "texture": self._fetch_asset(ASSET_HUMAN_WALK),
                "frames": 8,
            },
            PlayerStates.RUN: {
                "texture": self._fetch_asset(ASSET_HUMAN_RUN),
                "frames": 8,
            },
        }

        cosmetic_data: dict[
            PlayerStates, dict[PlayerHair, tuple[Texture, int]]
        ] = {}

        for state in PlayerStates:
            cosmetic_data[state] = {}
            for hair in PlayerHair:
                path: str = (
                    ASSET_HUMAN_BASE_DIR
                    + state.upper()
                    + f"/{hair.lower()}_{state.lower()}_strip.png"
                )
                cosmetic_data[state][hair] = (
                    self._fetch_asset(path),
                    PlayerStates.frames(state),
                )

        animator = Animator(
            animation_data,
            PlayerStates.IDLE,
            Vec2(96, 64),
            PLAYER_ANIMATION_FPS,
        )
        cosmetic_animator = PlayerCosmeticAnimator(
            cosmetic_data,
            PlayerHair.SPIKEY_HAIR,
            PlayerStates.IDLE,
            Vec2(96, 64),
            PLAYER_ANIMATION_FPS,
        )

        BaseState.player = Player(
            animator, cosmetic_animator, PlayerStates.IDLE
        )

    def _load_keybinds(self) -> None:
        for player_bindings in MovementBinding:
            actions: list[InputAction] = [
                InputAction(binding) for binding in player_bindings.value
            ]
            kn.input.bind(player_bindings.name, actions)

    def on_enter(self, previous_state: None | BaseState) -> None:
        self._load_player()
        self._load_keybinds()

        self.manager.change_state(self.manager.post_init_state)
