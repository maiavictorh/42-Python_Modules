#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def get_info(self) -> str:
        return (f"{self.name} ({type(self).__name__}):"
                f" {self.height}cm, {self.age} days")


class Flower(Plant):
    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color = color

    def get_info(self) -> str:
        return f"{super().get_info()}, {self.color} color"

    def bloom(self) -> None:
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

    def produce_shade(self) -> None:
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

    def get_nutri_value(self) -> None:
        print(f"{self.name} is rich in {self.nutritional_value}")


if __name__ == "__main__":
    print("=== Garden Plan Types ===\n")

    rose = Flower("Rose", 25, 30, "red")
    sunflower = Flower("Sunflower", 80, 45, "yellow")
    oak = Tree("Oak", 500, 1825, 50)
    pine = Tree("Pine", 7400, 1000, 91)
    tomato = Vegetable("Tomato", 80, 90, "summer", "vitamin C")
    carrot = Vegetable("Carrot", 62, 70, "autumn", "vitamin A")

    print(f"{rose.get_info()}")
    rose.bloom()
    print()
    print(f"{sunflower.get_info()}")
    sunflower.bloom()
    print()

    print(f"{oak.get_info()}")
    oak.produce_shade()
    print()
    print(f"{pine.get_info()}")
    pine.produce_shade()
    print()

    print(f"{tomato.get_info()}")
    tomato.get_nutri_value()
    print()
    print(f"{carrot.get_info()}")
    carrot.get_nutri_value()
    print()
