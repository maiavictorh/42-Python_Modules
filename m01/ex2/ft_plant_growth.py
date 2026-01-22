class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def get_info(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age} days old")

    def days_aged(self, days: int) -> None:
        self.age += days

    def grow(self, centimeters: int) -> None:
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
