import numpy as np
from collections import defaultdict

class Node():
    def __init__(self, data, priority):
        self.data = data
        self.priority = priority

# Work in Progress
class PriorityQueue():
    def __init__(self):
        self.queue = []

    def isEmpty(self):
        return len(self.queue) == 0
    
    def enqueue(self, d, p):
        # Create new node
        newNode = Node(d, p)
        self.queue.append(newNode)

    def dequeue(self):
        if (not self.isEmpty()):
            min = 0
            for i in range(len(self.queue)):
                if(self.queue[i].priority < self.queue[min].priority):
                    min = i
            return self.queue.pop(min)
        else:
            return None # Queue empty, dequeue failed

    def printQueue(self):
        for i in range(len(self.queue)):
            print(self.queue[i].priority)

class Graph():
    def __init__(self, V):
        self.V = V
        self.adjMatrix = np.zeros((self.V, self.V), dtype=int)

    def addEdge(self, src, dest, weight):
        # add edge for adjMatrix
        self.adjMatrix[src][dest] = weight

    def getAdjMatrix(self):
        return self.adjMatrix

    def getGraph(self):
        return self.adjList
