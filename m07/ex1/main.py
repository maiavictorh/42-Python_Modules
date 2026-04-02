from .SpellCard import SpellCard
from .ArtifactCard import ArtifactCard
from .Deck import Deck
from ex0.CreatureCard import CreatureCard
from ex0.Card import Rarity as r


if __name__ == "__main__":
    print("\n=== DataDeck Deck Builder ===")

    spell = SpellCard("Lightning Bolt", 3, r.EPIC.value,
                      "Deal 3 damage to target")
    artifact = ArtifactCard("Mana Crystal", 2, r.COMMON.value,
                            "Permanent", "+1 mana per turn")
    creature = CreatureCard("Fire Dragon", 5, r.LEGENDARY.value, 7, 5, 6)
    cards = [spell, artifact, creature]

    deck = Deck(cards)

    print("\nBuilding deck with different card types...")
