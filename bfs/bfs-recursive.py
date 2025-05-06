"""
Breadth-First Search (BFS) Algorithm Implementation (Recursive Version)

Programmer: Guillermo Bermejo

This implementation performs a breadth-first traversal on a graph represented as an adjacency list
in a recursive manner. BFS explores all vertices of a graph reachable from a starting vertex in
order of increasing distance (think level by level).

Applications:
- Finding the shortest path in an unweighted graph
- Testing bipartiteness
- Crawling data (e.g., web pages, networks)
- AI/game trees

Structures Used: Queue, Set
Parameters: adjacency list, starting node, visited=None, queue=None

Time Complexity: O(V + E), where V is the number of vertices and E is the number of edges
Space Complexity: O(V), due to the use of a queue and visited set

Pseudo Code (Recursive Version):
    if no visited structure has been created (set is None):
        create visited                  (a set to keep track of visited nodes to avoid double processing)

    if no queue structure has been created and there is a start (start is None):
        create queue                    (bfs uses the queue for wide traversal)
        add the given starting node to the queue

    if queue is empty:
        return

    pop front node off the queue

        if this front node has NOT been visited:
            add to visited

!           PROCESS NODE

            extract neighbors list from the given adjacency list

            for every neighbor in neighbors list:
                add to queue

    RECURSE (adjacency list, neighbor, visited, queue)

Example:
            0
          /   \
         1     2
        / \   / \
       3   4 5   6
      /           \
     7             8

Output: 0, 1, 2, 3, 4, 5, 6, 7, 8
"""

from collections import deque


def bfs(adjacency_list, start, visited=None, queue=None,):
    if visited is None:
        visited = set()

    if queue is None and start is not None:
        queue = deque([start])

    if not queue:
        return

    node = queue.popleft()

    if node not in visited:
        visited.add(node)

        # START PROCESS NODE
        print(node)
        # END PROCESS NODE

        neighbors = adjacency_list[node]

        for neighbor in neighbors:
            queue.append(neighbor)

    bfs(adjacency_list, start, visited, queue)


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

    bfs(adj_list, root)

