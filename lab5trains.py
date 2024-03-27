"""
Dijkstra algorithm implementation:

1. Mark the source node with a current distance of 0 and the rest with infinity.
2. Set the non-visited node with the smallest current distance as the current node.
3. For each neighbor, N of the current node adds the current distance of the adjacent node with the weight of the edge connecting 0->1.
If it is smaller than the current distance of Node, set it as the new current distance of N.
4. Mark the current node 1 as visited.
5. Go to step 2 if there are any nodes are unvisited.

"""

def dijkstra_algorithm_implementation():
    # Step 1:
    non_visited_nodes = [0, 1, 2, 3]
    node_distances = [0] + [float('inf')] * (len(non_visited_nodes) - 1)

    while True:
        # Step 2:
        current_node = node_distances.index(min(node_distances))

        # Step 3:
        


        if len(non_visited_nodes) == 0:
            break

   
    print(node_distances)


dijkstra_algorithm_implementation()