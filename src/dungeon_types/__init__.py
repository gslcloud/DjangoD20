"""
Dungeon Types

This module provides classes for different types of dungeons in the game.

Classes:
- Dungeon: Represents a generic dungeon.
- DungeonFactory: Factory class for creating dungeons.

"""

from .dungeon import Dungeon
from .dungeon_factory import DungeonFactory

__all__ = ['Dungeon', 'DungeonFactory']