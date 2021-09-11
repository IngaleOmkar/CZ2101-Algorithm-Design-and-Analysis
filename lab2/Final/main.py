import csv
import datastructures as ds
import dijkstra
from time import time

# Function for writing the results into a CSV file
def writeResults(fileName, iter, d):
    with open(fileName, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["Number of Vertices", "Time Q1 (ms)", "Time Q2 (ms)"])

        try:
            for i in range(0, iter):
                writer.writerow([d["Number of Vertices"][i], d["Time Q1"][i], d["Time Q2"][i]])
        except IndexError:
            print("Index error... Saved current results")
            return

if __name__ == "__main__":
    ITERATIONS = 1000
    START = 1 # START must at least be 1 

    fileName = 'Lab2_Results_1.csv' # File name for the csv (change the name if want to save to a different file otherwise it will override)

    d = {"Number of Vertices": [], "Time Q1": [], "Time Q2": [], 'SUCCESS': []}

    for i in range(START, ITERATIONS+1):
        try:
            G = ds.Graph(i)
            # G.randomGraph() # Generate random graph (for average case) -> uncomment to use
            G.randomCompleteGraph() # Generate random complete graph (for worst case) -> uncomment to use
            
            d["Number of Vertices"].append(i)

            start = time()
            d1 = dijkstra.dijkstra_pqueue(G, 0)
            end = time()
            q1_elapsedTime = (end - start) * 10**3 # in milliseconds
            d["Time Q1"].append(q1_elapsedTime)

            start = time()
            d2 = dijkstra.dijkstra_hqueue(G, 0)
            end = time()
            q2_elapsedTime = (end - start) * 10**3 # in milliseconds
            d["Time Q2"].append(q2_elapsedTime)

            success = (d1==d2)
            d["SUCCESS"].append(success)
            print(f'{i}: \tQ1 Time: {round(q1_elapsedTime, 5)} \tQ2 Time: {round(q2_elapsedTime, 5)}\tSUCCESS: {success}')

        except (KeyboardInterrupt):
                print("Keyboard Interrupt...")
                break

    writeResults(fileName, ITERATIONS, d)
        
    print('Completed!')
