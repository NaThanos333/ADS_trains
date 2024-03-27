"""
Dijkstra algorithm implementation:

1. Mark the source node with a current distance of 0 and the rest with infinity.
2. Set the non-visited node with the smallest current distance as the current node.
3. For each neighbor, N of the current node adds the current distance of the adjacent node with the weight of the edge connecting 0->1.
If it is smaller than the current distance of Node, set it as the new current distance of N.
4. Mark the current node 1 as visited.
5. Go to step 2 if there are any nodes are unvisited.

"""
class PriorityElement:
    def __init__(self, node, priority):
        self.node = node
        self.priority = priority

    def __lt__(self, other):
        return self.priority < other.priority

class _heap:
    def __init__(self):
        self._reverse_lookup = {}
        self._heap = [None]

    def size(self) -> int:
        return len(self._heap) - 1

    def __heap_empty_error(self) -> None:
        print("_heap empty")

    def _up_heap(self, index) -> None:
        parent_idx = len(self._heap) // 2
        if index > 1 and self._heap[index] > self._heap[parent_idx]:
            self._heap[index], self._heap[parent_idx] = self._heap[parent_idx], self._heap[index]
            self._reverse_lookup[self._heap[index].node], self._reverse_lookup[self._heap[parent_idx].node] = self._reverse_lookup[self._heap[parent_idx].node], self._reverse_lookup[self._heap[index].node]
            self._up_heap(parent_idx)

    def enqueue(self, value, priority) -> None:
        self._heap.append(PriorityElement(value, priority))
        self._reverse_lookup[value] = len(self._heap) - 1
        self._up_heap(len(self._heap) - 1)

    def _down_heap(self, index: int) -> None:
        index_max = index

        if index*2 <= self.size() and self._heap[index_max] < self._heap[index*2]:
            index_max = index*2
        if index*2+1 <= self.size() and self._heap[index_max] < self._heap[index*2+1]:
            index_max = index*2+1
        if index_max != index:
            self._heap[index], self._heap[index_max] = self._heap[index_max], self._heap[index]
            self._reverse_lookup[self._heap[index_max].node], self._reverse_lookup[self._heap[index].node] = self._reverse_lookup[self._heap[index].node], self._reverse_lookup[self._heap[index_max].node]
            self._down_heap(index_max)
        

    def remove_max(self):
        return_value = self._heap[1].nodes
        del self._reverse_lookup[return_value]
        if self.size() > 1:
            self._heap[1] = self._heap.pop()
            self._down_heap(1)
        else:
            self._heap.pop()
        return return_value.node


    def update_priority(self, value, priority):
        self._heap[self._reverse_lookup[value]].priority = priority
        self._up_heap(self._reverse_lookup[value])
        self._down_heap(self._reverse_lookup[value])


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
    todo_list = _heap()
    todo_list.enqueue(start_node, 0)
    distances = [0] + [float('inf')] * (len(graph._neighbours) - 1)
   
    while todo_list.size() > 0:
        current_node = todo_list.remove_max()
        for neighbor, weight in graph[current_node].items():
            if distances[neighbor] > distances[current_node] + weight:
                distances[neighbor] = distances[current_node] + weight
                todo_list.enqueue(neighbor, distances[neighbor])

    return distances


def test_dijkstra_algorithm_implementation():
    graph = UndirectedGraph(5)
    graph.add_edge(0, 1, 5)
    graph.add_edge(0, 2, 3)
    graph.add_edge(1, 2, 2)
    graph.add_edge(1, 3, 4)
    graph.add_edge(2, 3, 8)
    graph.add_edge(2, 4, 4)
    graph.add_edge(3, 4, 1)


    distances = dijkstra_algorithm_implementation(graph, 0)
    assert distances == [0, 5, 3, 9, 10]

    distances = dijkstra_algorithm_implementation(graph, 1)
    assert distances == [5, 0, 2, 6, 7]

    distances = dijkstra_algorithm_implementation(graph, 2)
    assert distances == [3, 2, 0, 8, 4]

    distances = dijkstra_algorithm_implementation(graph, 3)
    assert distances == [9, 6, 8, 0, 1]

    distances = dijkstra_algorithm_implementation(graph, 4)
    assert distances == [10, 7, 4, 1, 0]

    print("All tests passed")

test_dijkstra_algorithm_implementation()