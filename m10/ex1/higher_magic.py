from collections.abc import Callable


def spell(target: str, power: int) -> str:
    pass


def heal(target: str, power: int) -> str:
    return f"Heal restores {target}, for {power} HP"


def spell_combiner(spell1: Callable,
                   spell2: Callable) -> Callable[[str, int], tuple[str, str]]:
    def combined_spells(target: str, power: int) -> tuple[str, str]:
        return spell1(target, power), spell2(target, power)
    return combined_spells


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    pass


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    pass


def spell_sequence(spells: list[Callable]) -> Callable:
    pass


if __name__ == "__main__":
    test_values = [15, 10, 7]
    test_targets = ['Dragon', 'Goblin', 'Wizard', 'Knight']
