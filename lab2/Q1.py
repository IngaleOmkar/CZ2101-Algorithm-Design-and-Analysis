import DataStructures as ds

def Graph(vertices):
    # This 2D list, arr, is the adjacency matrix
    return [[0 for i in range(vertices)] for j in range(vertices)]

def add_connection(graph, vertex_from, vertex_to, weight):
    graph[vertex_from][vertex_to] = weight

def dijkstra(graph, source_index):

    # all initial distances set to infinity.
    distances = [float('inf')] * len(graph)

    # all predecessor index set to None.
    # This implies no index has been visited
    visited_from = [None] * len(graph)

    # This is a list of all the indexes that have already been visited
    visited = [False] * len(graph)

    # setting distance of source index to 0
    distances[source_index] = 0

    # initializing the priority queue 
    priority_queue = ds.PriorityQueue()

    # inserting all indices into the priority queue 
    priority_queue.enqueue(source_index, 0)

    while(not priority_queue.isEmpty()):
        current_index = priority_queue.dequeue().data
        visited[current_index] = True
        # Traversing all adjacent indexes for this graph
        for adjacent_vertex in range(len(graph[current_index])):
            if(graph[current_index][adjacent_vertex] == 0):
                continue
            if(not visited[adjacent_vertex] and 
                distances[adjacent_vertex] > distances[current_index] + graph[current_index][adjacent_vertex]):
                
                # Updating the distance
                distances[adjacent_vertex] = distances[current_index] + graph[current_index][adjacent_vertex]

                # Saving the index of origin
                visited_from[adjacent_vertex] = current_index

                # adding the index to the priority queue
                priority_queue.enqueue(adjacent_vertex, distances[adjacent_vertex])
    
    return distances

# Checking the graph based on lecture slides

g = Graph(5)
# s: 0, x: 1, u: 2, v: 3, y: 4
add_connection(g,0,1,5)
add_connection(g,0,2,10)
add_connection(g,2,3,1)
add_connection(g,1,4,2)
add_connection(g,4,3,6)
add_connection(g,3,4,4)
add_connection(g,1,3,9)
add_connection(g,2,1,2)
add_connection(g,1,2,3)
add_connection(g,4,0,7)

# calling on the dijsktra's algorithm to calculate distance
print(dijkstra(g, 0))

# Works!!

