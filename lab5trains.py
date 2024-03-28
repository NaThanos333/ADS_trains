import heapq
"""
Dijkstra algorithm implementation:
poep
1. Mark the source node with a current distance of 0 and the rest with infinity.
2. Set the non-visited node with the smallest current distance as the current node.
3. For each neighbor, N of the current node adds the current distance of the adjacent node with the weight of the edge connecting 0->1.
If it is smaller than the current distance of Node, set it as the new current distance of N.
4. Mark the current node 1 as visited.
5. Go to step 2 if there are any nodes are unvisited.

"""

class GraphEdge:
    def __init__(self, origin, destination, weight):
        self._incident_nodes = (origin, destination)
        self._origin = origin
        self._destination = destination
        self._weight = weight

    def is_incident(self, node):
        return node == self._origin or node == self._destination
    
    def other_node(self, node):
        if self.is_incident(node):
            return self._origin + self._destination - node
        
        return -1
    
    def get_weight(self):
        return self._weight
        

class UndirectedGraph:
    def __init__(self, node_count):
        self._neighbours = [[] for _ in range(node_count)]

    def add_edge(self, node1, node2, weight):
        new_edge = GraphEdge(node1, node2, weight)
        self._neighbours[node1].append(new_edge)
        self._neighbours[node2].append(new_edge)


def dijkstra_algorithm_implementation(graph, start_node):
    todo_list = []
    heapq.heappush(todo_list, (0, start_node))
    distances = [0] + [float('inf')] * (len(graph._neighbours) - 1)
   
    while todo_list:
        current_distance, current_node = heapq.heappop(todo_list)
        if current_distance > distances[current_node]:
            continue
        for edge in graph._neighbours[current_node]:
            neighbor = edge.other_node(current_node)
            weight = edge.get_weight()
            if distances[neighbor] > distances[current_node] + weight:
                distances[neighbor] = distances[current_node] + weight
                heapq.heappush(todo_list, (distances[neighbor], neighbor))

    return distances


def test_dijkstra_algorithm_implementation():

    # Create a graph
    graph = UndirectedGraph(12)

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


test_dijkstra_algorithm_implementation()
