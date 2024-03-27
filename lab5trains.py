"""
Dijkstra algorithm implementation:

1. Mark the source node with a current distance of 0 and the rest with infinity.
2. Set the non-visited node with the smallest current distance as the current node.
3. For each neighbor, N of the current node adds the current distance of the adjacent node with the weight of the edge connecting 0->1.
If it is smaller than the current distance of Node, set it as the new current distance of N.
4. Mark the current node 1 as visited.
5. Go to step 2 if there are any nodes are unvisited.

"""
from heap import Heap

def dijkstra_algorithm_implementation(graph, start_node):
    todo_list = set(graph.keys())
    distances = [0] + [float('inf')] * (len(todo_list) - 1)	
   
    while todo_list:
        current_node = min(todo_list, key=lambda node: distances[node])
        todo_list.remove(current_node)
        for neighbor, weight in graph[current_node].items():
            if distances[neighbor] > distances[current_node] + weight:
                distances[neighbor] = distances[current_node] + weight

    return distances

dijkstra_algorithm_implementation()

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

        