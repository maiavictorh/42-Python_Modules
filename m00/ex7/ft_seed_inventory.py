def ft_seed_inventory(seed_type: str, quantity: int, unit: str):
    up_seed = seed_type.capitalize()
    if unit == "packets":
        print(f"{up_seed} seeds: {quantity} {unit} available")
    elif unit == "grams":
        print(f"{up_seed} seeds: {quantity} {unit} total")
    elif unit == "area":
        print(f"{up_seed} seeds: covers {quantity} square meters")
    else:
        print("Unknown unit type")
