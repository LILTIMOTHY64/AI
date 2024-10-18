import heapq

# Define the graph
graph = {
    'S': {'A': 6, 'B': 5},  
    'A': {'B': 5, 'D': 1},  
    'B': {'C': 8, 'A': 6},
    'C': {'E': 9},
    'D': {'G': 2},  
    'E': {},  
    'G': {}   
}

# Define the heuristic values
heuristic = {
    'S': 7,
    'A': 6,
    'B': 5,
    'C': 8,
    'D': 1,
    'E': 9,
    'G': 0
}

# Branch and Bound with Cost and Heuristics
def branch_and_bound_with_heuristic(graph, heuristic, start, goal):
    queue = [(0 + heuristic[start], 0, start, [start])]
    
    extended_list = {}
    
    best_cost = float('inf')
    best_path = None
    
    while queue:
        f_cost, current_cost, current_node, path = heapq.heappop(queue)
        
        if current_node == goal and current_cost < best_cost:
            best_cost = current_cost
            best_path = path
            continue
        
        if current_node in extended_list and extended_list[current_node] <= current_cost:
            continue 
        
        extended_list[current_node] = current_cost
        
        for neighbor, edge_cost in graph[current_node].items():
            total_cost = current_cost + edge_cost
            f_neighbor_cost = total_cost + heuristic[neighbor]
            
            if total_cost < best_cost:
                heapq.heappush(queue, (f_neighbor_cost, total_cost, neighbor, path + [neighbor]))
    
    return best_path, best_cost

start_node = 'S'
goal_node = 'G'

solution_path, solution_cost = branch_and_bound_with_heuristic(graph, heuristic, start_node, goal_node)

print("Best Path Found (Branch and Bound with Cost + Heuristics):", solution_path)
print("Total Path Cost:", solution_cost)
