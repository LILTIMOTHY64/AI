from collections import deque

def bfs(graph, start, goal):
    visited = set()  # Set to keep track of visited nodes
    queue = deque([(start, [start])])  # Queue now stores tuples of (current node, path)
    
    while queue:
        current_node, path = queue.popleft()  # Get the node and the path taken to reach it
        print(f"Visiting: {current_node}")

        if current_node == goal:
            print(f"Goal {goal} found!")
            print("Path:", " -> ".join(path))
            return True  # Goal found

        if current_node not in visited:
            visited.add(current_node)  # Mark the current node as visited

            # Add all unvisited neighbors to the queue along with the updated path
            for neighbor in graph[current_node]:
                if neighbor not in visited:
                    queue.append((neighbor, path + [neighbor]))  # Add neighbor and the updated path
    
    print("Goal not found")
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

# Test BFS with 'S' as the source and 'G' as the goal
bfs(graph, 'S', 'G')