class RomaniaMap:
    def __init__(self):
        self.graph = {
            "Arad": [("Zerind", 75), ("Timisoara", 118), ("Sibiu", 140)],
            "Zerind": [("Arad", 75), ("Oradea", 71)],
            "Oradea": [("Zerind", 71), ("Sibiu", 151)],
            "Timisoara": [("Arad", 118), ("Lugoj", 111)],
            "Lugoj": [("Timisoara", 111), ("Mehadia", 70)],
            "Mehadia": [("Lugoj", 70), ("Drobeta", 75)],
            "Drobeta": [("Mehadia", 75), ("Craiova", 120)],
            "Craiova": [("Drobeta", 120), ("Pitesti", 138), ("Rimnicu Vilcea", 146)],
            "Sibiu": [("Arad", 140), ("Oradea", 151), ("Fagaras", 99), ("Rimnicu Vilcea", 80)],
            "Rimnicu Vilcea": [("Sibiu", 80), ("Craiova", 146), ("Pitesti", 97)],
            "Fagaras": [("Sibiu", 99), ("Bucharest", 211)],
            "Pitesti": [("Rimnicu Vilcea", 97), ("Craiova", 138), ("Bucharest", 101)],
            "Bucharest": [("Fagaras", 211), ("Pitesti", 101), ("Giurgiu", 90), ("Urziceni", 85)],
            "Giurgiu": [("Bucharest", 90)],
            "Urziceni": [("Bucharest", 85), ("Vaslui", 142), ("Hirsova", 98)],
            "Hirsova": [("Urziceni", 98), ("Eforie", 86)],
            "Eforie": [("Hirsova", 86)],
            "Vaslui": [("Urziceni", 142), ("Iasi", 92)],
            "Iasi": [("Vaslui", 92), ("Neamt", 87)],
            "Neamt": [("Iasi", 87)]
        }
        self.heuristic = {
            "Arad": 366, "Bucharest": 0, "Craiova": 160, "Drobeta": 242,
            "Eforie": 161, "Fagaras": 176, "Giurgiu": 77, "Hirsova": 151,
            "Iasi": 226, "Lugoj": 244, "Mehadia": 241, "Neamt": 234,
            "Oradea": 380, "Pitesti": 100, "Rimnicu Vilcea": 193,
            "Sibiu": 253, "Timisoara": 329, "Urziceni": 80, "Vaslui": 199,
            "Zerind": 374
        }

    def get_neighbors(self, city):
        return self.graph.get(city, [])

    def get_heuristic(self, city):
        return self.heuristic.get(city, float("inf"))


class IDAStar:
    def __init__(self, romania_map, max_nodes=7):
        self.romania_map = romania_map
        self.max_nodes = max_nodes  # Limit nodes in memory

    def search(self, node, goal, g, threshold, path, visited):
        f = g + self.romania_map.get_heuristic(node)
        if f > threshold:
            return f  # Return new threshold suggestion

        if node == goal:
            return "FOUND"  # Goal reached

        min_threshold = float("inf")

        neighbors = sorted(self.romania_map.get_neighbors(node), key=lambda x: self.romania_map.get_heuristic(x[0]))

        for neighbor, cost in neighbors:
            if neighbor in visited:
                continue  # Avoid revisiting nodes

            if len(path) >= self.max_nodes:
                return float("inf")  # Prune if node limit exceeded

            visited.add(neighbor)
            path.append(neighbor)

            result = self.search(neighbor, goal, g + cost, threshold, path, visited)

            if result == "FOUND":
                return "FOUND"

            if isinstance(result, (int, float)):
                min_threshold = min(min_threshold, result)

            path.pop()
            visited.remove(neighbor)

        return min_threshold

    def ida_star(self, start, goal):
        threshold = self.romania_map.get_heuristic(start)
        path = [start]

        while True:
            visited = set(path)
            result = self.search(start, goal, 0, threshold, path, visited)

            if result == "FOUND":
                return path

            if result == float("inf"):
                return None  # No solution found

            threshold = result  # Increase threshold


# Usage
romania_map = RomaniaMap()
ida_star_solver = IDAStar(romania_map, max_nodes=7)
path = ida_star_solver.ida_star("Iasi", "Bucharest")

print("Path found:", path if path else "No path found")
