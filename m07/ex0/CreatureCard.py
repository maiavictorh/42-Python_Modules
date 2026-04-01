from .Card import Card


class CreatureCard(Card):
    def __init__(self, name: str, cost: int, rarity: str,
                 attack: int, health: int, mana: int) -> None:
        super().__init__(name, cost, rarity)
        self._attack = self.validate_int(attack)
        self._health = self.validate_int(health)
        self._mana = self.validate_int(mana)

    def play(self, game_state: dict) -> dict:
        if self._mana >= self._cost:
            self._mana -= self._cost
            print("Play result: ",
                  {"card_played": self._name,
                   "mana_used": self._cost,
                   "effect": "Creature summoned to battlefield"})
        else:
            print("\33[33mInsufficient mana!\33[0m")
        return game_state

    def get_card_info(self) -> dict:
        info = super().get_card_info()
        info.update({"type": "Creature",
                     "attack": self._attack,
                     "health": self._health,
                     "mana": self._mana})
        return info

    def attack_target(self, target: "CreatureCard") -> dict:
        self._mana -= self._cost

        combat_resolved = False
        if self._attack >= target._health:
            combat_resolved = True

        return {"attacker": self._name,
                "target": target._name,
                "damage_dealt": self._attack,
                "combat_resolved": combat_resolved}
