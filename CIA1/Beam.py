import heapq

# Define the graph and heuristics
graph = {
    'S': {'A': 6, 'B': 5},  
    'A': {'B': 5, 'D': 1},  
    'B': {'C': 8, 'A': 6},
    'C': {'E': 9},
    'D': {'G': 2},  
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

# Function to get successors of the current node
def get_successors(graph, node):
    return graph[node].keys()

# Beam Search Algorithm
def beam_search(graph, heuristic, start, goal, beam_width=2):
    # Priority queue for the current beam
    beam = [(heuristic[start], [start])]  # (heuristic value, path)
    
    while beam:
        # Expand the beam, limited by the beam width
        new_beam = []
        
        # Iterate over the current beam paths
        for cost, path in beam:
            current_node = path[-1]
            
            # If we reached the goal, return the solution
            if current_node == goal:
                return path, cost
            
            # Expand the successors of the current node
            for neighbor in get_successors(graph, current_node):
                if neighbor not in path:  # Avoid cycles
                    new_path = path + [neighbor]
                    new_cost = cost + heuristic[neighbor]  # Update cost based on heuristic
                    
                    # Add the new path to the beam
                    new_beam.append((new_cost, new_path))
        
        # Keep only the best `beam_width` paths (based on cost)
        beam = heapq.nsmallest(beam_width, new_beam, key=lambda x: x[0])
        
    # If no solution is found, return failure
    return None, float('inf')

# Test the beam search algorithm
start = 'S'
goal = 'G'
solution, cost = beam_search(graph, heuristic, start, goal, beam_width=2)

print("Beam Search Solution Path:", solution)
print("Beam Search Path Cost:", cost)
