from abc import ABC, abstractmethod
from .Creature import Creature, Flameling, Pyrodon, Aquabub, Torragon


class CreatureFactory(ABC):
    def __init__(self) -> None:
        pass

    @abstractmethod
    def create_base() -> Creature:
        pass

    @abstractmethod
    def create_evolved() -> Creature:
        pass


class FlameFactory(ABC):
    def __init__(self) -> None:
        pass

    def create_base() -> Flameling:
        return Flameling("Flameling", "Fire")

    def create_evolved(creature: Creature) -> Pyrodon:
        return Pyrodon("Pyrodon", "Fire/Flying")


class AquaFactory(ABC):
    def __init__(self) -> None:
        pass

    def create_base() -> Aquabub:
        return Aquabub("Aquabub", "Water")

    def create_evolved(creature: Creature) -> Torragon:
        return Torragon("Torragon", "Water")
