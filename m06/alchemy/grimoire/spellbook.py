
def record_spell(spell_name: str, ingredients: str) -> str:
    try:
        from .validator import validate_ingredients
        if validate_ingredients(ingredients) == "VALID":
            return f"Spell recorded {spell_name} {validate_ingredients}"
    except Exception as err:
        return f"\33[31ERROR: {err}\33[0m"
