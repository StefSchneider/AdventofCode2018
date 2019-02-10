"""
Advent of Code 2018 - Day 03
Author: Stefan Schneider
Github: StefSchneider
"""

import numpy


class Claim:

    list_ids: list = []

    def __init__(self):
        pass

    def __str__(self):

        return list_ids

    def add_id(self, id):
        self.id = id
        list_ids.append(self.id)

        return list_ids


path_file: str = 'AoC2018_03_input.txt'
id: str = ''
coordinates_size: str = ''
coordinates: str = ''
size: str = ''
x_pos: int = 0 # part of coordinates
y_pos: int = 0 # part of coordinates
x_size: int = 0 # part of size
y_size: int = 0 # part of size
list_claims = []
overlap: int = 0

fabric = [[list_claims[:] for j in range(1000)] for i in range(1000)]

with open(path_file, 'r') as data_file:
    for line in data_file:
        id, coordinates_size = line.strip().split(' @ ')
        coordinates, size = coordinates_size.strip().split(': ')
        x_pos, y_pos = coordinates.strip().split(',')
        x_size, y_size = size.strip().split('x')
        print('ID: ', id, 'Positions: ', x_pos, y_pos, 'Size: ', x_size, y_size)
        x_size = int(x_size)
        y_size = int(y_size)
        x_pos = int(x_pos)
        y_pos = int(y_pos)
        for count_x in range(0, x_size):
            for count_y in range(0, y_size):
                fabric[x_pos+count_x][y_pos+count_y].append(id)
#                print(x_pos+count_x, y_pos+count_y)
#                print(fabric[x_pos+count_x][y_pos+count_y])


for i in range(0, 1000):
    for j in range(0, 1000):
        if len(fabric[i][j]) > 1:
            overlap += 1
            print(overlap)
