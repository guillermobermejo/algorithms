'''
Network Delay Time Question (Bellman Ford O(V*E) + O(E) == O(VE))

You are given a network of n nodes labeled from 1 to n.
You are also given a list of travel times:

(u, v, w)

where:
u = source node
v = destination node
w = time/cost/weight to travel from u to v

Starting from node k, determine:
The minimum time required for a signal to reach all nodes in the network.
If some node cannot be reached, return -1.
Otherwise, return the time it takes for the furthest node to receive the signal.
'''

'''
Bellman-Ford Psuedocode

BELLMAN_FORD(edges, start, V):

    create array dist[1..V]
    create array prev[1..V]

    for i = 1 to V:
        dist[i] = ∞
        prev[i] = NIL

    dist[start] = 0


    # Relax edges up to V-1 times
    for i = 1 to V-1:

        updated = false

        for each edge (u, v, w) in edges:

            if dist[u] ≠ ∞:

                if dist[u] + w < dist[v]:

                    dist[v] = dist[u] + w
                    prev[v] = u
                    updated = true

        if updated == false:
            break


    # Negative cycle detection
    for each edge (u, v, w) in edges:

        if dist[u] ≠ ∞:

            if dist[u] + w < dist[v]:

                report "negative cycle detected"


    return dist, prev
'''

from queue import PriorityQueue
import heapq

n = 8

times = [
    (1, 2, 4),
    (1, 3, 2),
    (2, 3, 1),
    (2, 4, 5),
    (3, 4, 8),
    (3, 5, 10),
    (4, 5, 2),
    (4, 6, 6),
    (5, 6, 3),
    (5, 7, 1),
    (6, 8, 2),
    (7, 6, 1),
    (7, 8, 4),
    (3, 7, 7),
    (2, 8, 15)
]

k = 1

# the standard

def bellman_ford(edges, start, num_v):
    dist = dict()
    prev = dict()
    
    for i in range(1, num_v+1):
        dist[i] = float('inf')
        prev[i] = None
    
    dist[start] = 0

    for _ in range(num_v-1):
        updated = False
        
        for u, v, w in edges:
            
            # if there is a valid path from start to u
            if dist[u] != float('inf'):
                new_distance_to_v = dist[u] + w
                
                if new_distance_to_v < dist[v]:
                    dist[v] = new_distance_to_v
                    prev[v] = u
                    updated = True
        
        # break if there were no more updates
        if updated == False:
            break
    
    for u, v, w in edges:
        # if there is a valid path from start to u
        if dist[u] != float('inf'):
            new_distance_to_v = dist[u] + w
                
            if new_distance_to_v < dist[v]:
                raise ValueError("negative-cycle detected")
                
    return dist, prev
    
    
def reconstruct_graph(prev, start, destination):
    path = []
    node = destination
    while node != start:
        path.append(node)
        node = prev[node]
    path.append(start)
    
    return list(reversed(path))

if __name__ == "__main__":
    start = k

    dist, prev = bellman_ford(times, start, n)
    
    furthest = max(dist, key=dist.get)
    
    path = reconstruct_graph(prev, start, furthest)
        
    print("\nDistances: ")
    print(dist)
    print("\nPrevious: ")
    print(prev)
    print("\nStart:")
    print(start)
    print("\nFurthest (Deepest) Node: ")
    print(furthest)
    print("\nPath from " + str(start) + " to " + str(furthest) + ": ")
    print(path)
    print("\nCost from " + str(start) + " to " + str(furthest) + ": ")
    print(dist[furthest])
