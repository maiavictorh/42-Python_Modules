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

    def get_info(self) -> str:
        """
        Returns information about the plant.

        :param self: the plant itself;
        :return: a formatted string;
        :rtype: str
        """
        return f"{self.name} ({self.height}cm, {self.age} days)"


if __name__ == "__main__":
    print("=== Plant Factory Output ===")

    plants = [Plant("Rose", 25, 30),
              Plant("Oak", 200, 365),
              Plant("Cactus", 5, 90),
              Plant("Sunflower", 80, 45),
              Plant("Fern", 15, 120)]

    count = 0
    for plant in plants:
        print(f"Created: {plant.get_info()}")
        count += 1
    print(f"\nTotal plants created: {count}")
