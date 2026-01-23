#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self.height = height
        self.age = age

    def get_info(self) -> str:
        return (f"{self.name} ({type(self).__name__}):"
                f" {self.height}cm, {self.age} days")


class Flower(Plant):
    def __init__(self, name: str, height: int, age: int, color: str):
        super().__init__(name, height, age)
        self.color = color

    def get_info(self) -> str:
        return f"{super().get_info()}, {self.color} color"

    def bloom(self):
        print(f"{self.name} is blooming beautifully!")


class Tree(Plant):
    def __init__(
            self,
            name: str,
            height: int,
            age: int,
            trunk_diameter: int
            ) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def get_info(self) -> str:
        return f"{super().get_info()}, {self.trunk_diameter}cm diameter"

    def produce_shade(self):
        shade = self.trunk_diameter * 1.56
        print(f"{self.name} provides {shade:.0f} square meters of shade")


class Vegetable(Plant):
    def __init__(
            self,
            name: str,
            height: int,
            age: int,
            harvest_season: str,
            nutritional_value: str
            ) -> None:
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def get_info(self) -> str:
        return f"{super().get_info()}, {self.harvest_season} harvest"

    def get_nutri_value(self) -> str:
        print(f"{self.name} is rich in {self.nutritional_value}")


if __name__ == "__main__":
    print("=== Garden Plan Types ===\n")

    rose = Flower("Rose", 25, 30, "red")
    sunflower = Plant("Sunflower", 80, 45)
    Oak = Tree("Oak", 500, 1825, 50)
    tomato = Vegetable("Tomato", 80, 90, "summer", "vitamin c")

    print(f"{rose.get_info()}")
    rose.bloom()
    print()

    print(f"{Oak.get_info()}")
    Oak.produce_shade()
    print()

    print(f"{tomato.get_info()}")
    tomato.get_nutri_value()
