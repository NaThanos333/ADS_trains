import heapq

class Graph:
    def __init__(self):
        self.edges = {}

    def add_edge(self, origin, destination, weight):
        if origin not in self.edges:
            self.edges[origin] = []
        self.edges[origin].append((destination, weight))

    def dijkstra(self, start):
        distances = {node: float('inf') for node in self.edges}
        distances[start] = 0
        heap = [(0, start)]
        while heap:
            current_distance, current_node = heapq.heappop(heap)
            if current_distance > distances[current_node]:
                continue
            for neighbor, weight in self.edges[current_node]:
                distance = current_distance + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(heap, (distance, neighbor))
        return distances

# Create a graph
graph = Graph()

# Add edges
edges = [
    ("Amsterdam", "Den Haag", 46),
    ("Amsterdam", "Den Helder", 77),
    ("Amsterdam", "Utrecht", 26),
    ("Den Haag", "Eindhoven", 89),
    ("Eindhoven", "Maastricht", 63),
    ("Eindhoven", "Nijmegen", 55),
    ("Eindhoven", "Utrecht", 47),
    ("Enschede", "Zwolle", 50),
    ("Groningen", "Leeuwarden", 34),
    ("Groningen", "Meppel", 49),
    ("Leeuwarden", "Meppel", 40),
    ("Maastricht", "Nijmegen", 111),
    ("Meppel", "Zwolle", 15),
    ("Nijmegen", "Zwolle", 77),
    ("Utrecht", "Zwolle", 51)
]

for edge in edges:
    origin, destination, weight = edge
    graph.add_edge(origin, destination, weight)

# Test Dijkstra's algorithm
start_node = "Amsterdam"
distances = graph.dijkstra(start_node)
print("Shortest distances from", start_node + ":")
for node, distance in distances.items():
    print(node + ":", distance)
