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
    beam = [(heuristic[start], [start])] 
    
    while beam:
        new_beam = []
        
        for cost, path in beam:
            current_node = path[-1]
            
            if current_node == goal:
                return path, cost
            
            for neighbor in get_successors(graph, current_node):
                if neighbor not in path: 
                    new_path = path + [neighbor]
                    new_cost = cost + heuristic[neighbor]  
                    
                    new_beam.append((new_cost, new_path))
        
        beam = heapq.nsmallest(beam_width, new_beam, key=lambda x: x[0])
        
    return None, float('inf')

start = 'S'
goal = 'G'
solution, cost = beam_search(graph, heuristic, start, goal, beam_width=2)

print("Beam Search Solution Path:", solution)
print("Beam Search Path Cost:", cost)
