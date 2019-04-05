"""
Advent of Code - Day 13
Author: Stefan Schneider
Github: StefSchneider
"""

path_file: str = "AoC2018_13_input.txt"
map_list: list = []
map_entry: tuple = (0, "", 0)  # order: x-pos, ypos of cart, direction, next direction intersection (0=left, 1=straight, 2=right)
carts: list = []
cart: tuple = () # use complex numbers for x- and y-position
current_cart: tuple = ()
next_intersection: int = 0
INITIALCARTS: dict = {"<": (-1, "-"),  # order key: direction cart, entry map
                      ">": (1, "-"),
                      "^": (-1j, "|"),
                      "v": (1j, "|")
                      }
INTERSECTION_DIRECTIONS: list = [-1, 0, 1]
DIRECTION_CHANGES: dict = {("+", -1, -1): 1j,
                           # order: 1: track, 2: direction cart, 3: direction intersection : new direction
                           ("+", -1, 0): -1,
                           ("+", -1, 1): -1j,
                           ("+", 1, -1): -1j,
                           ("+", 1, 0): 1,
                           ("+", 1, 1): 1j,
                           ("+", 1j, -1): 1,
                           ("+", 1j, 0): 1j,
                           ("+", 1j, 1): -1,
                           ("+", -1j, -1): -1,
                           ("+", -1j, 0): -1j,
                           ("+", -1j, 1): 1,
                           ("/", -1, 0): 1j,  # 3. value: 0 (straight)
                           ("/", 1, 0): -1j,
                           ("/", 1j, 0): -1,
                           ("/", -1j, 0): 1,
                           ("\\", -1, 0): -1j,
                           ("\\", 1, 0): +1j,
                           ("\\", 1j, 0): 1,
                           ("\\", -1j, 0): -1,
                           ("-", -1, 0): -1,
                           ("-", 1, 0): 1,
                           ("|", -1j, 0): -1j,
                           ("|", 1j, 0): 1j,
                           }
new_direction: int = 0
crash_position: tuple = (0, 0)
first_crash: bool = False
first_crash_position: tuple = (0, 0)
crashed: list = [] # list positions of crashed carts in cart list, set back to empty after deleting from list of carts

def move_cart(current_cart: tuple) -> tuple:
    new_track: str = ""
    direction_intersection: int = 0
    cart_position: complex = current_cart[0]
    direction: complex = current_cart[1]
    next_intersection: int = current_cart[2]
    cart_position += direction
    for i in range(0, len(map_list)):
        if map_list[i][0] == cart_position:
            new_track = map_list[i][1]
            if new_track == "+":
                direction_intersection = INTERSECTION_DIRECTIONS[next_intersection % 3]
                next_intersection += 1
            else:
                direction_intersection = 0
    direction = DIRECTION_CHANGES.get((new_track, direction, direction_intersection))
    current_cart = (cart_position, direction, next_intersection)

    return current_cart

# parse track and transfer in tuples
data_file = open(path_file).read().split("\n")
for y, line in enumerate(data_file):
    for x in range(0, len(line)):
        element = data_file[y][x]
        if element != " ":
            if element in INITIALCARTS: # add new cart to list of carts
                cart = (complex(x, y), INITIALCARTS.get(element)[0], next_intersection)
                carts.append(cart)
                element = INITIALCARTS.get(element)[1]
            map_entry = (complex(x, y), element)
            map_list.append(map_entry)

print("List of tracks:", map_list)

while len(carts) > 1:
    carts.sort(key=lambda carts: (carts[0].imag, carts[0].real)) # sort list of carts
    for i in range(0, len(carts)):
        count_double: int = 0
        current_cart = carts[i]
        carts[i] = move_cart(current_cart)
        for j in range(0, len(carts)):
            if carts[i][0] == carts[j][0] and carts[i] != carts[j]:
                crash_position = (int(carts[i][0].real), int(carts[i][0].imag))
                if not first_crash:
                    first_crash_position = crash_position
                    first_crash = True
                print("CRASH at", crash_position)
                crashed.append(i)
                crashed.append(j)

    # delete crashed carts from list of carts
    if len(crashed) > 0:
        crashed.sort()
        del carts[crashed[0]:crashed[1]+1] # add 1 to second number for slicing
        crashed = []

print("First crash at:", first_crash_position)
print("Position of last cart:", int(carts[0][0].real), ",", int(carts[0][0].imag))