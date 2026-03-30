if __name__ == "__main__":
    print("\n=== Pathway Debate Mastery ===")

    print("\nTesting Absolute Imports (from basic.py):")
    try:
        from alchemy.transmutation.basic import lead_to_gold, stone_to_gem
        print(f"lead_to_gold(): {lead_to_gold()}")
        print(f"stone_to_gem(): {stone_to_gem()}")
    except Exception as err:
        print(f"\33[31mERROR: {err}\33[0m")

    print("\nTesting Relative Imports (from advanced.py):")
    try:
        from alchemy.transmutation.advanced import \
                                             philosophers_stone, elixir_of_life
        print(f"philosophers_stone(): {philosophers_stone()}")
        print(f"elixir_of_life(): {elixir_of_life()}")
    except Exception as err:
        print(f"\33[31mERROR: {err}\33[0m")

    print("\nTesting Package Access:")
    try:
        import alchemy.transmutation
        print("alchemy.transmutation.lead_to_gold(): ", end="")
        print(alchemy.transmutation.lead_to_gold())
        print("alchemy.transmutation.philosophers_stone(): ", end="")
        print(alchemy.transmutation.philosophers_stone())
    except Exception as err:
        print(f"\33[31mERROR: {err}\33[0m")

    print("\nBoth pathways work! Absolute: clear, Relative: concise")
