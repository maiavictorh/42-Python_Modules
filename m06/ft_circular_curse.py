def validate_test() -> None:
    from alchemy.grimoire import record_spell
    print("record_spell(\"Fireball\", \"fire air\"):",
          record_spell("Fireball", "fire air"))
    print("record_spell(\"Dark Magic\", \"shadow\"):",
          record_spell("Dark Magic", "shadow"))


if __name__ == "__main__":
    print("\n=== Circular Curse Breaking ===")

    print("\nTesting ingredient validation:")
    try:
        from alchemy.grimoire import validate_ingredients
        print("validate_ingredients(\"fire air\"):",
              validate_ingredients("fire air"))
        print("validate_ingredients(\"dragon scales\"):",
              validate_ingredients("dragon scales"))
    except Exception as err:
        print(f"\33[32mERROR: {err}\33[0m")

    print("\nTesting spell recording with validation:")
    try:
        validate_test()
    except Exception as err:
        print(f"\33[32mERROR: {err}\33[0m")

    print("\nTesting late import technique:")
    try:
        from alchemy.grimoire import record_spell
        print("record_spell(\"Lightning\", \"air\"):",
              record_spell("Lightning", "air"))
    except Exception as err:
        print(f"\33[32mERROR: {err}\33[0m")

    print("\nCircular dependency curse avoided using late imports!"
          "\nAll spells processed safely!")
