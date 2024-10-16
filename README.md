
# CIA1
## AI Search Algorithms implemented in Python
### 1. AOStar.py
- Implementation of the AO* algorithm, which is used for searching through an AND-OR graph, useful in problem-solving scenarios involving contingent decisions.
- Key Features:
    - Solves complex decision-making problems.
    - Explores both AND and OR nodes.
### 2. AStar.py
- Implements the A* algorithm, a popular pathfinding and graph traversal algorithm known for its efficiency and accuracy in finding the shortest path.
- Key Features:
    - Uses both cost and heuristic (f(n) = g(n) + h(n)).
    - Guarantees the shortest path if the heuristic is admissible.
### 3. B&BCwCH.py (Branch and Bound with Cost and Heuristic)
- An implementation of the Branch and Bound algorithm that uses cost and heuristic values to prune the search space.
- Key Features:
    - Combines cost and heuristic for efficient pruning.
### 4. B&BwDHP.py (Branch and Bound with Dead Horse Principle)
- An extended Branch and Bound method that incorporates the Dead Horse Principle, where unpromising paths are pruned early.
- Key Features:
    - Early pruning of non-viable paths.
### 5. Beam.py
- Implements the Beam Search algorithm, a heuristic search technique that explores a set number of the most promising nodes at each level.
- Key Features:
    - Uses a beam width to limit the search space.
    - Efficient memory usage compared to exhaustive search methods.
### 6. BestFS.py
- Implements the Best-First Search algorithm, which greedily selects the most promising node based on a given heuristic.
- Key Features:
    - Uses a priority queue to explore the best node first.
### 7. BFS.py (Breadth First Search)
- Implements the Breadth-First Search algorithm, a fundamental graph traversal technique that explores all nodes at the present depth before moving on to nodes at the next depth level.
- Key Features:
    - Guarantees finding the shortest path in an unweighted graph.
    - Explores neighbors level by level.
    - Suitable for tree and graph traversal problems.
## 8. BMS.py (Beam Search)
- Implements a variant of Beam Search with specific beam width, focusing on heuristic-driven exploration.
- Key Features:
    - Efficient search within the constraints of a limited beam width.
### 9. Branch&Bound.py
- Standard implementation of the Branch and Bound algorithm, which systematically explores all possible solutions and prunes suboptimal paths.
- Key Features:
    - Guarantees finding the optimal solution.
    - Prunes non-promising paths to save time.
### 10. DFS.py (Depth-First Search)
- A basic implementation of Depth-First Search, a fundamental graph traversal algorithm.
- Key Features:
    - Explores as deep as possible along each branch before backtracking.
### 11. Hill_Climbing.py
- Implementation of the Hill Climbing algorithm, a local search technique that iteratively improves the solution by selecting the neighbor with the highest value.
- Key Features:
    - Can get stuck in local optima.
    - Suitable for optimization problems.
### 12. Oracle.py
- A simple oracle-finding algorithm that attempts to find the best solution in a decision problem.
- Key Features:
    - Explores the search space to find an optimal oracle.
# CIA2
## Gaming Adversarial Algorithms implemented in Python
### 1. a-bPrune.py (Alpha-Beta Pruning)
- Implementation of the Alpha-Beta Pruning algorithm, an optimization technique for the Minimax algorithm that reduces the number of nodes evaluated.
- Key Features:
    - Prunes branches in the game tree that don’t influence the final decision.
    - More efficient than standard Minimax.
