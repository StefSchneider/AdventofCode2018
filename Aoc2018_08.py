"""
Advent of Code - Day 8
Author: Stefan Schneider
Github: StefSchneider
"""


#all_metadata: list = []
#number_children: int = 0
#number_metadata: int = 0

path_file: str = "AoC2018_08_input_test.txt"
data_file = list(map(int, open(path_file).read().split(" "))) # convert list of strings in list of integers


def parse_node(data_file):
    number_children = data_file[0]
    number_metadata = data_file[1]
    data_file = data_file[2:]
    sum_metadata: int = 0
#    all_metadata: list = []
    metadata: int = 0
    print(number_children, number_metadata, data_file)
#    print(all_metadata)
    for i in range(0, number_children):
        metadata, data_file = parse_node(data_file)
        sum_metadata += metadata

    sum_metadata += sum(data_file[:number_metadata])

    if number_children == 0:
        return (sum_metadata, data_file[number_metadata:])

    else:
        print("Start child")
        parse_node(data_file)
        return (sum_metadata, data_file)




metadata, last = parse_node(data_file)
print(sum_metadata)

"""
solange du nicht beim letzten Kind einer Hierachie angekommen bist:
- bearbeite Knoten
    - wenn die Anzahl Kinder > 0:
        - bearbeite Knoten
"""