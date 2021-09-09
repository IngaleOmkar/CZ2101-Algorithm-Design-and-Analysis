import csv
from sort import sort
from random import randint

def writeResultsOptimization(fileName, iter, d):
    with open(fileName, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["S", "SavedComparisons"])

        for i in range(0, iter):
            writer.writerow([d["S"][i], d["SavedComparisons"][i]])

if __name__ == "__main__":

    LIMIT = 1000 # Play around with this value to set the limit of the array it will go up until
    MAX_ARR_VAL = 9999 # Set the max possible value in the array

    optimal = {"S":[],"SavedComparisons":[]}
    lower = 4
    upper = 45
    for s in range(lower,upper + 1):
        optimal["S"].append(s)
        sorter = sort(s)
        diff = {"ArraySize": [], "difference": []}

        for i in range(1, LIMIT+1):
            arrh = [randint(-MAX_ARR_VAL,MAX_ARR_VAL) for x in range(i)]
            arrm = arrh.copy()

            diff["ArraySize"].append(i)

            _, comparisonH  = sorter.hybrid_algorithm(0,len(arrh)-1,arrh)

            _, comparisonM = sorter.mergesort(0,len(arrm)-1,arrm)
            
            diff['difference'].append(comparisonM - comparisonH)
            sorter.mt = 0
            sorter.it = 0
            sorter.ht = 0
        
        optimal['SavedComparisons'].append(int(sum(diff["difference"])/len(diff['difference'])))
        print("value of s:", s, "\t|Comparison difference =", int(sum(diff["difference"])/len(diff['difference'])))
    writeResultsOptimization("optimal.csv",upper - lower, optimal)
