from collections.abc import Callable
from typing import Any


def mage_counter() -> Callable[[], int]:
    count = 0

    def counter() -> int:
        nonlocal count
        count += 1
        return count

    return counter


def spell_accumulator(initial_power: int) -> Callable[[int], int]:
    total_power = initial_power

    def accumulator(amount: int) -> int:
        nonlocal total_power
        total_power += amount
        return total_power

    return accumulator


def enchantment_factory(enchantment_type: str) -> Callable[[str], str]:

    def enchant(item_name: str) -> str:
        return f"{enchantment_type} {item_name}"

    return enchant


def memory_vault() -> dict[str, Callable]:
    vault = {}

    def store(key: str, value: Any):
        vault[key] = value

    def recall(key: str):
        return vault.get(key, "Memory not found")

    return {"store": store, "recall": recall}


if __name__ == "__main__":
    GREEN = "\33[32m"
    NC = "\33[0m"

    print(f"\n{GREEN}Testing mage counter...", NC)
    counter_a = mage_counter()
    counter_b = mage_counter()
    print(f"counter_a call 1: {counter_a()}")
    print(f"counter_a call 2: {counter_a()}")
    print(f"counter_b call 1: {counter_b()}")

    print(f"\n{GREEN}Testing spell accumulator...", NC)
    accumulate = spell_accumulator(100)
    print(f"Base: 100, add 20: {accumulate(20)}")
    print(f"Base 100, add 30: {accumulate(30)}")

    print(f"\n{GREEN}Testing enchantment factory...", NC)
    enchant1 = enchantment_factory("Flaming")
    enchant2 = enchantment_factory("Frozen")
    print(enchant1("Sword"))
    print(enchant2("Shield"))

    print(f"\n{GREEN}Testing memory vault...", NC)
    vault = memory_vault()
    vault['store']("secret", 42)
    print("Store 'secret' = 42")
    print(f"Recall 'secret': {vault['recall']('secret')}")
    print(f"Recall 'unknown': {vault['recall']('unknown')}")
