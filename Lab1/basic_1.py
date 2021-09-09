comparison = 0

##################### HYBRID ALGORITHM ######################

def hybrid_algorithm(n, m, arr):
    if(m <= n):
        return 
    elif(m > n):
        if(m - n + 1 < 5):
            insertionSort(arr, n, m + 1)
        else:
            mid = (m + n)//2
            hybrid_algorithm(n, mid, arr)
            hybrid_algorithm(mid + 1, m, arr)
            merge(n, mid, m, arr)

##################### MERGE SORT #####################

def mergesort(n, m, arr):
    global comparison
    if(m <= n):
        return 
    elif(m > n):
        mid = (m + n)//2
        mergesort(n, mid, arr)
        mergesort(mid + 1, m, arr)
        comparison = merge(n, mid, m, arr)

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
    if(len(arr) <= 1):
        return
    for i in range(l + 1, r):
        for j in range (i, l, -1):
            if(arr[j] < arr[j - 1]):
                swap(j, j -1, arr)
            else:
                break

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
from random import randint
#arr = [90,25,10,71,94,22,59,74]
arr = [randint(-9999,9999) for x in range(1000)]
mergesort(0,len(arr)-1,arr)
print(arr, comparison)