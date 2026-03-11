#!/usr/bin/env python3
import sys

if __name__ == "__main__":
    print("=== Command Quest ===")
    args = sys.argv
    args_len = len(args)
    if args_len < 2:
        print("No arguments provided!")
        print(f"Program name: {args[0]}")
        print(f"Total arguments: {args_len}")
    else:
        print(f"Program name: {args[0]}")
        print(f"Arguments received: {args_len - 1}")
        i = 1
        while i < args_len:
            print(f"Argument {i}: {args[i]}")
            i += 1
        print(f"Total arguments: {args_len}")
