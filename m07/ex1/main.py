from ex0 import CreatureCard
from ex0.Card import Rarity as r
from ex1 import SpellCard, ArtifactCard, Deck


if __name__ == "__main__":
    print("\n=== DataDeck Deck Builder ===")

    try:
        spell = SpellCard("Lightning Bolt", 3, r.EPIC.value,
                          6, "damage")
        artifact = ArtifactCard("Mana Crystal", 2, r.COMMON.value,
                                6, 99, "+1 mana")
        creature = CreatureCard("Fire Dragon", 5, r.LEGENDARY.value, 7, 5, 6)
        deck = Deck()
        deck.add_card(spell)
        deck.add_card(artifact)
        deck.add_card(creature)

        print("\nBuilding deck with different card types...")
        print("Deck stats:", deck.get_deck_stats())

        print("\nDrawing and playing cards:\n")
        deck.shuffle()
        for i in range(0, len(deck.cards)):
            drew_card = deck.draw_card()
            drew_card.play(drew_card.get_card_info())
            print()

    except Exception as err:
        print(f"\33[31mERROR: {err}\33[0m")

    print("Polymorphism in action: "
          "Same interface, different card behaviors!")
