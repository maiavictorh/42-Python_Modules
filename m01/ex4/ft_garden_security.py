#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self._height = 0
        self._age = 0
        self.set_height(height)
        self.set_age(age)

    def set_height(self, height: int) -> None:
        if height >= 0:
            self._height += height
            print(f"Height updated: {self._height}cm [OK]")
        else:
            print(f"Invalid operation attempted: height {height}cm [REJECTED]")
            print("Security: Negative height rejected")

    def set_age(self, age: int) -> None:
        if age >= 0:
            self._age = age
            print(f"Age updated: {self._age} days [OK]")
        else:
            print(f"Invalid operation attempted: age {age} days [REJECTED]")
            print("Security: Negative age rejected\n")

    def get_height(self) -> int:
        return self._height

    def get_age(self) -> int:
        return self._age

    def get_info(self) -> str:
        return f"{self.name} ({self.get_height()}cm, {self.get_age()} days)"


if __name__ == "__main__":
    print("=== Garden Security System ===")

    print("Plant created: Rose")
    rose = Plant("Rose", 25, 30)

    print("")
    rose.set_height(-5)

    print(f"\nCurrent plant: {rose.get_info()}")
