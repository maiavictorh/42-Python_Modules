#!/usr/bin/env python3

class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


def check_plant(water_level: int) -> None:
    if water_level < 10:
        raise PlantError("The tomato plant is wilting!")


def check_water(water_level: int) -> None:
    if water_level < 10:
        raise WaterError("Not enough water in the tank!")


def catch_plant_error():
    try:
        check_plant(7)
    except PlantError as err:
        print(f"Caught {type(err).__name__}: {err}")


def catch_water_error():
    try:
        check_water(7)
    except WaterError as err:
        print(f"Caught {type(err).__name__}: {err}")


if __name__ == "__main__":
    print("=== Custom Garden Errors Demo ===\n")
    print("Testing PlantError...")
    catch_plant_error()
    print("\nTesting WaterError...")
    catch_water_error()
    print("\nTesting catching all garden errors...")
    tests = [check_plant, check_water]
    for test in tests:
        try:
            test(7)
        except GardenError as err:
            print(f"Caught a garden error: {err}")

    print("\nAll custom error types work correctly!")
