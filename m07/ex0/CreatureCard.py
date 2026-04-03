from .Card import Card


class CreatureCard(Card):
    def __init__(self, name: str, cost: int, rarity: str,
                 mana: int, attack: int, health: int) -> None:
        super().__init__(name, cost, rarity, mana)
        self.attack = self.validate_int(attack)
        self.health = self.validate_int(health)
        self.type = "Creature"

    def play(self, game_state: dict) -> dict:
        if self.mana >= self.cost:
            self.mana -= self.cost
            print("Play result: ",
                  {"card_played": self.name,
                   "mana_used": self.cost,
                   "effect": "Creature summoned to battlefield"})
        else:
            print("\33[33mInsufficient mana!\33[0m")
        return game_state

    def get_card_info(self) -> dict:
        info = super().get_card_info()
        info.update({"type": self.type,
                     "attack": self.attack,
                     "health": self.health,
                     "mana": self.mana})
        return info

    def attack_target(self, target: "CreatureCard") -> dict:
        self.mana -= self.cost

        combat_resolved = False
        if self.attack >= target.health:
            combat_resolved = True

        return {"attacker": self.name,
                "target": target.name,
                "damage_dealt": self.attack,
                "combat_resolved": combat_resolved}
