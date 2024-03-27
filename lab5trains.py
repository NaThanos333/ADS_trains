"""
Dijkstra algorithm implementation:

1. Mark the source node with a current distance of 0 and the rest with infinity.
2. Set the non-visited node with the smallest current distance as the current node.
3. For each neighbor, N of the current node adds the current distance of the adjacent node with the weight of the edge connecting 0->1.
If it is smaller than the current distance of Node, set it as the new current distance of N.
4. Mark the current node 1 as visited.
5. Go to step 2 if there are any nodes are unvisited.

"""

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