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
    
    def enqueue(self, v, w):
        # Create new node
        newNode = Node(v, w)

        # Empty queue, insert at head
        if (self.isEmpty()):
            self.queue.insert(0, newNode)
        else:
            # Find correct position & insert
            if (w <= self.queue[0].weight):
                self.queue.insert(0, newNode)
            else:
                for i in range(len(self.queue)):
                    if (w < self.queue[i].weight):
                        self.queue.insert(i, newNode)
                        return

                self.queue.insert(i+1, newNode)

    def dequeue(self):
        if (not self.isEmpty()):
            return self.queue.pop(0)
        else:
            return None # Queue empty, dequeue failed

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
