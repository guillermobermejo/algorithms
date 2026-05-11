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

FUNCTION Dijkstra(Graph, Start):

    CREATE map Distance
    CREATE map Previous
    CREATE PriorityQueue PQ

    FOR each Vertex in Graph:
        Distance[Vertex] ← INFINITY
        Previous[Vertex] ← NULL
        INSERT (INFINITY, Vertex) INTO PQ

    Distance[Start] ← 0
    INSERT (0, Start) INTO PQ   // or update if your PQ supports it

    WHILE PQ is not empty:

        (CurrentDistance, U) ← EXTRACT-MIN(PQ)

        IF CurrentDistance > Distance[U]:
            CONTINUE   // skip outdated entry

        FOR each (Weight, V) in Graph[U]:

            NewDistance ← Distance[U] + Weight

            IF NewDistance < Distance[V]:

                Distance[V] ← NewDistance
                Previous[V] ← U

                INSERT (NewDistance, V) INTO PQ

    RETURN Distance, Previous
'''

from queue import PriorityQueue

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

def dijkstra(graph, start):
    dist = dict()
    prev = dict()
    
    pq = PriorityQueue()
    
    for vertex in graph.keys():
        dist[vertex] = float('inf')
        prev[vertex] = None
        pq.put((float('inf'), vertex))
        
    dist[start] = 0
    
    while not pq.empty():
        dist_u, u = pq.get()
        
        for dist_v, v in graph[u]:
            distance = dist[u] + dist_v
            
            if distance < dist[v]:
                dist[v] = distance
                prev[v] = u
                pq.put((distance, v))
                
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
    dist, prev = dijkstra(adjacency_list, start)
    
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
