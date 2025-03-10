import json
import math
cities = {
    "București": (560, 550),         # Schimbare: Bucharest -> București
    "Slobozia": (676, 534),
    "Cluj-Napoca": (325, 245),
    "Piatra Neamț": (576, 219),      # Schimbare: Piatra Neamt -> Piatra Neamț
    "Timișoara": (92, 380),
    "Iași": (698, 199),
    "Constanța": (810, 618),
    "Miercurea Ciuc": (530, 297),
    "Brașov": (510, 402),            # Schimbare: Brasov -> Brașov
    "Sibiu": (383, 390),
    "Oradea": (165, 205),
    "Craiova": (326, 577),
    "Galați": (743, 423),
    "Arad": (100, 320),
    "Pitești": (440, 508),
    "Bacău": (635, 276),
    "Vaslui": (709, 278),
    "Suceava": (564, 135),
    "Târgu Mureș": (425, 270),
    "Ploiești": (547, 493),
    "Călărași": (673, 593),          # Schimbare: Calarasi -> Călărași
    "Giurgiu": (543, 640),
    "Brăila": (727, 447),
    "Buzău": (623, 470),
    "Baia Mare": (330, 135),
    "Satu Mare": (257, 113),
    "Alba Iulia": (325, 340),
    "Bistrița": (403, 193),          # Schimbare: Bistrita -> Bistrița
    "Drobeta-Turnu Severin": (226, 528),
    "Târgu Jiu": (290, 480),
    "Reșița": (165, 442),
    "Slatina": (400, 570),
    "Râmnicu Vâlcea": (390, 479),
    "Târgoviște": (493, 501),        # Schimbare: Targoviste -> Târgoviște
    "Focșani": (645, 393),
    "Botoșani": (611, 118),
    "Deva": (255, 355),
    "Sfântu Gheorghe": (533, 370),
    "Zalău": (270, 190),             # Schimbare: Zalau -> Zalău
    "Tulcea": (820, 460),
    "Alexandria": (483, 620),
}


# Distantele dintre orase vecine (datele tale)
graph = {
    "Satu Mare": [("Oradea", 147), ("Zalău", 96.5), ("Baia Mare", 62.2)],
    "Oradea": [("Satu Mare", 147), ("Zalău", 125), ("Arad", 115), ("Cluj-Napoca", 159), ("Alba Iulia", 247)],
    "Zalău": [("Satu Mare", 96.5), ("Oradea", 125), ("Bistrița", 143), ("Baia Mare", 87.7), ("Cluj-Napoca", 86.4)],
    "Baia Mare": [("Satu Mare", 62.2), ("Zalău", 87.7), ("Bistrița", 142)],
    "Bistrița": [("Zalău", 143), ("Baia Mare", 142), ("Suceava", 196), ("Târgu Mureș", 91.3)],
    "Târgu Mureș": [("Bistrița", 91.3), ("Miercurea Ciuc", 142), ("Alba Iulia", 130)],
    "Miercurea Ciuc": [("Târgu Mureș", 142), ("Piatra Neamț", 162), ("Bacău", 138), ("Sfântu Gheorghe", 69.2)],
    "Piatra Neamț": [("Miercurea Ciuc", 162), ("Suceava", 103), ("Bacău", 61.3), ("Iași", 130)],
    "Suceava": [("Bistrița", 196), ("Piatra Neamț", 103), ("Botoșani", 39.7)],
    "Botoșani": [("Suceava", 39.7), ("Iași", 108)],
    "Iași": [("Botoșani", 108), ("Piatra Neamț", 130), ("Vaslui", 66.3), ("Bacău", 128)],
    "Vaslui": [("Iași", 66.3)],
    "Bacău": [("Miercurea Ciuc", 138), ("Piatra Neamț", 61.3), ("Iași", 128), ("Focșani", 109)],
    "Alba Iulia": [("Oradea", 247), ("Târgu Mureș", 130), ("Deva", 71.5), ("Sibiu", 82.2)],
    "Cluj-Napoca": [("Oradea", 159), ("Zalău", 86.4)],
    "Arad": [("Oradea", 115), ("Timișoara", 56.6), ("Deva", 187)],
    "Timișoara": [("Arad", 56.6), ("Reșița", 97.4), ("Deva", 151)],
    "Reșița": [("Timișoara", 97.4), ("Deva", 160), ("Târgu Jiu", 222), ("Drobeta-Turnu Severin", 159)],
    "Deva": [("Arad", 187), ("Timișoara", 151), ("Reșița", 160), ("Târgu Jiu", 146), ("Sibiu", 122)],
    "Târgu Jiu": [("Deva", 146), ("Reșița", 222), ("Drobeta-Turnu Severin", 83), ("Craiova", 111), ("Râmnicu Vâlcea", 115)],
    "Drobeta-Turnu Severin": [("Reșița", 159), ("Târgu Jiu", 83), ("Craiova", 111)],
    "Craiova": [("Drobeta-Turnu Severin", 111), ("Târgu Jiu", 111), ("Slatina", 50)],
    "Slatina": [("Craiova", 50), ("Pitești", 55), ("Alexandria", 108)],
    "Râmnicu Vâlcea": [("Târgu Jiu", 115), ("Sibiu", 104), ("Pitești", 64.9)],
    "Sibiu": [("Alba Iulia", 82.2), ("Deva", 122), ("Râmnicu Vâlcea", 104), ("Brașov", 147)],
    "Pitești": [("Râmnicu Vâlcea", 64.9), ("Slatina", 55), ("Alexandria", 121), ("Târgoviște", 80.9)],
    "Alexandria": [("Slatina", 108), ("Pitești", 121), ("Giurgiu", 58)],
    "Giurgiu": [("Alexandria", 58), ("București", 62.7), ("Călărași", 173)],
    "București": [("Giurgiu", 62.7), ("Călărași", 113), ("Slobozia", 48.3), ("Ploiești", 78.9), ("Buzău", 119), ("Târgoviște", 81.4)],
    "Călărași": [("București", 113), ("Giurgiu", 173), ("Slobozia", 48.3), ("Constanța", 151)],
    "Slobozia": [("București", 48.3), ("Călărași", 48.3), ("Buzău", 89.3), ("Tulcea", 159), ("Constanța", 144)],
    "Constanța": [("Călărași", 151), ("Slobozia", 144), ("Tulcea", 132)],
    "Tulcea": [("Slobozia", 159), ("Constanța", 132), ("Brăila", 43)],
    "Ploiești": [("București", 78.9), ("Târgoviște", 48.4), ("Brașov", 111), ("Buzău", 71.6)],
    "Târgoviște": [("Pitești", 80.9), ("București", 81.4), ("Ploiești", 48.4)],
    "Buzău": [("București", 119), ("Ploiești", 71.6), ("Slobozia", 89.3), ("Brăila", 103)],
    "Brașov": [("Sibiu", 147), ("Ploiești", 111), ("Sfântu Gheorghe", 32.9)],
    "Sfântu Gheorghe": [("Brașov", 32.9), ("Miercurea Ciuc", 69.2), ("Focșani", 158)],
    "Focșani": [("Sfântu Gheorghe", 158), ("Bacău", 109), ("Galați", 85.6), ("Brăila", 91.4)],
    "Brăila": [("Focșani", 91.4), ("Buzău", 103), ("Galați", 21.4), ("Tulcea", 43)],
    "Galați": [("Focșani", 85.6), ("Brăila", 21.4)],
}

# Computes the euclidian distance between 2 points
def heuristic(node, goal):
    if node not in cities or goal not in cities:
        return 0
    x1, y1 = cities[node]
    x2, y2 = cities[goal]
    return math.hypot(x2 - x1, y2 - y1) / 5  # dividing by 5 for more realistic distances



def idADistance(city1, city2):
    path, cost = ida_star(city1, city2)

    if path:
        print(f"Drumul optim: {' -> '.join(path)}")
        print(f"Distanța totală: {cost:.2f} km")
    else:
        print("Nu s-a găsit niciun drum între orașele selectate.")


def ida_star(start, goal):
    threshold = heuristic(start, goal)
    path = [start]

    while True:
        print(f"Start search cu threshold: {threshold}")
        temp = search(path, 0, threshold, goal)

        if temp == "FOUND":
            return path.copy(), sum_cost(path)

        if temp == float('inf'):
            return None, float('inf')

        threshold = temp


def search(path, g, threshold, goal):
    node = path[-1]
    f = g + heuristic(node, goal)

    if f > threshold:
        return f

    if node == goal:
        return "FOUND"

    if len(path) > 7:
        return float('inf')

    min_threshold = float('inf')

    for neighbor, cost in graph.get(node, []):
        if neighbor in path:
            continue  # Evită ciclurile

        path.append(neighbor)

        temp = search(path, g + cost, threshold, goal)

        if temp == "FOUND":
            return "FOUND"

        if temp < min_threshold:
            min_threshold = temp

        path.pop()  # Backtrack

    return min_threshold



def sum_cost(path):
    total = 0
    for i in range(len(path) - 1):
        node = path[i]
        next_node = path[i + 1]

        for neighbor, cost in graph.get(node, []):
            if neighbor == next_node:
                total += cost
                break
    return total
