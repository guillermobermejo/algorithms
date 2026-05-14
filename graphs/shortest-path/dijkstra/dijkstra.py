'''
Network Delay Time Question

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
Dijkstra Psuedocode

DIJKSTRA(graph, start)

    dist ← empty map
    prev ← empty map

    pq ← empty min-heap

    FOR each vertex v in graph:
        dist[v] ← ∞
        prev[v] ← null

    dist[start] ← 0

    INSERT (0, start) INTO pq

    WHILE pq is not empty:

        (dist_u, u) ← REMOVE-MIN(pq)

        // Ignore outdated heap entries
        IF dist_u > dist[u]:
            CONTINUE

        FOR each (weight, v) adjacent to u:

            new_dist ← dist[u] + weight

            IF new_dist < dist[v]:

                dist[v] ← new_dist
                prev[v] ← u

                INSERT (new_dist, v) INTO pq

    RETURN dist, prev
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

def create_adjacency_list(num_nodes, lst):
    adjacency = dict()
    
    for u, v, weight in lst:
        if u not in adjacency:
            adjacency[u] = []
            
        adjacency[u].append((weight, v))
     
    # nodes are numbers starting at 1. If n = 8 then nodes are 1-8 inclusive.
    # handle leaf node case as neighbors being []
    for i in range(1, num_nodes + 1):
        if i not in adjacency:
            adjacency[i] = []
        
    return adjacency


# the standard

def dijkstra_heapq(graph, start):
    dist = dict()
    prev = dict()
    
    pq = []                                             # init
    
    for vertex in graph.keys():
        dist[vertex] = float('inf')
        prev[vertex] = None
    
    dist[start] = 0
    heapq.heappush(pq, (0, start))                      # <>.heappush(init, x)
    
    while len(pq) != 0:                                 # len(init)
        dist_u, u = heapq.heappop(pq)                   # <>.heappop(init)
        
        # ignore paths to u that are greater than the current best path to u
        if dist_u > dist[u]:
            continue
        
        for dist_v, v in graph[u]:
            new_dist_to_v = dist[u] + dist_v
            
            if new_dist_to_v < dist[v]:
                dist[v] = new_dist_to_v
                prev[v] = u
                heapq.heappush(pq, (new_dist_to_v, v))  # <>.heappush(init, x)
                
    return dist, prev


def dijkstra_priorityqueue(graph, start):
    dist = dict()
    prev = dict()
    
    pq = PriorityQueue()                                # init
    
    for vertex in graph.keys():
        dist[vertex] = float('inf')
        prev[vertex] = None
    
    dist[start] = 0
    pq.put((0, start))                                  # init.put(x)
    
    while not pq.empty():                               # init.empty()
        dist_u, u = pq.get()                            # init.get()
        
        # ignore paths to u that are greater than the current best path to u
        if dist_u > dist[u]:
            continue
        
        for dist_v, v in graph[u]:
            new_dist_to_v = dist[u] + dist_v
            
            if new_dist_to_v < dist[v]:
                dist[v] = new_dist_to_v
                prev[v] = u
                pq.put((new_dist_to_v, v))              # init.put(x)
                
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

    adjacency_list = create_adjacency_list(n, times)
    dist, prev = dijkstra_heapq(adjacency_list, start)
    
    furthest = max(dist, key=dist.get)
    
    path = reconstruct_graph(prev, start, furthest)
        
    print("Adjacency List: ")
    print(adjacency_list)
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
