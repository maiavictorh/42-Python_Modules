def record_spell(spell_name: str, ingredients: str) -> str:
    try:
        from .validator import validate_ingredients
        if validate_ingredients(ingredients).find("INVALID") != -1:
            return (f"Spell rejected: {spell_name} "
                    f"({validate_ingredients(ingredients)})")
        else:
            return (f"Spell recorded: {spell_name} "
                    f"({validate_ingredients(ingredients)})")
    except Exception as err:
        return f"\33[31mERROR: {err}\33[0m"
