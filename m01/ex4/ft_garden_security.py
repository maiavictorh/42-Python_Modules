#!/usr/bin/env python3

class SecurePlant:
    """
    A plant class that stores basic information, such as name, height and age.
    Note that this plant have methods to protect itself from undesired input.
    """
    def __init__(self, name: str, height: int, age: int) -> None:
        """
        This method is a constructor, used for initializing the
        object's attributes when created. As we need to protect the plant
        attributes, we'll use setters as methods to validate the parameters.

        :param self: refers to the object itself;
        :param name: plant's name;
        :type name: str
        :param height: plant's height, in centimeters;
        :type height: int
        :param age: plant's age, in days;
        :type age: int
        """
        self.name = name
        self._height = 0
        self._age = 0
        self.set_height(height)
        self.set_age(age)

    def set_height(self, height: int) -> None:
        """
        This protection method is for checking whether the height passed to
        the plant is positive or negative. If negative, an error message is
        displayed, if not, the height is updated.

        :param self: the plant itself;
        :param height: the intended height;
        :type height: int
        """
        if height >= 0:
            self._height += height
            print(f"Height updated: {self._height}cm [OK]")
        else:
            print(f"Invalid operation attempted: height {height}cm [REJECTED]")
            print("Security: Negative height rejected")

    def set_age(self, age: int) -> None:
        """
        This protection method is for checking whether the age passed to
        the plant is positive or negative. If negative, an error message is
        displayed, if not, the age is updated.

        :param self: the plant itself;
        :param age: the intended age;
        :type age: int
        """
        if age >= 0:
            self._age = age
            print(f"Age updated: {self._age} days [OK]")
        else:
            print(f"Invalid operation attempted: age {age} days [REJECTED]")
            print("Security: Negative age rejected\n")

    def get_height(self) -> int:
        """
        Access and returns a protected attribute: height.

        :param self: the plant itself;
        :return: the plant's height;
        :rtype: int
        """
        return self._height

    def get_age(self) -> int:
        """
        Access and returns a protected attribute: age.

        :param self: the plant itself;
        :return: the plant's age;
        :rtype: int
        """
        return self._age

    def get_info(self) -> str:
        """
        Returns information about the plant.

        :param self: the plant itself;
        :return: a formatted string;
        :rtype: str
        """
        return f"{self.name} ({self.get_height()}cm, {self.get_age()} days)"


if __name__ == "__main__":
    print("=== Garden Security System ===")

    print("Plant created: Rose")
    rose = SecurePlant("Rose", 25, 30)

    print()
    rose.set_height(-5)

    print(f"\nCurrent plant: {rose.get_info()}")
