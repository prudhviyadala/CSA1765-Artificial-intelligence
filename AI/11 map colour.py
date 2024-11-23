def is_safe(node, color, graph, colors):
    """
    Check if it's safe to assign the color to the given node.
    """
    for neighbor in graph[node]:
        if colors[neighbor] == color:
            return False
    return True

def map_coloring_util(graph, color_options, colors, node):
    """
    Utility function to solve the map coloring problem using backtracking.
    """
    # If all nodes are assigned a color, return True
    if node == len(graph):
        return True

    # Try all colors for the current node
    for color in color_options:
        if is_safe(node, color, graph, colors):
            # Assign the color to the node
            colors[node] = color
            
            # Recur to assign colors to the rest of the nodes
            if map_coloring_util(graph, color_options, colors, node + 1):
                return True
            
            # Backtrack if assigning this color doesn't lead to a solution
            colors[node] = None

    return False

def map_coloring(graph, color_options):
    """
    Solve the map coloring problem.
    """
    # Initialize colors for all nodes to None (uncolored)
    colors = [None] * len(graph)

    if map_coloring_util(graph, color_options, colors, 0):
        return colors
    else:
        return None

# Example Usage
if __name__ == "__main__":
    # Define the graph as an adjacency list
    # Example graph: A map with 4 regions (nodes 0, 1, 2, 3)
    graph = {
        0: [1, 2],    # Region 0 is adjacent to regions 1 and 2
        1: [0, 2, 3], # Region 1 is adjacent to regions 0, 2, and 3
        2: [0, 1, 3], # Region 2 is adjacent to regions 0, 1, and 3
        3: [1, 2]     # Region 3 is adjacent to regions 1 and 2
    }

    # Color options as R, G, B
    color_options = ["R", "G", "B"]

    # Solve the problem
    result = map_coloring(graph, color_options)
    if result:
        print("Solution found:")
        for region, color in enumerate(result):
            print(f"Region {region}: {color}")
    else:
        print("No solution exists!")
