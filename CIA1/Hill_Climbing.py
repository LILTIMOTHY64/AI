import random

# Define the graph and heuristics
graph = {
    'S': {'A': 6, 'B': 5},  
    'A': {'B': 5, 'D': 1},  
    'B': {'C': 8, 'A': 6},
    'C': {'E': 9},
    'D': {'G': 0},  
    'E': {},  
    'G': {}   
}

# Heuristic values
heuristic = {
    'S': 7,
    'A': 6,
    'B': 5,
    'C': 8,
    'D': 1,
    'E': 9,
    'G': 0
}

# Generate a random solution/path from start to goal
def random_solution(graph, start, goal):
    points = list(graph.keys())  # All nodes in the graph
    current_node = start
    solution = [current_node]
    
    # Build a random path from start to goal
    while current_node != goal:
        neighbors = list(graph[current_node].keys())
        next_node = random.choice(neighbors)  # Pick a random neighbor
        if next_node not in solution:
            solution.append(next_node)
        current_node = next_node
    
    return solution

# Calculate the path cost based on heuristics
def path_cost(heuristic, solution):
    return sum([heuristic[node] for node in solution])

# Generate neighbors of a solution by swapping nodes
def generate_neighbors(solution):
    neighbors = []
    for i in range(1, len(solution) - 1):  # Exclude the start and goal nodes from swapping
        for j in range(i + 1, len(solution) - 1):
            neighbor = solution.copy()
            neighbor[i], neighbor[j] = neighbor[j], neighbor[i]  # Swap nodes
            neighbors.append(neighbor)
    return neighbors

# Find the best neighbor based on the path cost
def best_neighbor(graph, heuristic, current_solution):
    neighbors = generate_neighbors(current_solution)
    
    best_neighbor = current_solution
    best_cost = path_cost(heuristic, current_solution)
    
    for neighbor in neighbors:
        current_cost = path_cost(heuristic, neighbor)
        if current_cost < best_cost:
            best_cost = current_cost
            best_neighbor = neighbor
    
    return best_neighbor, best_cost

# Hill Climbing Algorithm
def hill_climbing(graph, heuristic, start, goal):
    # Generate an initial random solution
    current_solution = random_solution(graph, start, goal)
    current_cost = path_cost(heuristic, current_solution)
    
    while True:
        # Find the best neighbor
        neighbor, neighbor_cost = best_neighbor(graph, heuristic, current_solution)
        
        # If no improvement, break the loop
        if neighbor_cost >= current_cost:
            print(f"Reached local optimum at {current_solution} with cost {current_cost}")
            break
        
        # Otherwise, move to the better neighbor
        current_solution = neighbor
        current_cost = neighbor_cost
    
    return current_solution, current_cost

# Test the hill climbing algorithm
start = 'S'
goal = 'G'
solution, cost = hill_climbing(graph, heuristic, start, goal)

print("Final Solution Path:", solution)
print("Final Path Cost:", cost)
