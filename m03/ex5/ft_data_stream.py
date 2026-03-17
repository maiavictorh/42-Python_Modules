#!/usr/bin/env python3

import time
from typing import Generator


def generate_events(total_events: int) -> Generator[str, int, str]:
    players = ["alice", "bob", "charlie", "michael jackson"]
    events = ["killed monster", "found treasure", "leveled up"]

    for i in range(total_events):
        player = players[i % len(players)]
        level = i % 30 + 1
        event_type = events[i % len(events)]

        yield (player, level, event_type)


def process_stream(n: int) -> None:
    i = 1
    level_up = 0
    high_level = 0
    total_events = 0
    treasure_events = 0
    begin = time.time()
    stream = generate_events(n)

    print(f"Processing {n} game events...\n")

    for event in stream:
        total_events += 1
        player, level, event_type = event
        print(f"Event {i}: Player {player} (level {level}) {event_type}")
        if level >= 10:
            high_level += 1
        if event_type == "found treasure":
            treasure_events += 1
        if event_type == "leveled up":
            level_up += 1
        i += 1

    end = time.time()
    print("\n=== Stream Analytics ===")
    print(f"Total events processed: {total_events}")
    print(f"High-level players (10+): {high_level}")
    print(f"Treasure events: {treasure_events}")
    print(f"Level-up events: {level_up}")
    print("\nMemory usage: Constant (streaming)")
    print(f"Processing time: {end - begin:.3f} seconds")


def fibonacci() -> Generator[int, None, None]:
    i = 0
    j = 1
    while True:
        yield i
        next = i + j
        i = j
        j = next


def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1

    return True


def generate_prime() -> Generator[int, None, None]:
    i = 2
    while True:
        if is_prime(i):
            yield i
        i += 1


if __name__ == "__main__":
    print("=== Game Data Stream Processor ===\n")
    process_stream(10)

    print("\n=== Generator Demonstration ===")
    print("Fibonacci sequence (first 10):", end=" ")
    fibo = fibonacci()
    for i in range(0, 10):
        print(f"{next(fibo)}", end="")
        if i < 9:
            print(",", end=" ")
    print("\nPrime numbers (first 5):", end=" ")
    prime = generate_prime()
    for i in range(0, 5):
        print(f"{next(prime)}", end="")
        if i < 4:
            print(",", end=" ")
    print()
