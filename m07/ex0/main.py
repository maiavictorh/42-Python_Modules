from .CreatureCard import CreatureCard
from .Card import Rarity as r

if __name__ == "__main__":
    print("\n=== DataDeck Card Foundation ===")

    print("\nTesting Abstract Base Class Design:")
    try:
        fire_drgn = CreatureCard("Fire Dragon", 5, r.LEGENDARY.value, 7, 5, 6)
        print("\nCreatureCard Info:\n", fire_drgn.get_card_info())

        print(f"\nPlaying Fire Dragon with {fire_drgn._mana} mana available:")
        print("Playable:", fire_drgn.is_playable(fire_drgn._mana))
        fire_drgn.play(fire_drgn.get_card_info())

        fire_drgn._mana += 7
        goblin_warrior = CreatureCard("Goblin Warrior", 3,
                                      r.COMMON.value, 3, 3, 3)
        print(f"\n{fire_drgn._name} attacks {goblin_warrior._name}:")
        print("Attack result:", fire_drgn.attack_target(goblin_warrior))

        print(f"\nTesting insufficient mana ({fire_drgn._mana} available):")
        print("Playable:", fire_drgn.is_playable(fire_drgn._mana))
    except Exception as err:
        print(f"\33[31mERROR: {err}\33[0m")

    print("\nAbstract pattern successfully demonstrated!")
