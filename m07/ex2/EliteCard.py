from ex0.Card import Card
from ex2 import Combatable, Magical


class EliteCard(Card, Combatable, Magical):
    def __init__(self, name: str, cost: int, rarity: str, mana: int):
        super().__init__(name, cost, rarity, mana)

    def play(self, game_state: dict) -> dict:
        pass

    def attack(self, target) -> dict:
        pass

    def defend(self, incoming_damage: int) -> dict:
        pass

    def get_combat_stats(self) -> dict:
        pass

    def cast_spell(self, spell_name: str, targets: list) -> dict:
        pass

    def channel_mana(self, amount: int) -> dict:
        pass

    def get_magic_stats(self) -> dict:
        pass
