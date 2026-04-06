from abc import ABC, abstractmethod


class Creature(ABC):
    def __init__(self, name: str, type: str | list[str]) -> None:
        self.name = self.validate_str(name)
        self.type = self.validate_type(type)

    @abstractmethod
    def attack(self) -> None:
        pass

    def describe(self) -> str:
        return f"{self.name} is a {self.type} Creature"

    @staticmethod
    def validate_str(input: str) -> str:
        if type(input) is not str or not input.strip():
            raise ValueError("Invalid Input.")
        return input

    @staticmethod
    def validate_int(input: int) -> int:
        if type(input) is not int or input < 0:
            raise ValueError("Invalid Input.")
        return input

    def validate_type(self, type_input: str) -> None:
        valid = ["Fire", "Water", "Earth", "Air", "Flying"]

        for type in valid:
            if type_input == type:
                self.type = type_input
            else:
                raise ValueError("Invalid type.")


class Flameling(Creature):
    def __init__(self, name: str, type: str) -> None:
        super().__init__(name, type)

    def attack(self) -> None:
        pass

    def describe(self) -> str:
        return super().describe()


class Pyrodon(Creature):
    def __init__(self, name: str, type: str) -> None:
        super().__init__(name, type)


class Aquabub(Creature):
    def __init__(self, name: str, type: str) -> None:
        super().__init__(name, type)


class Torragon(Creature):
    def __init__(self, name: str, type: str) -> None:
        super().__init__(name, type)
