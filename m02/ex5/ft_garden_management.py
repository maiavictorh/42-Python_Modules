#!/usr/bin/env python3

class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(PlantError):
    pass


class SunlightError(PlantError):
    pass


class Plant:
    def __init__(self, name: str, water: int, sun: int) -> None:
        self.name = name
        self.water = water
        self.sun = sun


class GardenManager:
    def __init__(self) -> None:
        self.plants: list[Plant] = []
        self.water_tank = 5

    def add_plant(self, plant: Plant) -> None:
        try:
            if not isinstance(plant.name, str) or not plant.name.strip():
                raise ValueError("Plant name cannot be empty!")
            self.plants.append(plant)
            print(f"Added {plant.name} successfully")
        except ValueError as err:
            print(f"Error adding plant: {err}")

    def water_plants(self) -> None:
        print("Opening watering system")
        try:
            for plant in self.plants:
                if self.water_tank < 2:
                    raise GardenError("Not enough water in tank")
                plant.water += 1
                self.water_tank -= 2
                print(f"Watering {plant.name} - success")
        except GardenError as err:
            print(f"Caught {type(err).__name__}: {err}")
        finally:
            print("Closing watering system (cleanup)")

    def check_plant_health(self) -> None:
        try:
            for plant in self.plants:
                if 1 < plant.water > 10:
                    if plant.water < 1:
                        raise WaterError(f" Water level {plant.water}"
                                         f" is too low (min 1)")
                    elif plant.water > 10:
                        raise WaterError(f" Water level {plant.water}"
                                         f" is too high (max 10)")
                if 2 < plant.sun > 12:
                    if plant.sun < 2:
                        raise SunlightError(f"Sunlight hours {plant.sun}"
                                            " is too low (min 2)")
                elif plant.sun > 12:
                    raise SunlightError(f"Sunlight hours {plant.sun}"
                                        f" is too high (max 12)")
                else:
                    print(f"{plant.name}: healthy "
                          f"(water: {plant.water}, sun: {plant.sun})")
        except (WaterError, SunlightError) as err:
            print(f"Error checking {plant.name}: {err}")


def test_garden_management() -> None:
    torugo = GardenManager()
    tomato = Plant("tomato", 4, 8)
    lettuce = Plant("lettuce", 14, 7)
    carrot = Plant("   ", 7, 14)

    print("Adding plants to garden...")
    torugo.add_plant(tomato)
    torugo.add_plant(lettuce)
    torugo.add_plant(carrot)

    print("\nWatering plants...")
    torugo.water_plants()

    print("\nChecking plant health...")
    torugo.check_plant_health()

    print("\nTesting error recovery...")
    torugo.water_plants()
    print("System recovered and continuing...")


if __name__ == "__main__":
    print("=== Garden Management System ===\n")
    test_garden_management()
    print("\nGarden management system test complete!")
