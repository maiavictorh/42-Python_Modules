from ex0.Creature import Flameling


if __name__ == "__main__":

    try:
        flameling = Flameling("Flameling", "Fire")

        print("Testing factory")
        print(flameling.describe())
    except ValueError as err:
        print(f"\33[31mERROR: {err}\33[0m")
