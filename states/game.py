from __future__ import annotations

import pykraken as kn

from core.constants import PLAYER_TARGET_RES
from states.meta import BaseState, StateEnum


class GameState(BaseState, state_name=StateEnum.GAME):
    def process_update(self, dt: float) -> None:
        self.player.process_update(dt)

        player_texture, player_clip = self.player.animator.get_frame(
            self.player.flip
        )

        player_hair_texture, player_hair_clip = (
            self.player.cosmetic_animator.get_frame(self.player.flip)
        )

        kn.renderer.draw(
            player_texture,
            kn.Transform(self.player.position, size=PLAYER_TARGET_RES),
            src=player_clip,
        )

        kn.renderer.draw(
            player_hair_texture,
            kn.Transform(self.player.position, size=PLAYER_TARGET_RES),
            src=player_hair_clip,
        )
