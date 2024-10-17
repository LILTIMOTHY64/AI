import math

def alpha_beta_pruning(depth, nodeIndex, isMaximizingPlayer, values, alpha, beta, maxDepth):
    # Terminal node (leaf nodes)
    if depth == maxDepth:
        print(f"Leaf node reached at depth {depth}, returning value: {values[nodeIndex]}")
        return values[nodeIndex]

    if isMaximizingPlayer:
        best = -math.inf

        print(f"Maximizer at depth {depth}, alpha: {alpha}, beta: {beta}")
        # Maximizer's choice (MAX player)
        for i in range(2):
            value = alpha_beta_pruning(depth + 1, nodeIndex * 2 + i, False, values, alpha, beta, maxDepth)
            print(f"Maximizer at depth {depth}, comparing value: {value} with best: {best}")
            best = max(best, value)
            alpha = max(alpha, best)
            print(f"Maximizer updated alpha: {alpha}")

            # Alpha-Beta Pruning
            if beta <= alpha:
                print(f"Pruning at maximizer node at depth {depth}, alpha: {alpha}, beta: {beta}")
                break
        print(f"Maximizer at depth {depth}, selected best: {best}")
        return best
    else:
        best = math.inf

        print(f"Minimizer at depth {depth}, alpha: {alpha}, beta: {beta}")
        # Minimizer's choice (MIN player)
        for i in range(2):
            value = alpha_beta_pruning(depth + 1, nodeIndex * 2 + i, True, values, alpha, beta, maxDepth)
            print(f"Minimizer at depth {depth}, comparing value: {value} with best: {best}")
            best = min(best, value)
            beta = min(beta, best)
            print(f"Minimizer updated beta: {beta}")

            # Alpha-Beta Pruning
            if beta <= alpha:
                print(f"Pruning at minimizer node at depth {depth}, alpha: {alpha}, beta: {beta}")
                break
        print(f"Minimizer at depth {depth}, selected best: {best}")
        return best

# The depth of the game tree
maxDepth = 3

# Values of the leaf nodes
values = [-1, 4, 2, 6, -3, -5, 0, 7]

# Initial values of alpha and beta
alpha = -math.inf
beta = math.inf

# Call the alpha-beta pruning algorithm
optimalValue = alpha_beta_pruning(0, 0, True, values, alpha, beta, maxDepth)

print("\nThe optimal value is:", optimalValue)
