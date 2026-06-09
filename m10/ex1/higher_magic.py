from collections.abc import Callable
from typing import Any


def spell_combiner(spell1: Callable,
                   spell2: Callable) -> Callable[[str, int], tuple[str, str]]:
    def combined_spells(target: str, power: int) -> tuple[str, str]:
        return spell1(target, power), spell2(target, power)
    return combined_spells


def power_amplifier(base_spell: Callable,
                    multiplier: int) -> Callable[[str, int], str]:
    def amplified_spell(target: str, power: int) -> str:
        return base_spell(target, power * multiplier)
    return amplified_spell


def conditional_caster(condition: Callable,
                       spell: Callable) -> Callable[[str, int], str]:
    def casted(target: str, power: int) -> str:
        if condition(target, power):
            return spell(target, power)
        return "Spell fizzled"
    return casted


def spell_sequence(spells: list[Callable]) -> Callable[[str, int], Any]:
    def sequence(target: str, power: int) -> Any:
        return (spell(target, power) for spell in spells)
    return sequence


def fireball(target: str, power: int) -> str:
    return f"Fireball hits {target} for {power} damage"


def heal(target: str, power: int) -> str:
    return f"Heals {target} for {power} HP"


def shield(target: str, power: int) -> str:
    return f"Shield protects {target} with {power} armor"


if __name__ == "__main__":
    GREEN = "\33[32m"
    NC = "\33[0m"
    print(f"\n{GREEN}Testing spell combiner...", NC)
    combined = spell_combiner(fireball, heal)
    result = combined("Dragon", 21)
    print(f"Combined spell result: {result[0]}, {result[1]}")

    print(f"\n{GREEN}Testing power amplifier...", NC)
    mega_fireball = power_amplifier(fireball, 2)
    print(f"Original: {fireball('Dragon', 21)}")
    print(f"Amplified: {mega_fireball('Dragon', 21)}")

    print(f"\n{GREEN}Testing conditional caster...", NC)
    strong_only = conditional_caster(lambda _, power: power >= 50, fireball)
    print(strong_only("Dragon", 67))
    print(strong_only("Dragon", 42))

    print(f"\n{GREEN}Testing spell sequence...", NC)
    sequence = spell_sequence([fireball, heal, shield])
    results = sequence("Dragon", 21)
    for r in results:
        print(r)
