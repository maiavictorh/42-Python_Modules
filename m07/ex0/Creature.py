from abc import ABC, abstractmethod


class Creature(ABC):
    def __init__(self, name: str, creature_type: str) -> None:
        self.name = self.validate_str(name)
        self.creature_type = self.validate_type(creature_type)

    @abstractmethod
    def attack(self) -> str:
        pass

    def describe(self) -> str:
        format_type = ""

        i = 0
        for item in self.creature_type:
            format_type += item
            if i < len(self.creature_type) - 1:
                format_type += "/"
            i += 1

        return f"{self.name} is a {format_type} Creature"

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

    def validate_type(self, type_input: str) -> list[str]:
        if type(type_input) is not str or not type_input.strip():
            raise ValueError("Invalid Input.")

        valid_list = ["Fire", "Water", "Earth", "Air", "Flying"]
        type_list = []

        multiple_inputs = type_input.split("/")
        for input in multiple_inputs:
            clean_input = input.strip()
            if clean_input not in valid_list:
                raise ValueError("Invalid Type.")
            type_list.append(clean_input)
        return type_list


class Flameling(Creature):
    def __init__(self, name: str, creature_type: str) -> None:
        super().__init__(name, creature_type)

    def attack(self) -> str:
        return f"{self.name} uses Ember!"

    def describe(self) -> str:
        return super().describe()


class Pyrodon(Creature):
    def __init__(self, name: str, creature_type: str) -> None:
        super().__init__(name, creature_type)

    def attack(self) -> str:
        return f"{self.name} uses Flamethrower!"


class Aquabub(Creature):
    def __init__(self, name: str, creature_type: str) -> None:
        super().__init__(name, creature_type)


class Torragon(Creature):
    def __init__(self, name: str, creature_type: str) -> None:
        super().__init__(name, creature_type)
