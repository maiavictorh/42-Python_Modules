class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def display_info(self):
        print(f"Plant: {self.name}")
        print(f"Height: {self.height}cm")
        print(f"Age: {self.age} days")


def main():
    print("=== Welcome to My Garden ===")
    rose = Plant("Rose", 25, 30)
    rose.display_info()
    print("\n=== End of Program ===")


if __name__ == "__main__":
    main()
