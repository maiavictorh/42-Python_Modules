from ex0.Card import Card


class ArtifactCard(Card):
    def __init__(self,
                 name: str,
                 cost: int,
                 rarity: str,
                 mana: int,
                 durability: int,
                 effect_type: str) -> None:
        super().__init__(name, cost, rarity, mana)
        self.durability = self.validate_int(durability)
        self.effect_type = self.validate_str(effect_type)
        self.type = "Artifact"

    def play(self, game_state: dict) -> dict:
        if self.mana >= self.cost:
            self.mana -= self.cost

            if self.durability >= 99:
                effect = "Permanent"
            else:
                effect = "Temporary"
            print("Play result: ",
                  {"card_played": self.name,
                   "mana_used": self.cost,
                   "effect": f"{effect}: {self.effect_type} per turn"})
        else:
            print("\33[33mInsufficient mana!\33[0m")
        return game_state

    def activate_ability(self) -> dict:
        pass
