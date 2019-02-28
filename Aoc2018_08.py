"""
Advent of Code - Day 8
Author: Stefan Schneider
Github: StefSchneider
"""

"""
Regeln:
- Start 1. Knoten auf pos 1
- pos Start + 1: Anzahl Kinder
- pos Start + 2: Anzahl Matadaten von Ende




Lösung über Datenstruktur Queue:
A[2c, 3m] | B[0c, 3m] | C[1c, 1m] | D[0c, 1m]

first_node = True
elemente in der Queue bestehen aus tuple(Anzahl Kinder, Anzahl Metadaten)

Verarbeitung:

number_children_current_node auf 0 setzen (Anzahl der Kinder des gerade zu bearbeitenden Knotens)
1. pointer_node auf pos = 0 setzen
2. number_children von pos pointer_node + 1 auslesen
3. number_metadata von pos pointer_node + 2 auslesen
wenn number_children > 0:   - Metadaten ab pos pointer_node + 3 setzen, sonst Metadaten vom Ende auslesen
                            - pos pointer_node um number_metadata verschieben
 
"""




sum_input: int = 0

path_file: str = "AoC2018_08_input.txt"

data_file = open(path_file).read().split(" ")
print(data_file)

