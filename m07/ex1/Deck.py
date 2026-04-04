from ex0.Card import Card, CardError
import random


class Deck():
    def __init__(self):
        self.cards: list[Card] = []

    def add_card(self, card: Card) -> None:
        if not isinstance(card, Card):
            raise CardError("You can only add cards to the deck!")
        self.cards.append(card)

    def remove_card(self, card_name: str) -> bool:
        if len(self.cards) > 0:
            for card in self.cards:
                if card.name == card_name:
                    self.cards.remove(card)
                    return True
        return False

    def shuffle(self) -> None:
        if len(self.cards) > 1:
            random.shuffle(self.cards)

    def draw_card(self) -> Card:
        if len(self.cards) > 0:
            print(f"Drew: {self.cards[0].name} ({self.cards[0].type})")
            return self.cards.pop(0)

    def get_deck_stats(self) -> dict:
        from ex0 import CreatureCard
        from ex1 import SpellCard, ArtifactCard

        spell_count = 0
        creature_count = 0
        artifact_count = 0
        cost_sum = 0
        for card in self.cards:
            cost_sum += card.cost
            if isinstance(card, CreatureCard):
                creature_count += 1
            elif isinstance(card, SpellCard):
                spell_count += 1
            elif isinstance(card, ArtifactCard):
                artifact_count += 1

        avg_cost = f"{cost_sum / len(self.cards):.1f}"
        return {"total_cards": len(self.cards),
                "creatures": creature_count,
                "spells": spell_count,
                "artifacts": artifact_count,
                "avg_cost": avg_cost}
