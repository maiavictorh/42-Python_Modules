from collections.abc import Callable
from typing import Any
from functools import reduce, partial, lru_cache, singledispatch
from operator import add, mul


def spell_reducer(spells: list[int], operation: str) -> int:
    if not len(spells):
        return 0

    operations = {
        "add": add,
        "multiply": mul,
        "max": max,
        "min": min
    }

    if operation not in operations:
        raise ValueError("Unknown operation")

    return reduce(operations[operation], spells)


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:

    aqua = partial(base_enchantment, 50, "Aqua")
    fire = partial(base_enchantment, 50, "Fire")
    rock = partial(base_enchantment, 50, "Rock")
    return {
        "Aqua": aqua,
        "Fire": fire,
        "Rock": rock
    }


@lru_cache(maxsize=128)
def memoized_fibonacci(n: int) -> int:
    if n < 2:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable[[Any], str]:

    @singledispatch
    def dispatch(spell: Any) -> str:
        return "Unknow spell type"

    @dispatch.register
    def _(spell: int) -> str:
        return f"Damage spell: {spell} damage"

    @dispatch.register
    def _(spell: str) -> str:
        return f"Enchantment: {spell}"

    @dispatch.register
    def _(spell: list) -> str:
        return f"Multicast: {len(spell)} spells"

    return dispatch


def enchantment(power: int, element: str, target: str) -> str:
    return f"Enchants {power} of element {element} in {target}"


if __name__ == "__main__":
    GREEN = "\33[32m"
    RED = "\33[31m"
    NC = "\33[0m"

    print(f"\n{GREEN}Testing spell reducer...", NC)
    try:
        spells = [7, 17, 21, 37, 42]
        print("Add:", spell_reducer(spells, "add"))
        print("Mul:", spell_reducer(spells, "multiply"))
        print("Max:", spell_reducer(spells, "max"))
        print("Min:", spell_reducer(spells, "min"))
        print("Average:", end="")
        print(spell_reducer(spells, "Average"))
    except ValueError as err:
        print(RED, err, NC)

    print(f"\n{GREEN}Testing partial enchanter...", NC)
    enchantments = partial_enchanter(enchantment)
    aqua = enchantments["Aqua"]
    print(aqua("Sword"))

    print(f"\n{GREEN}Testing memoized fibonacci...", NC)
    print("Fib(0):", memoized_fibonacci(0))
    print("Fib(1):", memoized_fibonacci(1))
    print("Fib(10):", memoized_fibonacci(10))
    print("Fib(15):", memoized_fibonacci(15))

    print(f"\n{GREEN}Testing spell dispatcher...", NC)
    caster = spell_dispatcher()
    print(caster(42))
    print(caster("fireball"))
    print(caster([10, "fire-water", 2]))
    print(caster(3.14))
