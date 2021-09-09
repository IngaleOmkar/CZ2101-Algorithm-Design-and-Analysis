import csv
from sort import sort
from random import randint

def writeResults(fileName, iter, d):
    with open(fileName, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["Array Size", "hybridSort Time (ms)", "insertionSort Time (ms)", "mergeSort Time (ms)"])

        for i in range(0, iter):
            writer.writerow([d["ArraySize"][i], d["hybridSort"][i], d["insertionSort"][i], d["mergeSort"][i]])

def writeResultsComparison(fileName, iter, d):
    with open(fileName, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["Array Size", "hybridSort", "insertionSort", "mergeSort"])

        for i in range(0, iter):
            writer.writerow([d["ArraySize"][i], d["hybridSort"][i], d["insertionSort"][i], d["mergeSort"][i]])

if __name__ == "__main__":

    LIMIT = 1000 # Play around with this value to set the limit of the array it will go up until
    MAX_ARR_VAL = 9999 # Set the max possible value in the array

    for s in range(9,10):
        sorter = sort(s)
        d = {"ArraySize": [], "hybridSort": [], "insertionSort": [], "mergeSort": []}
        c = {"ArraySize": [], "hybridSort": [], "insertionSort": [], "mergeSort": []}
        print("Running...")

        for i in range(1, LIMIT+1):
            arrh = [randint(-MAX_ARR_VAL,MAX_ARR_VAL) for x in range(i)]
            arrm = arrh.copy() 
            arri = arrh.copy()

            d["ArraySize"].append(i)
            c["ArraySize"].append(i)
            ########## HYBRID #############

            hybridTime, comparisonH  = sorter.hybrid_algorithm(0,len(arrh)-1,arrh)
            d["hybridSort"].append(hybridTime)
            c["hybridSort"].append(comparisonH)

            ######### INSERTION ############

            insertionTime, comparisonI = sorter.insertionSort(arri,0,len(arri))
            d["insertionSort"].append(insertionTime)
            c["insertionSort"].append(comparisonI)

            ######### MERGE ################

            mergeTime, comparisonM = sorter.mergesort(0,len(arrm)-1,arrm)
            d["mergeSort"].append(mergeTime)
            c["mergeSort"].append(comparisonM)
            ######### PRINT ################
            print(i, "\t", hybridTime, "\t", insertionTime, "\t", mergeTime, "\t", comparisonH, "\t", comparisonI, "\t", comparisonM)

        fileName = "results_time"+str(s)+".csv"
        fileNameC = "results_comparison"+str(s)+".csv"
        writeResults(fileName, LIMIT, d)
        writeResultsComparison(fileNameC, LIMIT, c)

    print("Completed!")