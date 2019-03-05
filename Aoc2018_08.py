"""
Advent of Code - Day 8
Author: Stefan Schneider
Github: StefSchneider
"""


all_metadata: list = []
number_children: int = 0
number_metadata: int = 0

path_file: str = "AoC2018_08_input_test.txt"
data_file = list(map(int, open(path_file).read().split(" ")))


def parse_node(pointer_start: int, children_current_hierachy: int) -> list:
    print("Start new node with pointer:", pointer_start, "children current hierachy:", children_current_hierachy)
    if children_current_hierachy > 0:
        number_children = data_file[pointer_start]
        pointer_start += 1
        number_metadata = data_file[pointer_start]
        pointer_start += 1
        print("Pointer start", pointer_start, "Number children", number_children, "Number metadata", number_metadata)
        if number_children == 0:
            for i in range(0, number_metadata):
                print("Pointer start in loop", pointer_start, "i",i, "Data:", data_file[pointer_start])
                all_metadata.append(data_file[pointer_start])
                pointer_start += 1
            print(all_metadata)
        else:
            parse_node(pointer_start, data_file[pointer_start])
        children_current_hierachy -= 1
        parse_node(pointer_start, children_current_hierachy)

    return all_metadata


parse_node(0, data_file[0])
print(sum(all_metadata))


"""
def parse_metadata(pointer_start, number_children):
    jump: int = 0
    print("pointer start", pointer_start)
    for j in range(0, number_children):
        print("Number children", data_file[pointer_start])
        if data_file[pointer_start] == 0:
            number_metadata = data_file[pointer_start+1]
            print("Number Metadata", number_metadata)
            for i in range(0, number_metadata+1):
                all_metadata.append(data_file[pointer_start+i+1])
                print(all_metadata)
            jump += number_metadata+1
        else:
            jump += 2
            parse_metadata(pointer_start+jump, data_file[pointer_start+jump])

    print(all_metadata)
    return all_metadata

parse_metadata((0), data_file[0])
print("Result of part one:", sum(all_metadata))
"""


"""
rekursive Lösung:

wenn Anzahl Kinder = 0, dann metadaten zurücliefern

sonst Aufruf der Funktion, die neues Kind ausliest
"""