#!/usr/bin/env python3
# import sys
import math


def dist_calc(pos1: tuple, pos2: tuple) -> int:
    return math.sqrt((pos2[0] - pos1[0]) ** 2
                     + (pos2[1] - pos1[1]) ** 2
                     + (pos2[2] - pos1[2]) ** 2)


if __name__ == "__main__":
    print("=== Game Coordinate System ===\n")

    pos0 = (0, 0, 0)
    pos1 = (10, 20, 5)
    print(f"Position created: {pos1}")
    print(f"Distance between {pos0} and {pos1}: {dist_calc(pos0, pos1):.2f}")

    pos2_str = "3,4,0"
    temp = pos2_str.split(",")
    pos2 = (int(temp[0]), int(temp[1]), int(temp[2]))
    print(f"\nParsing coordinates: \"{pos2_str}\"")
    print(f"Parsed position: {pos2}")
    print(f"Distance between {pos0} and {pos2}: {dist_calc(pos0, pos2)}")

    pos3_str = "abc,def,ghi"
    print(f"\nParsing invalid coordinates: \"{pos3_str}\"")
    try:
        temp = pos3_str.split(",")
        pos3 = (int(temp[0]), int(temp[0]), int(temp[0]))
    except ValueError as err:
        print(f"Error parsing coordinates: {err}")
        print(f"Error details - Type: {type(err).__name__}, Args: (\"{err}\")")

    pos = (3, 4, 0)
    (x, y, z) = pos
    print("\nUnpacking demonstration:")
    print(f"Player at x={pos[0]}, y={pos[1]}, z={pos[2]}")
    print(f"Coordinates: X={x}, Y={y}, Z={z}")
