"""
This code implements the Floyd Warshall algorithm recursively.
Created on 28th February 2024.
"""

NO_PATH = 2048
MAX_LENGTH = 4


def floyd_recursive(distance, start_node, end_node, intermediate)->int:
    """
    A recursive implementation of Floyd's algorithm.
    """
    # Base case: If start_node and end_node are the same, distance is 0.
    if start_node == end_node:
        return 0
    # If either start_node or end_node has no path through intermediate node, return infinity.
    if intermediate == -1:
        return distance[start_node][end_node]
    # Compute the distance via intermediate node recursively.
    return min(
        floyd_recursive(distance, start_node, end_node, intermediate - 1),
        distance[start_node][intermediate] + distance[intermediate][end_node]
    )


def floyd2(graph):
    """
    A wrapper function to apply Floyd's algorithm recursively.
    """
    for intermediate in range(MAX_LENGTH):
        for start_node in range(MAX_LENGTH):
            for end_node in range(MAX_LENGTH):
                graph[start_node][end_node] = min(
                    graph[start_node][end_node],
                    floyd_recursive(graph, start_node, end_node, intermediate)
                )
    return graph


if __name__ == '__main__':
    graph = [[0, 7, NO_PATH, 8], [NO_PATH, 0, 5, NO_PATH], [NO_PATH, NO_PATH, 0, 2], [NO_PATH, NO_PATH, NO_PATH, 0]]
    print(floyd2(graph))
