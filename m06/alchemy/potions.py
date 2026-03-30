def healing_potion() -> str:
    try:
        from .elements import create_fire, create_water
        return ("Healing potion brewed with "
                f"{create_fire()} and {create_water()}")
    except Exception as err:
        return f"\33[31mERROR: {err}\33[0m"


def strength_potion() -> str:
    try:
        from .elements import create_earth, create_fire
        return (f"Strength potion brewed with "
                f"{create_earth()} and {create_fire()}")
    except Exception as err:
        return f"\33[31mERROR: {err}\33[0m"


def invisibility_potion() -> str:
    try:
        from .elements import create_air, create_water
        return ("Invisibility potion brewed with"
                f" {create_air()} and {create_water()}")
    except Exception as err:
        return f"\33[31mERROR: {err}\33[0m"


def wisdom_potion() -> str:
    try:
        from .elements import create_fire, create_water, \
                              create_earth, create_air
        return (f"Wisdom potion brewed with {create_fire()}, "
                f"{create_water()}, {create_earth} and {create_air}")
    except Exception as err:
        return f"\33[31mERROR: {err}\33[0m"
