if __name__ == "__main__":
    print("\n=== Import Transmutation Mastery ===")

    print("\nMethod 1 - Full module import:")
    try:
        import alchemy
        print("alchemy.elements.create_fire(): "
              f"{alchemy.elements.create_fire()}")
    except Exception as err:
        print(f"\33[31mERROR: {err}\33[0m")

    print("\nMethod 2 - Specific function import:")
    try:
        from alchemy import create_water
        print(f"create_water(): {create_water()}")
    except Exception as err:
        print(f"\33[31mERROR: {err}\33[0m")

    print("\nMethod 3 - Aliased import:")
    try:
        from alchemy.potions import healing_potion as heal
        print(f"heal(): {heal()}")
    except Exception as err:
        print(f"\33[31mERROR: {err}\33[0m")

    print("\nMethod 4 - Multiple imports:")
    try:
        from alchemy.elements import create_fire, create_earth
        from alchemy.potions import strength_potion
        print(f"create_earth(): {create_earth()}\n"
              f"create_fire(): {create_fire()}\n"
              f"strength_potion(): {strength_potion()}")
    except Exception as err:
        print(f"\33[31mERROR: {err}\33[0m")

    print("\n\33[32mAll import transmutation methods mastered!\33[0m")
