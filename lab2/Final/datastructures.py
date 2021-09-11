import numpy as np
from random import randint

# Node for priority queue
class Node():
    def __init__(self, data, priority):
        self.data = data
        self.priority = priority

# Node for linked list
class ListNode():
    def __init__(self, index, weight):
        self.idx = index
        self.weight = weight
        self.next = None

    def addConnection(self, nextNode):
        self.next = nextNode

# Graph data structure
class Graph():
    def __init__(self, V):
        self.V = V

        # Create a size V * V adjMatrix of weights 0
        self.adjMatrix = np.zeros((self.V, self.V), dtype=int)

        # Creating a adjList
        self.adjList = [None] * self.V

    def addEdge(self, src, dest, weight):
        # add edge for adjMatrix
        self.adjMatrix[src][dest] = weight

        # add edge for adjList
        newNode = ListNode(dest, weight)
        newNode.addConnection(self.adjList[src])
        self.adjList[src] = newNode

    # Create a random graph of specified size (vertices)
    # Populate both adjMatrix & adjList
    def randomGraph(self):
        # For every vertex in the graph
        # Randomly generate the number of edges it will connect to
        # For each edge if the destination already exists or the destination is itself
        # get another destination vertex
        for src in range(self.V):
            numOfEdges = randint(0, self.V - 1)
            if (numOfEdges == 0):
                continue
            else:
                added = []
                for edge in range(numOfEdges):
                    dest = randint(0, self.V - 1)
                    while dest in added or dest == src:
                        dest = randint(0, self.V - 1)
                    added.append(dest)
                    self.addEdge(src, dest, randint(1, 50))
                added = []

    # Create a random complete graph
    # Worst case graph
    def randomCompleteGraph(self):
        for src in range(self.V):
            edges = self.V - 1 # V - 1 edges
            for edge in range(edges+1):
                if (edge != src):
                    self.addEdge(src, edge, randint(1, 100))
                    
    def getAdjMatrix(self):
        return self.adjMatrix

    def getAdjList(self):
        return self.adjList

    # Debugging
    # def printAdjList(self):
    #     for i in range(len(self.adjList)):
    #         print("i: ", i)
    #         if self.adjList[i] != None:
    #             cur = self.adjList[i]
    #             while cur != None:
    #                 print(i, cur.idx, cur.weight)
    #                 cur = cur.next

# Priority queue data structure
class PriorityQueue():
    def __init__(self):
        self.queue = []

    # Checks if queue is empty
    # Returns boolean value
    def isEmpty(self):
        return len(self.queue) == 0
    
    # Enqueue inserts the elements according to their priority
    # In our case, the priority are the weight of the graph
    # Hence, the shorter distance indicates a higher priority
    def enqueue(self, d, p):
        # Create new node
        newNode = Node(d, p)

        # Empty queue, insert at head
        if (self.isEmpty()):
            self.queue.insert(0, newNode)
        else:
            # Find correct position & insert
            if (p <= self.queue[0].priority):
                self.queue.insert(0, newNode)
            else:
                for i in range(len(self.queue)):
                    if (p < self.queue[i].priority):
                        self.queue.insert(i, newNode)
                        return

                self.queue.insert(i+1, newNode)

    # Dequeue pops the element at the head of the list
    # The priority queue is already sorted upon insertion
    def dequeue(self):
        if (not self.isEmpty()):
            return self.queue.pop(0)
        else:
            return None # Queue empty, dequeue failed

# Heap data structure
class HeapPriorityQueue():
    def __init__(self):
        self.queue = []
    
    def pop(self):
        if(self.isEmpty()):
            return None
        else:
            toreturn = self.queue[0]
            self.queue[0] = self.queue[len(self.queue) - 1]
            self.queue.pop(len(self.queue) - 1)
            self.heapify(0)
            return toreturn
    
    def push(self, index, weight):
        self.queue.append(ListNode(index, weight))# adding to last position
        self.queue.insert(0, None)# making heap start from 1
        self.move_up(len(self.queue)-1)# 
        del self.queue[0]
    
    def move_up(self, i):
        """
        Moves the value up in the tree to maintain the heap property.
        """
        # While the element is not the root or the left element
        while(i // 2 > 0): # get to root, 0
            # If the element is less than its parent swap the elements
            if self.queue[i].weight < self.queue[i// 2].weight:
                self.queue[i], self.queue[i// 2] = self.queue[i// 2], self.queue[i]
            # Move the index to the parent to keep the properties
            i = i // 2

    def heapify(self, i):
        smallest = i; # Initialize smallest as root
        # The following is different because the array is 0 indexed
        l = 2 * i + 1; # left = 2*i + 1
        r = 2 * i + 2; # right = 2*i + 2
    
        # If left child is smaller than root
        if(l < len(self.queue) and self.queue[l].weight < self.queue[smallest].weight):
            smallest = l;
    
        # If right child is smaller than smallest so far
        if(r < len(self.queue) and self.queue[r].weight < self.queue[smallest].weight):
            smallest = r;
    
        # If smallest is not root
        if(smallest != i):
            self.queue[i], self.queue[smallest] = self.queue[smallest], self.queue[i];
            # Recursively heapify the affected sub-tree
            self.heapify(smallest)
        
    def isEmpty(self):
        return len(self.queue) == 0
    
    # Debugging
    # def printHeap(self):
    #     print("Array representation of Heap is:")
    #     for i in range(len(self.queue)):
    #         print(self.queue[i].weight, end = " ")
    #     print()