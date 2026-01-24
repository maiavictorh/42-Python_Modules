#!/usr/bin/env python3

class Plant:
    """
    A plant class that stores basic information, such as name, height and age.
    """
    def __init__(self, name: str, height: int, age: int) -> None:
        """
        This method is a constructor, used for initializing the
        object's attributes when created.

        :param self: refers to the object itself;
        :param name: plant's name;
        :type name: str
        :param height: plant's height, in centimeters;
        :type height: int
        :param age: plant's age, in days;
        :type age: int
        """
        self.name = name
        self.height = height
        self.age = age

    def get_info(self) -> None:
        """
        Displays information about the plant
        (now in a different format :/).

        :param self: the plant itself;
        """
        print(f"{self.name}: {self.height}cm, {self.age} days old")


if __name__ == "__main__":
    print("=== Garden Plant Registry ===")
    rose = Plant("Rose", 25, 30)
    sunflower = Plant("Sunflower", 80, 45)
    cactus = Plant("Cactus", 15, 120)

    plants = [rose, sunflower, cactus]
    for plant in plants:
        plant.get_info()
