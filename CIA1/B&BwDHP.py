import heapq

# Define the graph
graph = {
    'S': {'A': 6, 'B': 5},  
    'A': {'B': 5, 'D': 1},  
    'B': {'C': 8, 'A': 6},
    'C': {'E': 9},
    'D': {'G': 0},  
    'E': {},  
    'G': {}   
}

# Branch and Bound with Dead Horse Principle (Extended List)
def branch_and_bound_with_extended_list(graph, start, goal):
    queue = [(0, start, [start])]  
    
    extended_list = {}
    
    best_cost = float('inf')
    best_path = None
    
    while queue:
    
        current_cost, current_node, path = heapq.heappop(queue)
        
        if current_node == goal and current_cost < best_cost:
            best_cost = current_cost
            best_path = path
        
        if current_node in extended_list and extended_list[current_node] <= current_cost:
            continue
        
        extended_list[current_node] = current_cost
        
        for neighbor, edge_cost in graph[current_node].items():
            total_cost = current_cost + edge_cost
            
            if total_cost < best_cost:
                heapq.heappush(queue, (total_cost, neighbor, path + [neighbor]))
    
    return best_path, best_cost

start_node = 'S'
goal_node = 'G'

solution_path, solution_cost = branch_and_bound_with_extended_list(graph, start_node, goal_node)

print("Best Path Found (Branch and Bound with Extended List):", solution_path)
print("Total Path Cost:", solution_cost)
