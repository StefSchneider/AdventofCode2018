"""
Advent of Code - Day 11
Author: Stefan Schneider
Github: StefSchneider
"""

import numpy

grid_serial_number: int = 3613 # input
grid_energies: dict = {} # {[top, left]:grid_energy}
max_grid: tuple = (0 ,0, 0)
max_grid_energy: int = 0



def calculate_power_level(x_coordinate: int, y_coordinate: int, grid_serial_number: int) -> int:
    rack_ID: int = 0
    power_level: int = 0
    hundreds_digit: int = 0

    rack_ID = x_coordinate + 10  # step 1
    power_level = rack_ID * y_coordinate  # step 2
    power_level += grid_serial_number  # step 3
    power_level *= rack_ID
    hundreds_digit = power_level // 100  # step 4
    power_level = int(str(hundreds_digit)[-1])
    power_level -= 5  # step 5#

    return power_level


def calculate_grid_energy(window) -> int:
    grid_energy: int = 0
    grid_energy = numpy.sum(window)

    return grid_energy


grid = numpy.empty((300, 300), int)
for y in range(0, 300):
    for x in range(0, 300):
        grid[x][y] = calculate_power_level(x+1, y+1, grid_serial_number)


for size in range(1, 301):
    grid_energies = {}
    for i in range(0, 301-size):
        for j in range(0, 301-size):
            window_energy = calculate_grid_energy(grid[j:j+size, i:i+size])
            grid_energies[(j+1,i+1), size] = window_energy
    max_grid = [(k, grid_energies[k]) for k in sorted(grid_energies, key=grid_energies.get, reverse=True)][0]
    print(max_grid)
    if max_grid[1] > max_grid_energy:
        print("New high energy:", max_grid)
        max_grid_energy = max_grid[1]


