import DataStructures as ds

def dijkstra_pqueue(G, src):
    d = [float('inf')] * G.V
    pi = [None] * G.V
    S = [False] * G.V

    priorityQueue = ds.PriorityQueue()
    Graph = G.getAdjMatrix()

    d[src] = 0

    priorityQueue.enqueue(0, d[0])

    while (not priorityQueue.isEmpty()):
        u = priorityQueue.dequeue()
        S[u.data] = True

        for v in range(G.V):
            if (Graph[u.data][v] > 0 and S[v] == False and d[v] > d[u.data] + Graph[u.data][v]):
                d[v] = d[u.data] + Graph[u.data][v]
                pi[v] = u.data
                priorityQueue.enqueue(v, d[v])

    return d

def dijkstra_hqueue(G, src):
    d = [float('inf')] * len(G.adjList)
    pi = [None] * len(G.adjList)
    S = [False] * len(G.adjList)

    # Create heap
    heap = ds.HeapPriorityQueue()

    d[src] = 0

    heap.push(src, 0)

    while (not heap.isEmpty()):
        current = heap.pop()
        S[current.idx] = True
        adjNode = G.adjList[current.idx]

        # Traversing linked list
        while (adjNode != None):
            if (not S[adjNode.idx] and d[adjNode.idx] > d[current.idx] + adjNode.weight):
                d[adjNode.idx] = d[current.idx] + adjNode.weight
                pi[adjNode.idx] = current.idx
                heap.push(adjNode.idx, d[adjNode.idx])
            adjNode = adjNode.next
    
    return d