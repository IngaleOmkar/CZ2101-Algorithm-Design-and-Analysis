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

class PriorityQueue():

    def __init__(self):
        self.heap = []

    def isEmpty(self):
        return len(self.heap) == 0
    
    def heappush(self, index, weight):
        """Push item onto heap, maintaining the heap invariant."""
        newNode = Node(index, weight)
        self.heap.append(newNode)
        self._siftdown(0, len(self.heap)-1)

    def heappop(self):
        """Pop the smallest item off the heap, maintaining the heap invariant."""
        lastelt = self.heap.pop()    # raises appropriate IndexError if heap is empty
        if self.heap:
            returnitem = self.heap[0]
            self.heap[0] = lastelt
            self._siftup(0)
            return returnitem
        return lastelt
    
    def _siftdown(self, startpos, pos):
        newitem = self.heap[pos]
        # Follow the path to the root, moving parents down until finding a place
        # newitem fits.
        while pos > startpos:
            parentpos = (pos - 1) >> 1
            parent = self.heap[parentpos]
            if newitem.weight < parent.weight:
                self.heap[pos] = parent
                pos = parentpos
                continue
            break
        self.heap[pos] = newitem
    
    def _siftup(self, pos):
        endpos = len(self.heap)
        startpos = pos
        newitem = self.heap[pos]
        # Bubble up the smaller child until hitting a leaf.
        childpos = 2*pos + 1    # leftmost child position
        while childpos < endpos:
            # Set childpos to index of smaller child.
            rightpos = childpos + 1
            if rightpos < endpos and not self.heap[childpos].weight < self.heap[rightpos].weight:
                childpos = rightpos
            # Move the smaller child up.
            self.heap[pos] = self.heap[childpos]
            pos = childpos
            childpos = 2*pos + 1
        # The leaf at pos is empty now.  Put newitem there, and bubble it up
        # to its final resting place (by sifting its parents down).
        self.heap[pos] = newitem
        self._siftdown(startpos, pos)


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
            parent_pos = (pos-1) >> 1 # Divide by 2
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
    priority_queue = PriorityQueue()
    # Setting distance for source index to 0
    d[source_index] = 0

    # Pushing source index with weight 0 into the queue
    priority_queue.heappush(source_index,0)

    while(not priority_queue.isEmpty()):
        current = priority_queue.heappop()
        s[current.index] = True
        adj_node = g.vertices[current.index]
        # traversing the linked list
        while(adj_node != None):
            if(not s[adj_node.index] and d[adj_node.index] > d[current.index] + adj_node.weight):
                d[adj_node.index] = d[current.index] + adj_node.weight
                pi[adj_node.index] = current.index
                priority_queue.heappush(adj_node.index, d[adj_node.index])
            adj_node = adj_node.next
    end = time.time()
    return d, end-start

g = Graph(5)
g.addEdge(0,1,10)
g.addEdge(0,2,5)
g.addEdge(1,2,2)
g.addEdge(2,1,3)
g.addEdge(1,3,1)
g.addEdge(2,3,9)
g.addEdge(2,4,2)
g.addEdge(3,4,4)
g.addEdge(4,3,6)

print(dijkstra(g,0))