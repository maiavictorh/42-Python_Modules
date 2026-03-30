def validate_ingredients(ingredients: str) -> str:
    valid = ["fire", "water", "earth", "air"]

    for word in valid:
        if ingredients.find(word) != -1:
            return f"{ingredients} - \33[32mVALID\33[0m"
    return f"{ingredients} - \33[33mINVALID\33[0m"
