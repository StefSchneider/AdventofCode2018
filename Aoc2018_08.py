"""
Advent of Code - Day 8
Author: Stefan Schneider
Github: StefSchneider
"""

import _collections

nodes = _collections.deque
node_data: tuple = (0, 0, 0) # pos 1: number_children, pos 2: number_metadata, pos 3: position_child
pointer: int = 0
pointer_first_child: int = 0
sum_metadata: int = 0
number_children: int = 0
number_metadata: int = 0
position_first_child: int = 0
path_file: str = "AoC2018_08_input_test.txt"


data_file = list(map(int, open(path_file).read().split(" ")))
print(data_file)
node_data = (int(data_file[0]), int(data_file[1]), int(data_file[2])) # initial node
nodes.append(node_data)
#while pointer < len(data_file)-1:
while len(nodes) > 0:
    current_node = nodes.popleft()
    number_children = current_node[0]
    number_metadata = current_node[1]
    position_first_child = current_node[2]
    for i in range(1, number_children):
        node_data = (int(data_file[pointer]), int(data_file[pointer + 1]), int(data_file[pointer + 2]))

    if number_children > 0:
        pointer += 2+node_data[1]
        number_children -= 1
        for i in range(0, node_data[1]):
            sum_metadata += int(data_file[pointer+i])
    else:
        for i in range(0, node_data[1]):
            sum_metadata += int(data_file.pop())
            print(sum_metadata)

    print(node_data)
    pointer += 1

# nodes.append(node_data)
"""
Regeln:
- Der erste Knoten startet auf Pos. 1
- Die Anzahl der Kinder wird von der 1. Position eines Knotens eingelsen
- Die Zahl der Metadaten wird von der 2. Position eines Knotens eingelesen
- Ein neues Kind startet direkt ab der dritten Position eines Kindes
- Die Metadaten eines Knotens werden direkt nach der Stelle, an der die Anzahl steht, ausgelesen, aber nicht gelöscht.
    Ausnahme: Beim letzten Knoten in einer Hierarchie werden die Metadaten von hinten ausgelesen und anschließend gelöscht 
- Für jedes Kind wird ein eigener Knoten angelegt und ans Ende der Queue gehangen
- der erste Knoten der Queue ist der aktuell zu bearbeitende Knoten
- die Schleife wird solange durchlaufen, bis die Queue auf Null ist -> Folge: Es muss eine initiale Befüllung der Queue mit dem ersten Knoten geben




Lösung über Datenstruktur Queue:
A[2c, 3m] | B[0c, 3m] | C[1c, 1m] | D[0c, 1m]

first_node = True
elemente in der Queue bestehen aus tuple(Anzahl Kinder, Anzahl Metadaten, Position erstes Kind)
sum_metadata: int = 0

Verarbeitung:

number_children_current_node auf 0 setzen (Anzahl der Kinder des gerade zu bearbeitenden Knotens)
1. pointer_node auf pos = 0 setzen
2. number_children von pos pointer_node+1 auslesen
3. number_metadata von pos pointer_node+2 auslesen
4. position_first_child auf pos pointer node+3 setzen
wenn number_children > 0:   - neues Element node an Queue anhängen mit number_children, number_metadata und position_first_child   
                            - Metadaten ab pos pointer_node + 3 setzen, sonst Metadaten vom Ende auslesen
                            - pos pointer_node um number_metadata verschieben




Ablauf:
- auslesen, wie viele neue Kinder hat der aktuelle Knoten
- auslesen, wie viele Metadatem hat der aktuelle Knoten
- Metadaten zu sum_metadata addieren
- Zeiger um eine Position nach rechts verschieben, um Start des 1. Kindes zu markieren
- für jedes Kind einen neuen Knoten anlegen
- Knoten für jedes Kind mit Tuple (0, 0, Position 1. Kind) versehen  ACHTUNG 3. Stelle später überschreiben
- Knoten ans Ende der Queue hängen
-> aktuelle Knotenbearbeitung abgeschlossen - aktueller Knoten kann aus Queue gelöscht werden
ACHTUNG: Arbeitsschritt vorziehen: Daten des aktuellen Knotens mit .popleft() auslesen und dabei Knoten löschen
- Gibt es weitere Knoten auf der gleichen Hierarchieebene? Abfrage durch Zähler nodes_same_hierarchy

 
"""







