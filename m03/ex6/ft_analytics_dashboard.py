#!/usr/bin/env python3

class Player:
    def __init__(self, name: str, score: int,
                 is_active: bool, achievements: set[str]):
        self.name = name
        self.score = score
        self.is_active = is_active
        self.achievements = achievements


if __name__ == "__main__":
    print("=== Game Analytics Dashboard ===")

    alice = Player("alice", 2300, True, {"first_kill", "perfectionist",
                                         "collector", "speed_demon",
                                         "treasure_hunter"})
    charlie = Player("charlie", 2150, True, {"boss_slayer", "perfectionist",
                                             "collector", "speed_demon",
                                             "treasure_hunter"})
    diana = Player("diana", 2050, False, {"perfectionist", "collector",
                                          "speed_demon", "treasure_hunter"})
    bob = Player("bob", 1800, True, {"level_10", "perfectionist", "collector"})
    players = [alice, bob, charlie, diana]

    print("\n=== List Comprehension Examples ===")
    high_scorers = [player.name for player in players if player.score > 2000]
    scores_doubled = [player.score * 2 for player in players]
    active_players = [player.name for player in players if player.is_active]
    print(f"High scorers (>2000): {high_scorers}")
    print(f"Scores doubled: {scores_doubled}")
    print(f"Active players: {active_players}")

    print("\n=== Dict Comprehension Examples ===")
    players_dict = {alice.name: alice.score,
                    bob.name: bob.score,
                    charlie.name: charlie.score}
    categories = {"high": 3, "medium": 2, "low": 1}
    achieves_count = {player.name: len(player.achievements)
                      for player in players if player.name in players_dict}
    print(f"Player scores: {players_dict}")
    print(f"Score categories: {categories}")
    print(f"Achievements counts: {achieves_count}")

    print("\n=== Set Comprehension Examples ===")
    players_set = {player.name for player in players}
    alice_uniq = alice.achievements - bob.achievements - charlie.achievements
    bob_uniq = bob.achievements - alice.achievements - charlie.achievements
    charlie_uniq = charlie.achievements - alice.achievements - bob.achievements
    achieves_set = alice_uniq | bob_uniq | charlie_uniq
    regions = {"north", "east", "central", "north"}
    print(f"Unique players: {players_set}")
    print(f"Unique achievements: {achieves_set}")
    print(f"Active regions: {regions}")

    print("\n=== Combined Analysis ===")
    achievements = alice.achievements | bob.achievements | charlie.achievements
    players_score = [player.score for player in players]
    average_score = sum(players_score) / len(players_score)
    top_performer = players[0]
    for player in players:
        if player.score > top_performer.score:
            top_performer == player
    print(f"Total players: {len(players)}")
    print(f"Total unique achievements: {len(achievements)}")
    print(f"Average score: {average_score:.1f}")
    print(f"Top performer: {top_performer.name} ({top_performer.score} points,"
          f" {len(top_performer.achievements)} achievements)")
