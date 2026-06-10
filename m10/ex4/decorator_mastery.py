import time
import functools
from collections.abc import Callable


def spell_timer(func: Callable) -> Callable:

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Casting {func.__name__}...")
        start = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - start
        print(f"Spell completed in {elapsed:.3f} seconds")
        return result
    return wrapper


def power_validator(min_power: int) -> Callable:

    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            power = kwargs.get("power") or next(
                (a for a in args if isinstance(a, int)), None
            )
            if power is None or power < min_power:
                return "Insufficient power for this spell"
            return func(*args, **kwargs)
        return wrapper
    return decorator


def retry_spell(max_attempts: int) -> Callable:

    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    print(
                        f"Spell failed, retrying... "
                        f"(attempt {attempt}/{max_attempts})"
                    )
            return f"Spell casting failed after {max_attempts} attempts"
        return wrapper
    return decorator


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        return len(name) >= 3 and all(c.isalpha() or c.isspace() for c in name)

    @power_validator(min_power=10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with {power} power"


if __name__ == "__main__":
    GREEN = "\33[32m"
    NC = "\33[0m"

    print(f"\n{GREEN}Testing spell timer...", NC)

    @spell_timer
    def fireball() -> str:
        time.sleep(0.1)
        return "Fireball cast!"

    result = fireball()
    print(f"Result: {result}")

    print(f"\n{GREEN}Testing retrying spell...", NC)
    call_count = {"n": 0}

    @retry_spell(max_attempts=3)
    def always_fails() -> str:
        raise RuntimeError("No mana!")

    print(always_fails())

    @retry_spell(max_attempts=3)
    def unstable_spell() -> str:
        call_count["n"] += 1
        if call_count["n"] < 3:
            raise RuntimeError("Spell unstable!")

    print(f"\n{GREEN}Testing MageGuild...", NC)
    print(MageGuild.validate_mage_name("Merlin"))
    print(MageGuild.validate_mage_name("X2"))

    guild = MageGuild()
    print(guild.cast_spell("Lightning", 15))
    print(guild.cast_spell("Spark", 5))
