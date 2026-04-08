from abc import ABC, abstractmethod
from typing import Optional
from ex0.Creature import Creature


class HealCapability(ABC):
    def __init__(self) -> None:
        pass

    @abstractmethod
    def heal(self, target: str) -> str:
        pass


class TransformCapability(ABC):
    def __init__(self) -> None:
        pass

    @abstractmethod
    def transform(self):
        pass

    @abstractmethod
    def revert(self):
        pass


class Sproutling(Creature, HealCapability):
    def __init__(self, name: str, creature_type: str) -> None:
        super().__init__(name, creature_type)

    def attack(self) -> str:
        return f"{self.name} uses Vine Whip!"

    def heal(self, target: Optional[str] = None) -> str:
        if target is not str or target.strip():
            return f"{self.name} heals itself for a small amount"
        else:
            return f"{self.name} heals itself and others for a small amount"


class Bloomelle(Creature, HealCapability):
    def __init__(self, name: str, creature_type: str) -> None:
        super().__init__(name, creature_type)

    def attack(self) -> str:
        return f"{self.name} uses Petal Dance!"

    def heal(self, target: Optional[str] = None) -> str:
        if target is not str or target.strip():
            return f"{self.name} heals itself for a large amount"
        else:
            return f"{self.name} heals itself and others for a large amount"


class Shiftling(Creature, TransformCapability):
    def __init__(self, name: str, creature_type: str) -> None:
        super().__init__(name, creature_type)

    def attack(self) -> str:
        return f"{self.name} attacks normally."

    def transform(self):
        return super().transform()

    def revert(self):
        return super().revert()


class Morphagon(Creature, TransformCapability):
    def __init__(self, name: str, creature_type: str):
        super().__init__(name, creature_type)

    def attack(self) -> str:
        return f"{self.name} attacks normally."

    def transform(self):
        return super().transform()

    def revert(self):
        return super().revert()
