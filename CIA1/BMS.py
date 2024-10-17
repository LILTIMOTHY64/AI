# Define the graph (unweighted, no heuristics)
graph = {
    'S': ['A', 'B'],
    'A': ['B', 'D'],
    'B': ['C', 'A'],
    'C': ['E'],
    'D': ['G'],
    'E': [],
    'G': []
}

# Function to find all paths from start to goal
def bms(graph, start, goal, path=[]):
    path = path + [start]  # Add current node to the path
    
    # If the start node is the goal, return the current path
    if start == goal:
        return [path]
    
    # If the start node has no outgoing edges, return an empty list (no path)
    if start not in graph:
        return []
    
    # List to store all the paths from start to goal
    paths = []
    
    # Explore all the neighbors of the current node
    for neighbor in graph[start]:
        if neighbor not in path:  # Avoid cycles by skipping nodes already in the path
            new_paths = bms(graph, neighbor, goal, path)
            for new_path in new_paths:
                paths.append(new_path)
    
    return paths

# Run the function to find all paths from 'S' to 'G'
start_node = 'S'
goal_node = 'G'
all_paths = bms(graph, start_node, goal_node)

# Output the results
print("All Possible Paths from", start_node, "to", goal_node, ":")
for path in all_paths:
    print(path)
