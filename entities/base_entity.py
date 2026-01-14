from __future__ import annotations

from abc import ABC, abstractmethod


class BaseEntity(ABC):
    @abstractmethod
    def process_update(self, dt: float) -> None: ...

    @abstractmethod
    def process_render(self) -> None: ...
