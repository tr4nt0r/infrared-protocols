"""Base class for generic LED remotes."""

from abc import abstractmethod
from enum import IntEnum

from ....commands import Command


class GenericLEDRemoteCode(IntEnum):
    """Base class for generic LED remote control IR command codes."""

    @abstractmethod
    def to_command(self, repeat_count: int = 0) -> Command:
        """Build a NEC command."""
