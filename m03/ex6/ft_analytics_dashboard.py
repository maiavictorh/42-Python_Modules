#!/usr/bin/env python3

class Player:
    def __init__(self, name: str, score: int, is_active: bool):
        self.name = name
        self.score = score
        self.is_active = is_active


def handle_list(players: list[Player]) -> None:
    high_scorers = [player.name for player in players if player.score > 2000]
    scores_doubled = [player.score * 2 for player in players]
    active_players = [player.name for player in players if player.is_active]
    print(f"High scorers (>2000): {high_scorers}")
    print(f"Scores doubled: {scores_doubled}")
    print(f"Active players: {active_players}")


def handle_dict(players: list[Player]) -> None:
    


if __name__ == "__main__":
    print("=== Game Analytics Dashboard ===")

    alice = Player("alice", 2300, True)
    charlie = Player("charlie", 2150, True)
    bob = Player("bob", 1800, True)
    diana = Player("diana", 2050, False)
    players = [alice, bob, charlie, diana]
    print("\n=== List Comprehension Examples ===")
    handle_list(players)

    print("\n=== Dict Comprehension Examples ===")

    print("\n=== Set Comprehension Examples ===")

    print("\n=== Combined Analysis ===")
