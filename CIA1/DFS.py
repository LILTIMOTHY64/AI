def dfs(graph, start, goal, visited=None, path=None):
    if visited is None:
        visited = set()  # Initialize the visited set
    if path is None:
        path = []  # Initialize path list to track the current path
    
    visited.add(start)  # Mark the current node as visited
    path.append(start)  # Add current node to the path
    print(f"Visiting: {start}")

    if start == goal:
        print(f"Goal {goal} found!")
        print("Path:", " -> ".join(path))
        return True  # Stop the search when goal is found

    # Explore the neighbors of the current node
    for neighbor in graph[start]:
        if neighbor not in visited:
            if dfs(graph, neighbor, goal, visited, path):  # Recursively visit neighbors
                return True  # Return True if goal is found in the neighbor's path

    path.pop()  # Backtrack: remove the current node from the path
    return False  # Return False if the goal was not found


# Graph structure with S as the source and G as the goal
graph = {
    'S': ['A', 'B'],
    'A': ['B', 'D'],
    'B': ['C', 'A'],
    'C': ['E'],
    'D': ['G'],
    'E': [],   # E is a dead end
    'G': []    # G is the goal
}

# Test DFS with 'S' as the source and 'G' as the goal
dfs(graph, 'S', 'G')