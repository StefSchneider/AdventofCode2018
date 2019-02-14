"""
Advent of Code - Day 11
Author: Stefan Schneider
Github: StefSchneider
"""

grid_serial_number: int = 3613 # input
grid: list = [[]]

grid_energies: dict = {} # {[top, left]:grid_energy}

class Cell():

    def __init__(self, x_coordinate, y_coordinate):
        self.coordinate = x_coordinate
        self.coordinate = y_coordinate
        power_level: int = 0

 #   def __str__(self, power_level):
  #      self.power_level = power_level
#
 #       return self.power_level

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
        power_level -= 5 # step 5

        return power_level


    def calculate_grid_energy(self, x_coordinate: int, y_coordinate: int) -> int:
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        grid_energy: int = 0
        for i in range(0, 3):
            for j in range(0,3):
                grid_energy += cell[i][j].power_level

        return grid_energy


for i in range(0, 30):
    for j in range(0,30):
        print(i,j)
        grid_cell = Cell(i+1, j+1)
        grid[i][j].insert(i)
 #       grid.append(grid_cell)

print(grid[0], type(grid[0]))


