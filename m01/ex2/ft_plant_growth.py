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
        Displays information about the plant.

        :param self: the plant itself;
        """
        print(f"{self.name}: {self.height}cm, {self.age} days old")

    def days_aged(self, days: int) -> None:
        """
        Increases age (in days) to the plant.

        :param self: the plant itself;
        :param days: amount of days passed (of type int);
        """
        self.age += days

    def grow(self, centimeters: int) -> None:
        """
        Increases height (in centimeters) to the plant.

        :param self: the plant itself;
        :param days: amount of centimeters to grow (of type int);
        """
        self.height += centimeters


if __name__ == "__main__":
    rose = Plant("Rose", 25, 30)

    print("=== Day 1 ===")
    rose.get_info()

    days = 6
    print("=== Day 7 ===")
    rose.days_aged(days)
    rose.grow(days)
    rose.get_info()
    print(f"Growth this Week: +{days}cm")
