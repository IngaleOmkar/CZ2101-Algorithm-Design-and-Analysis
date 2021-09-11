import csv
from os import write
import DataStructures as ds
import dijkstra
from time import time

def writeResults(fileName, iter, d):
    with open(fileName, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["Number of Vertices", "Time Q1 (ms)", "Time Q2 (ms)"])

        for i in range(0, iter):
            writer.writerow([d["Number of Vertices"][i], d["Time Q1"][i], d["Time Q2"][i]])

if __name__ == "__main__":
    ITERATIONS = 600

    fileName = 'Lab2_Results.csv'

    d = {"Number of Vertices": [], "Time Q1": [], "Time Q2": []}

    try:
        for i in range(300, ITERATIONS+1):
            G = ds.Graph(i)
            G.randomCompleteGraph()
            
            d["Number of Vertices"].append(i)

            start = time()
            dijkstra.dijkstra_pqueue(G, 0)
            end = time()
            q1_elapsedTime = (end - start) * 10**3 # milliseconds
            d["Time Q1"].append(q1_elapsedTime)

            start = time()
            dijkstra.dijkstra_pqueue(G, 0)
            end = time()
            q2_elapsedTime = (end - start) * 10**3 # milliseconds
            d["Time Q2"].append(q2_elapsedTime)

            print(f'{i}: \tQ1 Time: {round(q1_elapsedTime, 5)} \tQ2 Time: {round(q2_elapsedTime, 5)}')

    except KeyboardInterrupt:
            writeResults(fileName, ITERATIONS, d)
            print("Keyboard Interrupt... Saving current results...")
            print('Completed!')

    writeResults(fileName, ITERATIONS, d)
    print('Completed!')