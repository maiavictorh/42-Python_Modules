class Plant:
    def __init__(self, name: str) -> None:
        self._name = name
        self.__height = 0
        self.__age = 0

    def get_info(self) -> str:
        return f"{self._name} ({self.__height}cm, {self.__age} days)"

    def set_height(self, height: int) -> None:
        if (height < 0):
            print(f"Invalid operation attempted: height {height} [REJECTED]")
            print("Security: Negative height rejected")
        else:
            print(f"Height updated: {height}")


if __name__ == "__main__":
    print("=== Plant Security System ===")

    rose = Plant("Rose", 25, 30),
