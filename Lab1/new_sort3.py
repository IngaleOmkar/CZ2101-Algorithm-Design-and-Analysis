hybrid_comparison = 0
insertion_comparison = 0
merge_comparison = 0
s = 5

hybrid_arr = []
merge_arr = []
##################### HYBRID ALGORITHM ######################

def hybrid_algorithm(n, m):
    global hybrid_comparison, s, hybrid_arr, insertion_comparison
    if(m <= n):
        return 
    elif(m > n):
        if(m - n + 1 < s):
            insertionSort(n, m)
            #print("b",hybrid_comparison)
            hybrid_comparison += insertion_comparison
            #print("ta",insertion_comparison,"after",hybrid_comparison)
            insertion_comparison = 0
        else:
            mid = (m + n)//2
            hybrid_algorithm(n, mid)
            hybrid_algorithm(mid + 1, m)
            hybrid_comparison = hybrid_merge(n, mid, m)

def hybrid_merge(n, mid, m):
    comparison = 0 
    a = n # "Running index" for left sub-array
    b = mid + 1 # "Running index" for right sub-array
    while(a <= mid and b <= m): #both sub-arrays "not empty"
        if(hybrid_arr[a] <= hybrid_arr[b]):
            a += 1
            comparison += 1
        else:
            num = hybrid_arr[b]
            shift(a, b)
            hybrid_arr[a] = num
            a += 1
            b += 1
            mid += 1
            comparison += 1
    return comparison

##################### MERGE SORT #####################

def mergesort(n, m):
    global merge_comparison, merge_arr
    if(m <= n):
        return 
    elif(m > n):
        mid = (m + n)//2
        mergesort(n, mid)
        mergesort(mid + 1, m)
        merge_comparison = merge(n, mid, m)

def merge(n, mid, m):
    global merge_arr
    comparison = 0 
    a = n # "Running index" for left sub-array
    b = mid + 1 # "Running index" for right sub-array
    while(a <= mid and b <= m): #both sub-arrays "not empty"
        if(merge_arr[a] <= merge_arr[b]):
            a += 1
            comparison += 1
        else:
            num = merge_arr[b]
            shift_merge(a, b)
            merge_arr[a] = num
            a += 1
            b += 1
            mid += 1
            comparison += 1
    return comparison

################### INSERTION SORT ###################

def insertionSort(l, r):
    global insertion_comparison, hybrid_arr
    counter = 0
    if(len(hybrid_arr) <= 1):
        return 0
    for i in range(l + 1, r+1):
        for j in range (i, l, -1):
            if(hybrid_arr[j] < hybrid_arr[j - 1]):
                swap(j, j -1)
                counter += 1
            else:
                counter += 1
                break
    insertion_comparison = counter
    return counter

############## HELPER FUNCTIONS #############

def shift(i, j):
    global hybrid_arr
    for ind in range(j,i,-1):
        hybrid_arr[ind] = hybrid_arr[ind - 1]

def shift_merge(i, j):
    global merge_arr
    for ind in range(j,i,-1):
        merge_arr[ind] = merge_arr[ind - 1]

def applyMergeSort(arr):
    m = len(arr) - 1
    mergesort(0, len(arr) - 1, arr)

def swap(i, j):
    global hybrid_arr
    hybrid_arr[i], hybrid_arr[j] = hybrid_arr[j], hybrid_arr[i]

def swap_merge(i, j):
    global merge_arr
    merge_arr[i], merge_arr[j] = merge_arr[j], merge_arr[i]

############ TESTING ########################

hybrid_arr = [i for i in range(1000,-1,-1)]
#[90,25,10,71,94,22,59,74,99,-3,1,2,3,4]
merge_arr = hybrid_arr.copy()
hybrid_algorithm(0,len(hybrid_arr)-1)
print(hybrid_arr, hybrid_comparison)
mergesort(0,len(merge_arr)-1)
print(merge_arr, merge_comparison)

'''

import csv
from random import randint

def writeResultsOptimization(fileName, iter, d):
    with open(fileName, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["S", "Difference"])

        for i in range(0, iter):
            writer.writerow([d["S"][i], d["Difference"][i]])

LIMIT = 500 # Play around with this value to set the limit of the array it will go up until
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