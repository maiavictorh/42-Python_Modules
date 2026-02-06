#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.points = 7
        self.set_height(height)
        self.set_age(age)

    @staticmethod
    def validate_height(height: int) -> bool:
        return height >= 0

    @staticmethod
    def validate_age(age: int) -> bool:
        return age >= 0

    def set_height(self, height: int) -> bool:
        if self.validate_height(height):
            self.height = height
            return True
        return False

    def set_age(self, age: int) -> bool:
        if self.validate_age(age):
            self.age = age
            return True
        return False

    def grow(self, amount: int) -> str:
        self.height += amount
        return f"{self.name} grew {amount}cm"

    def get_info(self) -> str:
        return f"{self.name}: {self.height}cm"


class FloweringPlant(Plant):
    def __init__(
            self,
            name: str,
            height: int,
            age: int,
            color: str,
            blooming: bool
            ) -> None:
        super().__init__(name, height, age)
        self.color = color
        self.points = 21
        self.blooming = blooming

    def bloom(self) -> str:
        if self.blooming:
            return " (blooming)"
        return ""

    def get_info(self) -> str:
        return f"{super().get_info()}, {self.color} flowers{self.bloom()}"


class PrizeFlower(FloweringPlant):
    def __init__(
            self,
            name: str,
            height: int,
            age: int,
            color: str,
            blooming: bool
            ) -> None:
        super().__init__(name, height, age, color, blooming)
        self.prize_points = 42

    def get_info(self) -> str:
        return f"{super().get_info()}, Prize points: {self.prize_points}"


class Garden:
    def __init__(self, name: str) -> None:
        self.name = name
        self.plants: list[Plant] = []

    def add_plant(self, plant: Plant) -> str:
        self.plants.append(plant)
        return f"Added {plant.name} to {self.name} garden"

    def grow_all(self, amount: int) -> int:
        print(f"{self.name} is helping all plants grow...")
        total = 0
        for plant in self.plants:
            total += amount
            print(f"{plant.grow(amount)}")
        return total


class GardenManager:
    def __init__(self) -> None:
        self.gardens: list[Garden] = []

    def add_garden(self, garden: Garden) -> None:
        self.gardens.append(garden)

    class GardenStats:
        @staticmethod
        def count_gardens(gardens: list[Garden]) -> str:
            count = 0
            for garden in gardens:
                count += 1
            return f"Total gardens managed: {count}"

        @staticmethod
        def count_plants(plants: list[Plant]) -> str:
            count = 0
            for plant in plants:
                count += 1
            return f"Plants added: {count}"

        @staticmethod
        def count_by_type(plants: list[Plant]) -> str:
            reg = 0
            flo = 0
            prz = 0
            for plant in plants:
                if isinstance(plant, PrizeFlower):
                    prz += 1
                elif isinstance(plant, FloweringPlant):
                    flo += 1
                elif isinstance(plant, Plant):
                    reg += 1
            return (f"Plant types: {reg} regular, {flo} flowering,"
                    f" {prz} prize flowers")

        @staticmethod
        def validate_heights(gardens: list[Garden]) -> bool:
            for garden in gardens:
                for plant in garden.plants:
                    if not Plant.validate_height(plant.height):
                        return False
            return True

        @staticmethod
        def total_points(garden: Garden) -> int:
            total_points = 0
            for plant in garden.plants:
                total_points += plant.points
            return total_points

    @classmethod
    def create_garden_network(cls) -> 'GardenManager':
        return cls()


if __name__ == "__main__":
    print("=== Garden Management System Demo ===\n")

    oak = Plant("Oak Tree", 100, 1800)
    rose = FloweringPlant("Rose", 25, 17, "red", True)
    sunflower = PrizeFlower("Sunflower", 50, 21, "yellow", False)
    pine = Plant("Pine", 7400, 1000)
    carrot = Plant("Carrot", 62, 70)

    victor: GardenManager = GardenManager.create_garden_network()
    alice = Garden("Alice")
    bob = Garden("Bob")
    victor.add_garden(alice)
    victor.add_garden(bob)

    print(f"{alice.add_plant(oak)}")
    print(f"{alice.add_plant(rose)}")
    print(f"{alice.add_plant(sunflower)}")
    bob.add_plant(pine)
    bob.add_plant(carrot)
    print()

    total_growth = alice.grow_all(5)
    print()

    print(f"=== {alice.name}'s Garden Report ===")
    print("Plants in garden:")
    print(f"- {oak.get_info()}")
    print(f"- {rose.get_info()}")
    print(f"- {sunflower.get_info()}\n")

    total_plants = victor.GardenStats.count_plants(alice.plants)
    bob_points = victor.GardenStats.total_points(bob)
    valid_heights = GardenManager.GardenStats.validate_heights(victor.gardens)
    alice_points = victor.GardenStats.total_points(alice)

    print(f"{total_plants}, Total growth: {total_growth}cm")
    print(f"{victor.GardenStats.count_by_type(alice.plants)}")
    print()

    print(f"Height validation test: {valid_heights}")
    print(f"Garden scores - {alice.name}: {alice_points}, Bob: {bob_points}")
    print(victor.GardenStats.count_gardens(victor.gardens))
