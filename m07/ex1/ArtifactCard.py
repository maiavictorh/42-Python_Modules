from ex0.Card import Card


class ArtifactCard(Card):
    def __init__(self,
                 name: str,
                 cost: int,
                 rarity: str,
                 durability: int,
                 effect_type: str) -> None:
        super().__init__(name, cost, rarity)
        self.durability = durability
        self.effect_type = effect_type

    def play(self, game_state: dict) -> dict:
        pass

    def activate_ability(self) -> dict:
        pass
