import time
import random

class Node():
    def __init__(self, index, weight):
        self.index = index 
        self.next = None 
        # This weight is the weight of edge between 
        # the source index and the node index.
        self.weight = weight
    
    def add_connection(self, next_node):
        self.next = next_node

class Graph():
    def __init__(self, vertices):
        # Creating a list of list of all vertices which 
        # will store the nodes
        self.vertices = [None] * vertices
    
    def addEdge(self, index_from, index_to, weight):
        # creating the node first
        newNode = Node(index_to, weight)
        newNode.add_connection(self.vertices[index_from])
        self.vertices[index_from] = newNode
    
    def printAdjList(self, index):
        node = self.vertices[index]
        while(node != None):
            print(node.index,end='->')
            node = node.next

class HeapPriorityQueue():
    # Required functions: createHeap, heapPush, heapPop
    
    def __init__(self):
        self.queue = []
    
    def pop(self):
        if(self.isEmpty()):
            return None
        else:
            toreturn = self.queue[0]
            self.queue[0] = self.queue[len(self.queue) - 1]
            self.queue.pop(len(self.queue) - 1)
            self.buildHeap()
            return toreturn
    
    def push(self, index, weight):
        self.queue.append(Node(index, weight))
        self.buildHeap()
    
    def heapify(self, i):
        smallest = i; # Initialize smallest as root
        # The following is different because the array is 0 indexed
        l = 2 * i + 1; # left = 2*i + 1
        r = 2 * i + 2; # right = 2*i + 2
    
        # If left child is smaller than root
        if l < len(self.queue) and self.queue[l].weight < self.queue[smallest].weight:
            smallest = l;
    
        # If right child is smaller than smallest so far
        if r < len(self.queue) and self.queue[r].weight < self.queue[smallest].weight:
            smallest = r;
    
        # If smallest is not root
        if smallest != i:
            self.queue[i], self.queue[smallest] = self.queue[smallest], self.queue[i];
            # Recursively heapify the affected sub-tree
            self.heapify(smallest)
  
    # Function to build a Min-Heap from the given array
    def buildHeap(self):
        # Index of last non-leaf node
        startIdx = len(self.queue) // 2 - 1;
        # Perform reverse level order traversal
        # from last non-leaf node and heapify
        # each node
        for i in range(startIdx, -1, -1):
            self.heapify(i);  
        
    def isEmpty(self):
        return len(self.queue) == 0
    
    def printHeap(self):
        print("Array representation of Heap is:");
        for i in range(len(self.queue)):
            print(self.queue[i].weight, end = " ");
        print()

def dijkstra(g, source_index):
    start = time.time()
    d = [float("inf")] * len(g.vertices)
    pi = [None] * len(g.vertices)
    s = [False] * len(g.vertices)

    # Creating the priority queue 
    priority_queue = HeapPriorityQueue()
    # Setting distance for source index to 0
    d[source_index] = 0

    # Pushing source index with weight 0 into the queue
    priority_queue.push(source_index,0)

    while(not priority_queue.isEmpty()):
        current = priority_queue.pop()
        s[current.index] = True
        adj_node = g.vertices[current.index]
        # traversing the linked list
        while(adj_node != None):
            if(not s[adj_node.index] and d[adj_node.index] > d[current.index] + adj_node.weight):
                d[adj_node.index] = d[current.index] + adj_node.weight
                pi[adj_node.index] = current.index
                priority_queue.push(adj_node.index, d[adj_node.index])
            adj_node = adj_node.next
    end = time.time()
    return d, end-start
