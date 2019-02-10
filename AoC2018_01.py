"""
Advent of Code 2018 - Day 1
Author: Stefan Schneider
Github StefSchneider
"""

from itertools import cycle # just for Part 2

path_file: str = "AoC2018_01_input.txt"


# ---------- PART ONE ----------

print("Starting part one...\r")

resulting_frequency: int = 0

with open(path_file, 'r') as data_file:
    # use file with data for frequencies
    for line in data_file:
        resulting_frequency += int(line.strip())

print("Resulting frequency: ", resulting_frequency)
print("\r")


# ---------- PART TWO ----------

print("Starting part two...\r")

frequency: int = 0
frequencies: set = set((frequency,)) # creates a tuple of frequencies

with open(path_file, "r") as data_file:
    # use file with data for frequencies
    for line in cycle(data_file):
        frequency += int(line)
        if frequency in frequencies:
            break # stop cycle if first double frequency
        frequencies.add(frequency)

print("First double frequency:", frequency)