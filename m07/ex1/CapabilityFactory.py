from ex0 import CreatureFactory
from .Capability import Sproutling, Bloomelle, Shiftling, Morphagon


class HealingCreatureFactory(CreatureFactory):
    def __init__(self) -> None:
        pass

    def create_base() -> Sproutling:
        return Sproutling("Sproutling", "Grass")

    def create_evolved() -> Bloomelle:
        return Bloomelle("Bloomelle", "Grass/Fairy")


class TransformCreatureFactory(CreatureFactory):
    def __init__(self) -> None:
        pass

    def create_base() -> Shiftling:
        return Shiftling("Shiftling", "Normal")

    def create_evolved() -> Morphagon:
        return Morphagon("Morphagon", "Normal/Dragon")
