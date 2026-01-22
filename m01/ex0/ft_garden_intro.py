class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def get_info(self) -> None:
        print(f"Plant: {self.name}")
        print(f"Height: {self.height}cm")
        print(f"Age: {self.age} days")


if __name__ == "__main__":
    print("=== Welcome to My Garden ===")
    rose = Plant("Rose", 25, 30)
    rose.get_info()
    print("\n=== End of Program ===")
