import heapq

class Graph:
    def __init__(self):
        self.edges = {}

    def add_edge(self, origin, destination, weight):
        if origin not in self.edges:
            self.edges[origin] = {}
        self.edges[origin][destination] = weight
        
        # Since it's an undirected graph, add the reverse edge as well
        if destination not in self.edges:
            self.edges[destination] = {}
        self.edges[destination][origin] = weight

    def dijkstra(self, start):
        distances = {node: float('inf') for node in self.edges}
        distances[start] = 0
        heap = [(0, start)]
        while heap:
            current_distance, current_node = heapq.heappop(heap)
            if current_distance > distances[current_node]:
                continue
            for neighbor, weight in self.edges[current_node].items():
                distance = current_distance + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(heap, (distance, neighbor))
        return distances

# Create a graph
graph = Graph()

# Add edges
edges = {
    "Amsterdam": {"Den Haag": 46, "Den Helder": 77, "Utrecht": 26},
    "Den Haag": {"Amsterdam": 46, "Eindhoven": 89},
    "Den Helder": {"Amsterdam": 77},
    "Utrecht": {"Amsterdam": 26, "Eindhoven": 47, "Zwolle": 51},
    "Eindhoven": {"Den Haag": 89, "Utrecht": 47, "Maastricht": 63, "Nijmegen": 55},
    "Maastricht": {"Eindhoven": 63, "Nijmegen": 111},
    "Nijmegen": {"Eindhoven": 55, "Maastricht": 111, "Zwolle": 77},
    "Zwolle": {"Utrecht": 51, "Nijmegen": 77},
    "Enschede": {"Zwolle": 50},
    "Groningen": {"Leeuwarden": 34, "Meppel": 49},
    "Leeuwarden": {"Groningen": 34, "Meppel": 40},
    "Meppel": {"Groningen": 49, "Leeuwarden": 40, "Zwolle": 15}
}

for origin, destinations in edges.items():
    for destination, weight in destinations.items():
        graph.add_edge(origin, destination, weight)

# Test Dijkstra's algorithm
start_node = "Amsterdam"
distances = graph.dijkstra(start_node)
print("Shortest distances from", start_node + ":")
for node, distance in distances.items():
    print(node + ":", distance)
