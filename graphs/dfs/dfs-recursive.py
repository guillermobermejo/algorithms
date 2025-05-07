"""
Depth-First Search (DFS) Algorithm Implementation (Recursive Version)

Programmer: Guillermo Bermejo

This implementation performs a depth-first traversal on a graph represented as an adjacency
list in a recursive manner (implicit stack). DFS explores as far as possible along each branch before
backtracking, using recursion or an explicit stack (think deepest going left to right).

Applications:
- Detecting cycles in a graph
- Topological sorting (on DAGs)
- Finding connected components
- Solving puzzles (e.g., mazes, Sudoku)
- Pathfinding in AI

Structures Used: Stack, Set
Parameters: adjacency list, starting node, visited=None

Time Complexity: O(V + E), where V is the number of vertices and E is the number of edges
Space Complexity: O(V), due to the recursion stack or explicit stack

Pseudo Code (Recursive Version):
    if no visited structure has been created (set is None):
        create visited                  (a set to keep track of visited nodes to avoid double processing)

    if node not in visited:
        add to visited                  (dfs uses the stack for deep traversal)

!       PROCESS NODE

        extract neighbors list from adjacency list

        for every neighbor in neighbors list:
            RECURSE (adjacency list, neighbor, visited)

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


def dfs(adjacency_list, start, visited=None):
    if visited is None:
        visited = set()

    if start not in visited:
        visited.add(start)

        # START PROCESS NODE
        print(start)
        # END PROCESS NODE

        neighbors = adjacency_list[start]

        for neighbor in neighbors:
            dfs(adjacency_list, neighbor, visited)


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

