#!/usr/bin/env python3
import sys

if __name__ == "__main__":
    print("=== Player Score Analytics ===")
    args = sys.argv
    args_len = len(args)
    nums: list = []
    if args_len < 2:
        print("No scores provided. Usage: "
              f"python3 {args[0]} <score1> <score2> ...")
    else:
        try:
            i = 1
            while i < args_len:
                nums.append(int(args[i]))
                i += 1
        except ValueError:
            print(f"Cannot add {args[i]}: invalid number!")
        print(f"Scores processed: {nums}")
        print(f"Total players: {len(nums)}")
        print(f"Total score: {sum(nums)}")
        print(f"Average score: {sum(nums) / len(nums)}")
        print(f"High score: {max(nums)}")
        print(f"Low score: {min(nums)}")
        print(f"Score range {max(nums) - min(nums)}")
