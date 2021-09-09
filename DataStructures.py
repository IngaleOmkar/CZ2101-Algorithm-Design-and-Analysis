import numpy as np
from random import randint
from collections import defaultdict

class Node():
    def __init__(self, v, w):
        self.vertex = v
        self.weight = w

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
                    if (w > self.queue[i].weight):
                        self.queue.insert(i+1, newNode)

    def dequeue(self):
        if (not self.isEmpty()):
            return self.queue.pop(0)
        else:
            return None # Queue empty, dequeue failed

    def printQueue(self):
        for i in range(len(self.queue)):
            print(self.queue[i].weight)

# Work in Progress
class Heap():
    def __init__(self, heapSize):
        # Create a heap of heapSize nodes
        # Zero-indexed heap
        self.heap = [float('inf')] * heapSize

    def parent(self, pos):
        if (pos == 0):
            return None # pos == 0 -> it is the root node
        return pos//2
    
    def leftChild(self, pos):
        return pos//2 + 1

    def rightChild(self, pos):
        return pos//2 + 2

    def heapify(self):
        pass

    def fixHeap(self):
        pass

    def deleteMin(self):
        pass

    def pop(self):
        pass

    def push(self, d, p):
        newNode = Node(d, p)
        self.heap.append(newNode)

    def isEmpty(self):
        return len(self.heap) == 0

    def printHeap(self):
        print(self.heap)

    def getHeap(self):
        return self.heap

class Graph():
    def __init__(self, V, MAX_WEIGHT):
        self.V = V
        self.MAX_WEIGHT = MAX_WEIGHT
        self.adjList = defaultdict(list)
        self.adjMatrix = np.zeros((self.V, self.V), dtype=int)

    def addEdge(self, src, dest, weight):
        # add edge for adjList
        newNode = Node(dest, weight)
        self.adjList[src].insert(0, newNode)

        # add edge for adjMatrix
        self.adjMatrix[src][dest] = weight

    def randomGraph(self):
        # Create a random graph of size V
        for src in range(self.V):
            edges = randint(0, self.V - 1)
            if (edges == 0):
                continue
            else:
                for edge in range(edges):
                    destinations = []
                    dest = randint(1, self.V - 1)
                    if dest not in destinations:
                        destinations.append(dest)
                    while dest in destinations:
                        dest = randint(1, self.V - 1)

                    self.addEdge(src, dest, randint(1, 100))

    def getAdjList(self):
        # output -> src: [[dest, weight]]
        return self.adjList

    def getAdjMatrix(self):
        return self.adjMatrix

    def getGraph(self):
        return self.adjList, self.adjMatrix
