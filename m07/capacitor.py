from ex1 import HealingCreatureFactory, TransformCreatureFactory


if __name__ == "__main__":

    print("Testing Creature with healing capability base:")
    sproutling = HealingCreatureFactory.create_base()
    print(sproutling.describe())
    print(sproutling.attack())
    print(sproutling.heal())
    print(" evolved:")
    bloomelle = HealingCreatureFactory.create_evolved()
    print(bloomelle.describe())
    print(bloomelle.attack())
    print(bloomelle.heal("cu"))

    shiftling = TransformCreatureFactory.create_base()
