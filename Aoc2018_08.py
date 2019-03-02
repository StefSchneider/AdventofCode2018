"""
Advent of Code - Day 8
Author: Stefan Schneider
Github: StefSchneider
"""


all_metadata: list = []
number_children: int = 0
number_metadata: int = 0

path_file: str = "AoC2018_08_input.txt"
data_file = list(map(int, open(path_file).read().split(" ")))


def parse_data():
    pass


print("Result of part one:", sum(all_metadata))


"""
rekursive Lösung:

wenn Anzahl Kinder = 0, dann metadaten zurücliefern

sonst Aufruf der Funktion, die neues Kind ausliest
"""