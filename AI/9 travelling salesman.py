from itertools import permutations

# Define the function to calculate the total cost of a given path
def calculate_path_cost(graph, path):
    cost = 0
    for i in range(len(path) - 1):
        cost += graph[path[i]][path[i + 1]]  # Add the cost between two cities
    cost += graph[path[-1]][path[0]]  # Add the cost to return to the starting city
    return cost

# Function to solve the TSP
def tsp(graph):
    # Get all the nodes (cities) in the graph
    cities = list(graph.keys())
    min_cost = float('inf')  # Initialize with a very large value
    best_path = None
    
    # Generate all permutations of cities except the starting city
    for perm in permutations(cities[1:]):  
        path = [cities[0]] + list(perm)  # Start with city A
        cost = calculate_path_cost(graph, path)
        
        # Update the minimum cost and best path if a lower-cost path is found
        if cost < min_cost:
            min_cost = cost
            best_path = path

    # Add the return to A for the best path for explicit clarity
    best_path.append(cities[0])
    return best_path, min_cost

# Example graph represented as an adjacency matrix (dictionary of dictionaries)
graph = {
    'A': {'A': 0, 'B': 10, 'C': 15, 'D': 20},
    'B': {'A': 10, 'B': 0, 'C': 35, 'D': 25},
    'C': {'A': 15, 'B': 35, 'C': 0, 'D': 30},
    'D': {'A': 20, 'B': 25, 'C': 30, 'D': 0}
}

# Solve the TSP problem
best_path, min_cost = tsp(graph)

# Print the result
print("Optimal Path:", " -> ".join(best_path))
print("Minimum Cost:", min_cost)
