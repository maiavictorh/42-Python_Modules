#!/usr/bin/env python3

class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class NameError(PlantError):
    pass


class WaterError(PlantError):
    pass


class SunlightError(PlantError):
    pass


def check_plant_health(plant_name: str,
                       water_level: int,
                       sunlight_hours: int) -> str:
    if not 1 <= water_level <= 10:
        if water_level < 1:
            raise WaterError(f"Water level {water_level} is too low (min 1)")
        else:
            raise WaterError(f"Water level {water_level} is too high (max 10)")
    if not 2 <= sunlight_hours <= 12:
        if sunlight_hours < 2:
            raise ValueError(f"Sunlight hours {sunlight_hours}"
                             " is too low (min 2)")
        else:
            raise ValueError(f"Sunlight hours {sunlight_hours}"
                             " is too high (max 12)")
    return f"Plant '{plant_name}' is healthy!"


class Plant:
    def __init__(self, name: str, water: int, sun: int) -> None:
        self.name = name
        self.water = water
        self.sun = sun


class GardenManager:
    def __init__(self) -> None:
        self.plants: list[Plant] = []

    def add_plant(self, plant: Plant) -> None:
        try:
            if not plant.name:
                raise NameError("Plant name cannot be empty!")                
            self.plants.append(plant)
            print(f"Added {plant} succesfully")
        except NameError as err:
            print(f"Error adding plant: {err}")

    def water_plants(self) -> None:
        try:
            for plant in self.plants:
                if plant.water > 9:
                    raise WaterError("Plant water level will pass the limit!")
                plant.water += 1
                print(f"Watering {plant.name} - success")
        except WaterError as err:
            print(f"Error: {err}")
        finally:
            print("Closing watering system (cleanup)")
