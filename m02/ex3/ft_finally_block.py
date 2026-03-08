#!/usr/bin/env python3

class InvalidPlantError(Exception):
    pass


def water_plants(plant_list: list) -> None:
    print("Opening watering system")
    try:
        for plant in plant_list:
            if not plant:
                raise InvalidPlantError(f"Cannot water {plant}"
                                        " - invalid plant!")
            print(f"Watering {plant}")
    except InvalidPlantError as err:
        print(f"Error: {err}")
    finally:
        print("Closing watering system (cleanup)")


def test_watering_system():
    good_list = ["tomato", "lettuce", "carrots"]
    bad_list = ["tomato", None, "carrots"]

    print("Testing normal watering...")
    water_plants(good_list)
    print("Watering completed successfully!\n")

    print("Testing with error...")
    water_plants(bad_list)


if __name__ == "__main__":
    print("=== Garden Watering System ===\n")
    test_watering_system()
    print("\nCleanup always happens, even with errors!")
