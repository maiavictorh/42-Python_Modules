def validate_ingredients(ingredients: str) -> str:
    valid = ["fire", "water", "earth", "air"]

    for i in valid:
        if valid == ingredients:
            return f"{ingredients} - VALID"
    return f"{ingredients} - INVALID"
