import DataStructures as ds
import time

def dijkstra(G, src):
    start = time.time()
    d = [float('inf')] * G.V
    pi = [None] * G.V
    S = [False] * G.V
    priorityQueue = ds.PriorityQueue()
    Graph = G.getAdjMatrix()

    d[src] = 0

    priorityQueue.enqueue(src, 0)
    
    while (not priorityQueue.isEmpty()):
        u = priorityQueue.dequeue()
        S[u.data] = True

        for v in range(G.V):
            if (Graph[u.data][v] > 0 and S[v] == False and d[v] > d[u.data] + Graph[u.data][v]):
                d[v] = d[u.data] + Graph[u.data][v]
                pi[v] = u.data
                priorityQueue.enqueue(v, d[v])
    end = time.time()
    return d, end-start

if __name__ == "__main__":
    # Create a graph of 5 vertices
    g = ds.Graph(5)

    # Add edges
    g.addEdge(0, 1, 10)
    g.addEdge(0, 2, 5)
    g.addEdge(2, 1, 3)
    g.addEdge(1, 2, 2)
    g.addEdge(1, 3, 1)
    g.addEdge(2, 4, 2)
    g.addEdge(4, 0, 7)
    g.addEdge(2, 3, 9)
    g.addEdge(3, 4, 4)
    g.addEdge(4, 3, 6)

    # Perform dijkstras
    res = dijkstra(g, 0)
    print(res)

