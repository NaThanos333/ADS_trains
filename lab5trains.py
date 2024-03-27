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
    
class WeightedNode:
    def __init__(self, node, weight):
        self._node = node
        self._weight = weight

    def __lt__(self, other):
        return self._weight > other._weight
        

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
    graph = UndirectedGraph(6)
    graph.add_edge(0, 1, 7)
    graph.add_edge(0, 2, 9)
    graph.add_edge(0, 5, 14)
    graph.add_edge(1, 2, 10)
    graph.add_edge(1, 3, 15)
    graph.add_edge(2, 3, 11)
    graph.add_edge(2, 5, 2)
    graph.add_edge(3, 4, 6)
    graph.add_edge(4, 5, 9)
    assert dijkstra_algorithm_implementation(graph, 0) == [0, 7, 9, 20, 26, 11]
    assert dijkstra_algorithm_implementation(graph, 1) == [7, 0, 10, 15, 21, 12]
    assert dijkstra_algorithm_implementation(graph, 2) == [9, 10, 0, 11, 17, 2]
    assert dijkstra_algorithm_implementation(graph, 3) == [20, 15, 11, 0, 6, 13]
    assert dijkstra_algorithm_implementation(graph, 4) == [26, 21, 17, 6, 0, 9]
    assert dijkstra_algorithm_implementation(graph, 5) == [11, 12, 2, 13, 9, 0]

test_dijkstra_algorithm_implementation()
