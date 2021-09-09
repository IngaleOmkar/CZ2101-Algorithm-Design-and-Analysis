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

class HeapPriorityQueue():
    # Required functions: createHeap, heapPush, heapPop
    
    def __init__(self):
        self.queue = []

    def push(self, index, weight):
        newNode = Node(index, weight)
        self.queue.append(newNode)
        self.heapify()
    
    def heapify(self):
        # Storing the node for future saving
        newItemObj = self.queue[len(self.queue)-1]
        # Taking the "weight" as that is used for comparison
        newItem = self.queue[len(self.queue)-1].weight
        pos = len(self.queue) - 1
        while(pos > 0):
            parent_pos = (pos-1) >> 1 #//2
            parent = self.queue[parent_pos].weight
            if(newItem < parent):
                self.queue[pos] = self.queue[parent_pos]
                pos = parent_pos
                continue
            break
        self.queue[pos] = newItemObj
    
    def isEmpty(self):
        return len(self.queue) == 0

    def pop(self):
        #Pop the smallest item off the heap
        lastelt = self.queue.pop()    # raises appropriate IndexError if heap is empty
        if self.queue:
            returnitem = self.queue[0]
            self.queue[0] = lastelt
            self.heapify()
            return returnitem
        return lastelt
    
    def print(self):
        for i in range(len(self.queue)):
            print(self.queue[i].weight, end=',')

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

# Defines the number of "nodes" in the graph
vertices = 100000
# Defines the number of "connections" in the graph
edges = 1000000
# Creates the graph
g = Graph(vertices)
# Creates a new dictionary to ensure no same edge with different weights 
added = {i:[] for i in range(vertices)}
# Populates the graph with randomly generated connections
for i in range(edges):
    start_edge = random.randint(0,vertices-1)
    end_edge = random.randint(0,vertices-1)
    weight = random.randint(0,50)
    if((start_edge != end_edge) and (end_edge not in added[start_edge])):
        added[start_edge].append(end_edge)
        g.addEdge(start_edge, end_edge, weight)

'''# s: 0, u: 1, x: 2, v: 3, y: 4
g.addEdge(0, 1, 10)
g.addEdge(0, 2, 5)
g.addEdge(2, 1, 3)
g.addEdge(1, 2, 2)
g.addEdge(1, 3, 1)
g.addEdge(2, 4, 2)
g.addEdge(4, 0, 7)
g.addEdge(2, 3, 9)
g.addEdge(3, 4, 4)
g.addEdge(4, 3, 6)'''

print(dijkstra(g, 0)[1])