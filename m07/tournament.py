from ex2 import NormalStrategy, AggressiveStrategy, DefensiveStrategy

if __name__ == "__main__":

    flameling = NormalStrategy("Flameling", "Fire")
    sproutling = DefensiveStrategy("Sproutling", "Grass")
    flameling2 = AggressiveStrategy("Flameling", "Fire")

    tournament0 = (flameling, sproutling)

    print("Tournament 0 (basic)")
    print("[ ", end="")
    i = 0
    for creature in tournament0:
        print(f"({creature.name}+{creature.strat_type})", end="")
        if i < len(tournament0) - 1:
            print(", ", end="")
        i += 1
    print(" ]")
