#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = 0
        self.age = 0
        self.set_height(height)
        self.set_age(age)

    def set_height(self, height: int) -> bool:
        if height >= 0:
            self.height += height
            return True
        else:
            return False

    def set_age(self, age: int) -> bool:
        if age >= 0:
            self.age = age
            return True
        else:
            return False

    def grow(self) -> str:
        self.set_height(1)
        return f"{self.name} grew 1cm"

    def get_info(self) -> str:
        return f"{self.name}: {self.height}cm"


class Flowering(Plant):
    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color = color

    def get_info(self) -> str:
        return f"{super().get_info()}, {self.color} flowers (blooming)"


class PrizeFlower(Flowering):
    def __init__(
            self,
            name: str,
            height: int,
            age: int,
            color: str,
            prize_points: int):
        super().__init__(name, height, age, color)
        self.prize_points = prize_points

    def get_info(self):
        return f"{super().get_info()}, Prize points: {self.prize_points}"


if __name__ == "__main__":
    print("=== Garden Management System Demo ===\n")

    oak = Plant("Oak Tree", 100, 1800)
    rose = Flowering("Rose", 25, 17, "red")
    sunflower = PrizeFlower("Sunflower", 50, 21, "yellow", 10)
    print(f"{oak.get_info()}")
    print(f"{rose.get_info()}")
    print(f"{sunflower.get_info()}")
