from ex0.Card import Card


class SpellCard(Card):
    def __init__(self,
                 name: str,
                 cost: int,
                 rarity: str,
                 mana: int,
                 effect_type: str) -> None:
        super().__init__(name, cost, rarity, mana)
        self.effect_type = self.validate_str(effect_type)
        self.type = "Spell"

    def play(self, game_state: dict) -> dict:
        if self.mana >= self.cost:
            self.mana -= self.cost

            print("Play result: ",
                  {"card_played": self.name,
                   "mana_used": self.cost,
                   "effect": f"Deal 3 {self.effect_type} to target"})
        else:
            print("\33[33mInsufficient mana!\33[0m")
        return game_state

    def resolve_effect(self, targets: list) -> dict:
        pass
