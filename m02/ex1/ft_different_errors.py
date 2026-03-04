#!/usr/bin/env python3

def garden_operations(error: int) -> None:
    if error == 0:
        print("\nTesting ValueError...")
        try:
            temp = int("abc")
        except ValueError as err:
            print(f"Caught {type(err).__name__}: {err}")
    elif error == 1:
        print("\nTesting ZeroDivisionError...")
        try:
            temp = 10 / 0
            print({temp})
        except ZeroDivisionError as err:
            print(f"Caught {type(err).__name__}: {err}")
    elif error == 2:
        print("\nTesting FileNotFoundError...")
        try:
            open("missing.txt")
        except FileNotFoundError as err:
            print(f"Caught {type(err).__name__}: {err}")
    elif error == 3:
        print("\nTesting KeyError...")
        try:
            rose = {"color": "red"}
            print(rose["missing_plant"])
        except KeyError as err:
            print(f"Caught {type(err).__name__}: {err}")


def test_error_types() -> None:
    print("=== Garden Error Types Demo ===")

    i = 0
    while i < 4:
        garden_operations(i)
        i += 1

    print("\nTesting multiple errors together...")
    try:
        temp = int("abc")
        temp /= 0
        open("anothermissing.txt")
        sunflower = {"name": "sunflower"}
        print({sunflower["color"]})
    except (ValueError, ZeroDivisionError, FileNotFoundError, KeyError):
        print("Caught an error, but program continues!")

    print("\nAll error types tested succesfully!")


if __name__ == "__main__":
    test_error_types()
