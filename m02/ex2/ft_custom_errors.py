#!/usr/bin/env python3

class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


def check_plant(humidity: int) -> None:
    if humidity < 10:
        raise PlantError("The tomato plant is wilting!")


def check_water(water_level: int) -> None:
    if water_level < 10:
        raise WaterError("Not enough water in the tank!")


if __name__ == "__main__":
    print("=== Custom Garden Errors Demo ===\n")
    tests = [check_plant, check_water]
    for test in tests:
        try:
            test(7)
        except (PlantError, WaterError) as err:
            print(f"Testing {type(err).__name__}...")
            print(f"Caught {type(err).__name__}: {err}\n")
    print("Testing catching all garden errors...")
    for test in tests:
        try:
            test(7)
        except GardenError as err:
            print(f"Caught a garden error: {err}")

    print("\nAll custom error types work correctly!")
