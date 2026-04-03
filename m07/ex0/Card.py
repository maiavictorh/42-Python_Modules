from abc import ABC, abstractmethod
from enum import Enum


class CardError(Exception):
    pass


class Rarity(Enum):
    LEGENDARY = "Legendary"
    EPIC = "Epic"
    RARE = "Rare"
    COMMON = "Common"


class Card(ABC):
    def __init__(self, name: str, cost: int, rarity: str, mana: int) -> None:
        self.name = self.validate_str(name)
        self.cost = self.validate_int(cost)
        self.rarity = self.validate_str(rarity)
        self.mana = self.validate_int(mana)

    @staticmethod
    def validate_str(input: str) -> str:
        if type(input) is not str or not input.strip():
            raise ValueError("Invalid imput.")
        return input

    @staticmethod
    def validate_int(input: int) -> int:
        if type(input) is not int or input < 0:
            raise ValueError("Invalid input.")
        return input

    @abstractmethod
    def play(self, game_state: dict) -> dict:
        pass

    def get_card_info(self) -> dict:
        return {"name": self.name, "cost": self.cost, "rarity": self.rarity}

    def is_playable(self, available_mana: int) -> bool:
        return available_mana > self.cost
