#!/usr/bin/env python3

def check_plant_health(plant_name: str,
                       water_level: int,
                       sunlight_hours: int) -> str:
    if not plant_name:
        raise ValueError("Plant name cannot be empty!")
    if not 1 <= water_level <= 10:
        if water_level < 1:
            raise ValueError(f"Water level {water_level} is too low (min 1)")
        else:
            raise ValueError(f"Water level {water_level} is too high (max 10)")
    if not 2 <= sunlight_hours <= 12:
        if sunlight_hours < 2:
            raise ValueError(f"Sunlight hours {sunlight_hours}"
                             " is too low (min 2)")
        else:
            raise ValueError(f"Sunlight hours {sunlight_hours}"
                             " is too high (max 12)")
    return f"Plant '{plant_name}' is healthy!"


def test_plant_checks() -> None:
    print("Testing good values...")
    try:
        print(f"{check_plant_health('tomato', 7, 10)}")
    except ValueError as err:
        print(f"Error: {err}\n")
    print("\nTesting empty plant name...")
    try:
        print(f"{check_plant_health(None, 7, 10)}")
    except ValueError as err:
        print(f"Error: {err}")
    print("\nTesting bad water level...")
    try:
        print(f"{check_plant_health('tomato', 15, 7)}")
    except ValueError as err:
        print(f"Error: {err}")
    print("\nTesting bad sunlight hours...")
    try:
        print(f"{check_plant_health('tomato', 7, 0)}")
    except ValueError as err:
        print(f"Error: {err}")
    finally:
        print("\nAll error raising tests completed!")


if __name__ == "__main__":
    print("=== Garden Plant Health Checker ===\n")
    test_plant_checks()
