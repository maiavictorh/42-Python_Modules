#!/usr/bin/env python3

class Player:
    def __init__(self, name: str, achievements: set):
        self.name = name
        self.achievements = achievements


if __name__ == "__main__":
    print("=== Achievement Tracker System ===\n")
    alice = Player("Alice", {"first_kill", "level_10",
                             "treasure_hunter", "speed_demon"})
    bob = Player("Bob", {"first_kill", "level_10", "boss_slayer", "collector"})
    charlie = Player("Charlie", {"level_10", "treasure_hunter", "boss_slayer",
                                 "speed_demon", "perfectionist"})
    players = [alice, bob, charlie]
    for player in players:
        print(f"Player {player.name} achievements: {player.achievements}")

    print("\n=== Achievement Analytics ===")
    achievements = alice.achievements | bob.achievements | charlie.achievements
    print(f"All unique achievements: {achievements}")
    print(f"Total unique achievements: {len(achievements)}")

    common = alice.achievements & bob.achievements & charlie.achievements
    print(f"\nCommon to all players: {common}")

    alice_rare = alice.achievements - bob.achievements - charlie.achievements
    bob_rare = bob.achievements - alice.achievements - charlie.achievements
    charlie_rare = charlie.achievements - alice.achievements - bob.achievements
    rare = alice_rare | bob_rare | charlie_rare
    print(f"Rare achievements (1 player): {rare}")

    alice_vs_bob = alice.achievements & bob.achievements
    alice_unique = alice.achievements - bob.achievements
    bob_unique = bob.achievements - alice.achievements
    print(f"\nAlice vs Bob common: {alice_vs_bob}")
    print(f"Alice unique: {alice_unique}")
    print(f"Bob unique: {bob_unique}")
