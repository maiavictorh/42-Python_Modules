from abc import ABC, abstractmethod
from ex0.Creature import Creature
# from ex0 import __creature_factory__ as f1
# from ex1 import __capability_factory__ as f2
from ex1.Capability import HealCapability, TransformCapability


class BattleStrategy(ABC):
    def __init__(self) -> None:
        pass

    @abstractmethod
    def act() -> str:
        pass

    @abstractmethod
    def is_valid() -> bool:
        pass


class NormalStrategy(Creature, BattleStrategy):
    def __init__(self, name: str, creature_type: str):
        super().__init__(name, creature_type)
        self.strat_type = "Normal"

    def attack(self) -> str:
        return super().attack()

    @staticmethod
    def act():
        pass

    @staticmethod
    def is_valid():
        pass


class AggressiveStrategy(Creature, TransformCapability, BattleStrategy):
    def __init__(self, name, creature_type):
        super().__init__(name, creature_type)
        self.strat_type = "Aggressive"

    def attack(self) -> str:
        return super().attack()

    def transform(self):
        return super().transform()

    def revert(self):
        return super().revert()

    @staticmethod
    def act():
        pass

    @staticmethod
    def is_valid():
        pass


class DefensiveStrategy(Creature, HealCapability, BattleStrategy):
    def __init__(self, name: str, creature_type: str):
        super().__init__(name, creature_type)
        self.strat_type = "Normal"

    def attack(self) -> str:
        return super().attack()

    def heal(self, target):
        return super().heal(target)

    @staticmethod
    def act():
        pass

    @staticmethod
    def is_valid():
        pass
