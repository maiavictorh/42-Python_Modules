import alchemy

if __name__ == "__main__":
    red = "\33[31m"
    nc = "\33[0m"
    print("=== Sacred Scroll Mastery ===\n\n"
          "Testing direct module access:")

    print(f"alchemy.elements.create_fire(): {alchemy.elements.create_fire()}")
    print("alchemy.elements.create_water():", alchemy.elements.create_water())
    print("alchemy.elements.create_earth():", alchemy.elements.create_earth())
    print(f"alchemy.elements.create_air(): {alchemy.elements.create_air()}")

    print("\nTesting package-level access (controlled by __init__.py):")
    print(f"alchemy.create_fire(): {alchemy.create_fire()}")
    print(f"alchemy.create_water(): {alchemy.create_water()}")
    try:
        print(f"alchemy.create_fire(): {alchemy.create_earth()}")
    except AttributeError:
        print(f"alchemy.create_earth(): {red}AttributeError - not exposed{nc}")
    try:
        print(f"alchemy.create_air(): {alchemy.create_air()}")
    except AttributeError:
        print(f"alchemy.create_air(): {red}AttributeError - not exposed{nc}")

    print("\nPackage metadata:\n"
          f"Version: {alchemy.__version__}\n"
          f"Author: {alchemy.__author__}")
