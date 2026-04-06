from ex0.Creature import Flameling, Pyrodon


if __name__ == "__main__":

    try:
        flameling = Flameling("Flameling", "Fire")
        pyrodon = Pyrodon("Pyrodon", "Fire/Flying")

        print("Testing factory")
        print(flameling.describe())
        print(flameling.attack())

        print(pyrodon.describe())
        print(pyrodon.attack())

    except ValueError as err:
        print(f"\33[31mERROR: {err}\33[0m")
