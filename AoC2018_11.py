"""
Advent of Code - Day 11
Author: Stefan Schneider
Github: StefSchneider
"""

grid_serial_number: int = 3613 # input

grid: list = []

grid_energies: dict = {} # {[top, left]:grid_energy}

class Cell():

    def __init__(self, x_coordinate, y_coordinate):
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        self.power_level: int = 0

    def __str__(self):

        return self.x_coordinate, self.y_coordinate, self.power_level

    def calculate_power_level(self, x_coordinate: int, y_coordinate: int, grid_serial_number: int) -> int:
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        self.grid_serial_number = grid_serial_number
        rack_ID: int = 0
        power_level: int = 0
        hundreds_digit: int = 0

        rack_ID = x_coordinate + 10 # step 1
        power_level = rack_ID * y_coordinate # step 2
        power_level += grid_serial_number # step 3
        power_level *= rack_ID
        hundreds_digit = power_level // 100 #step 4
        power_level = int(str(hundreds_digit)[-1])
        power_level -= 5 # step 5#

        return power_level


    def calculate_grid_energy(self, x_coordinate: int, y_coordinate: int) -> int:
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        self.grid_energy: int = 0
        for x in range(0, 3):
            for y in range(0,3):
                self.grid_energy += grid[x_coordinate+x][y_coordinate+y].power_level

        return self.grid_energy



for i in range(0, 300):
    column = []
    for j in range(0,300):
        grid_cell = Cell(i+1, j+1)
        column.append(grid_cell)
    grid.append(column)


for x in range(1, 301):
    for y in range(1, 301):
        grid[x-1][y-1].power_level = grid_cell.calculate_power_level(x, y, grid_serial_number)


for i in range(0, 297):
    for j in range(0, 297):
        window_energy = grid_cell.calculate_grid_energy(i+1, j+1)
        grid_energies[(i+1,j+1)] = window_energy


max_energy = sorted(grid_energies.values(), reverse = True)[0]

s = [(k, grid_energies[k]) for k in sorted(grid_energies, key=grid_energies.get)]
for k, v in s:
    print(k, v)

print(max_energy)