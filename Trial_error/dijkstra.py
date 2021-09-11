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