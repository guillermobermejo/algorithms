"""
Depth-First Search (DFS) Algorithm Implementation (Iterative Version)

Programmer: Guillermo Bermejo

This implementation performs a depth-first traversal on a graph represented as an adjacency
list in an iterative manner. DFS explores as far as possible along each branch before
backtracking, using recursion or an explicit stack (think deepest going left to right).

Applications:
- Detecting cycles in a graph
- Topological sorting (on DAGs)
- Finding connected components
- Solving puzzles (e.g., mazes, Sudoku)
- Pathfinding in AI

Structures Used: Stack, Set
Parameters: adjacency list, starting node

Time Complexity: O(V + E), where V is the number of vertices and E is the number of edges
Space Complexity: O(V), due to the recursion stack or explicit stack

Pseudo Code (Iterative Version):
    declare a 'visited' structure (a set to keep track of visited nodes to avoid double processing)
    declare a stack structure (dfs uses the stack for deep traversal)
    add the given starting node to the stack

    while stack is not empty:
        pop top node from the stack

        if this top node has NOT been visited:
            add to visited

!           PROCESS NODE

            extract neighbors list from the given adjacency list
            reverse list (retain the DFS behaviour)

            for every neighbor in neighbors list:
                add to stack

Example:
            0
          /   \
         1     2
        / \   / \
       3   4 5   6
      /           \
     7             8

Output: 0, 1, 3, 7, 4, 2, 5, 6, 8
"""


def dfs(adjacency_list, start):
    visited = set()
    stack = [start]

    while stack:
        node = stack.pop()

        if node not in visited:
            visited.add(node)

            # START PROCESS NODE
            print(node)
            # END PROCESS NODE

            neighbors = list(adjacency_list[node])
            neighbors.reverse()

            for neighbor in neighbors:
                stack.append(neighbor)


if __name__ == '__main__':
    adj_list = {
        0: [1, 2],
        1: [3, 4],
        2: [5, 6],
        3: [7],
        4: [],
        5: [],
        6: [8],
        7: [],
        8: []
    }

    root = 0

    dfs(adj_list, root)

