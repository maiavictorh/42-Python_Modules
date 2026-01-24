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
        Returns information about the plant
        (now in a another different format :/).

        :param self: the plant itself;
        :return: a formatted string;
        :rtype: str
        """
        return (f"{self.name} ({type(self).__name__}):"
                f" {self.height}cm, {self.age} days")


class Flower(Plant):
    """
    A different kind of Plant, which stores more information,
    and have it's own methods.
    """
    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        """
        Works just like the Plant constructor, but have an extra
        characteristic. Note that this class inherits the Plant attributes.

        :param color: flower's color;
        :type color: str
        """
        super().__init__(name, height, age)
        self.color = color

    def get_info(self) -> str:
        """
        Returns information about the flower,
        but adding specific attributes.

        :param self: the flower itself;
        :return: a formatted string;
        :rtype: str
        """
        return f"{super().get_info()}, {self.color} color"

    def bloom(self) -> None:
        """
        Prints a message that indicates the flower is blooming.

        :param self: the flower itself;
        """
        print(f"{self.name} is blooming beautifully!")


class Tree(Plant):
    """
    Another kind of plant, which also stores different information,
    and have it's own methods.
    """
    def __init__(
            self,
            name: str,
            height: int,
            age: int,
            trunk_diameter: int
            ) -> None:
        """
        Works just like the Plant constructor, but have an extra
        characteristic. Note that this class inherits the Plant attributes.

        :param trunk_diameter: tree's trunk diameter (used for calculating
        it's shade area);
        :type trunk_diameter: int
        """
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def get_info(self) -> str:
        """
        Returns information about the tree,
        but adding specific attributes.

        :param self: the tree itself;
        :return: a formatted string;
        :rtype: str
        """
        return f"{super().get_info()}, {self.trunk_diameter}cm diameter"

    def produce_shade(self) -> None:
        """
        Calculates and displays the shade area produced by the tree,
        based on the trunk diameter.

        :param self: the tree itself;
        """
        shade = self.trunk_diameter * 1.56
        print(f"{self.name} provides {shade:.0f} square meters of shade")


class Vegetable(Plant):
    """
    Another kind of plant, which also stores different information,
    and have it's own methods.
    """
    def __init__(
            self,
            name: str,
            height: int,
            age: int,
            harvest_season: str,
            nutritional_value: str
            ) -> None:
        """
        Works just like the Plant constructor, but have extra characteristics.
        Note that this class inherits the Plant attributes.

        :param harvest_season: vegetable's respective harvest season;
        :type harvest_season: str
        :param nutritional_value: vegetable's nutritional value, such as
        vitamins, etc;
        """
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def get_info(self) -> str:
        """
        Returns information about the vegetable,
        but adding specific attributes.

        :param self: the vegetable itself;
        :return: a formatted string;
        :rtype: str
        """
        return f"{super().get_info()}, {self.harvest_season} harvest"

    def get_nutri_value(self) -> None:
        """
        Display information about the vegetable's nutrients.

        :param self: the vegetable itself;
        """
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
