#!/usr/bin/env python3

def garden_operations(error: str) -> None:
    if error == "ValueError":
        temp = int("abc")
    elif error == "ZeroDivisionError":
        temp = 42 / 0
        print({temp})
    elif error == "FileNotFoundError":
        open("missing.txt")
    elif error == "KeyError":
        rose = {"color": "red"}
        print(rose["missing_plant"])
    else:
        print(f"{error} is not supported yet!")


def test_error_types() -> None:
    print("=== Garden Error Types Demo ===")
    errors = ["ValueError", "ZeroDivisionError",
              "FileNotFoundError", "KeyError"]
    for error in errors:
        print(f"Testing {error}...")
        try:
            garden_operations(error)
        except (ValueError, ZeroDivisionError,
                FileNotFoundError, KeyError) as err:
            print(f"Caught {type(err).__name__}: {err}")
        finally:
            print()
    print("All error types tested succesfully!")


if __name__ == "__main__":
    test_error_types()
