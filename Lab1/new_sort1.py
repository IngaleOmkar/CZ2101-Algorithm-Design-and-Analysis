hybrid_comparison = 0
insertion_comparison = 0
merge_comparison = 0
s =0
##################### HYBRID ALGORITHM ######################

def hybrid_algorithm(n, m, arr):
    global hybrid_comparison, s
    if(m <= n):
        return 
    elif(m > n):
        if(m - n + 1 < s):
            print("before", hybrid_comparison)
            hybrid_comparison += insertionSort(arr, n, m)
            print("added", hybrid_comparison)
        else:
            mid = (m + n)//2
            hybrid_algorithm(n, mid, arr)
            hybrid_algorithm(mid + 1, m, arr)
            hybrid_comparison = hybrid_merge(n, mid, m, arr)

def hybrid_merge(n, mid, m, arr):
    comparison = 0 
    a = n # "Running index" for left sub-array
    b = mid + 1 # "Running index" for right sub-array
    while(a <= mid and b <= m): #both sub-arrays "not empty"
        if(arr[a] <= arr[b]):
            a += 1
            comparison += 1
        else:
            num = arr[b]
            shift(a, b, arr)
            arr[a] = num
            a += 1
            b += 1
            mid += 1
            comparison += 1
    return comparison

##################### MERGE SORT #####################

def mergesort(n, m, arr):
    global merge_comparison
    if(m <= n):
        return 
    elif(m > n):
        mid = (m + n)//2
        mergesort(n, mid, arr)
        mergesort(mid + 1, m, arr)
        merge_comparison = merge(n, mid, m, arr)

def merge(n, mid, m, arr):
    comparison = 0 
    a = n # "Running index" for left sub-array
    b = mid + 1 # "Running index" for right sub-array
    while(a <= mid and b <= m): #both sub-arrays "not empty"
        if(arr[a] <= arr[b]):
            a += 1
            comparison += 1
        else:
            num = arr[b]
            shift(a, b, arr)
            arr[a] = num
            a += 1
            b += 1
            mid += 1
            comparison += 1
    return comparison

################### INSERTION SORT ###################

def insertionSort(arr, l, r):
    global insertion_comparison
    counter = 0
    if(len(arr) <= 1):
        return 0
    for i in range(l + 1, r+1):
        for j in range (i, l, -1):
            if(arr[j] < arr[j - 1]):
                swap(j, j -1, arr)
                counter += 1
            else:
                counter += 1
                break
    insertion_comparison = counter
    return counter

############## HELPER FUNCTIONS #############

def shift(i, j, arr):
    for ind in range(j,i,-1):
        arr[ind] = arr[ind - 1]

def applyMergeSort(arr):
    m = len(arr) - 1
    mergesort(0, len(arr) - 1, arr)

def swap(i, j, arr):
    arr[i], arr[j] = arr[j], arr[i]

############ TESTING ########################

arr = [90,25,10,71,94,22,59,74]
arr1 = arr.copy()
hybrid_algorithm(0,len(arr)-1, arr)
print(arr,hybrid_comparison)
mergesort(0,len(arr1)-1, arr1)
print(arr1,merge_comparison)
insertionSort([45,29,6,64,12,16],0,5)
print("i", insertion_comparison)
'''

import csv
from random import randint

def writeResultsOptimization(fileName, iter, d):
    with open(fileName, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["S", "Difference"])

        for i in range(0, iter):
            writer.writerow([d["S"][i], d["Difference"][i]])

LIMIT = 1000 # Play around with this value to set the limit of the array it will go up until
MAX_ARR_VAL = 9999 # Set the max possible value in the array

optimal = {"S":[],"Difference":[]}
lower = 4
upper = 45
for a in range(lower,upper + 1):
    optimal["S"].append(s)
    diff = {"ArraySize": [], "difference": []}
    s = a
    for i in range(1, LIMIT+1):
        arrh = [randint(-MAX_ARR_VAL,MAX_ARR_VAL) for x in range(i)]
        arrm = arrh.copy()

        diff["ArraySize"].append(i)

        hybrid_algorithm(0,len(arrh)-1,arrh)

        mergesort(0,len(arrm)-1,arrm)
            
        diff['difference'].append(merge_comparison - hybrid_comparison)
        merge_comparison = 0
        hybrid_comparison = 0
        insertion_comparison = 0
        
    optimal['Difference'].append(int(sum(diff["difference"])/len(diff['difference'])))
    print("value of s:", s, "\t|Mean Comparison difference =", int(sum(diff["difference"])/len(diff['difference'])))
writeResultsOptimization("optimal.csv",upper - lower, optimal)
'''