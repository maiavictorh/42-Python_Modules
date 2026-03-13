#!/usr/bin/env python3
import sys


class NegativeValue(Exception):
    pass


def parse_args(args: list[str]) -> dict:
    inventory = {}
    for arg in args:
        if ':' in arg:
            key, value = arg.split(":")
            try:
                temp = int(value)
                if temp < 0:
                    raise NegativeValue("Argument must be positive!")
                inventory[key] = temp
            except (ValueError, NegativeValue) as err:
                print(f"Error: {err}")
    return inventory


if __name__ == "__main__":
    args = sys.argv
    inventory = parse_args(args)
    print("=== Inventory System Analysis ===")
    total = 0
    for value in inventory.values():
        total += value
    print(f"Total items in inventory: {total}")
    print(f"Unique item types: {len(inventory.keys())}")

    print("\n=== Current Inventory ===")
    for key, value in inventory.items():
        print(f"{key}: {value} units ({value / total * 100:.1f}%)")
    print("\n=== Inventory Statistics ===")
    key_abundant = None
    value_abundant = 0
    for key, value in inventory.items():
        if value > value_abundant:
            key_abundant = key
            value_abundant = value
    print(f"Most abundant: {key_abundant} ({value_abundant} units)")
    for key, value in inventory.items():
        if value < value_abundant:
            key_abundant = key
            value_abundant = value
    print(f"Least abundant: {key_abundant} ({value_abundant} units)")
    print("\n=== Item Categories ===")
    moderate = {}
    scarce = {}
    for key, value in inventory.items():
        if value > 3:
            moderate[key] = value
        else:
            scarce[key] = value
    print(f"Moderate: {moderate}\nScarce: {scarce}")
    print("\n=== Management Suggestions ===")
    restock = []
    for key, value in inventory.items():
        if value < 2:
            restock.append(key)
    print(f"Restock needed: {restock}")
    print("\n=== Dictionary Properties Demo ===")
    keys = list(inventory.keys())
    values = list(inventory.values())
    print(f"Dictionary keys: {keys}")
    print(f"Dictionary values: {values}")
    print(f"Sample lookup - 'sword' in inventory: {'sword' in inventory}")
