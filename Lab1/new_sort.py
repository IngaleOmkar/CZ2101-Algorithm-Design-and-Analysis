hybrid_comparison = 0
insertion_comparison = 0
merge_comparison = 0

##################### HYBRID ALGORITHM ######################

def hybrid_algorithm(n, m, arr):
    global hybrid_comparison
    if(m <= n):
        return 
    elif(m > n):
        if(m - n + 1 < 5):
            hybrid_comparison += insertionSort(arr, n, m)
        else:
            mid = (m + n)//2
            hybrid_algorithm(n, mid, arr)
            hybrid_algorithm(mid + 1, m, arr)
            hybrid_comparison = merge(n, mid, m, arr)

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
    insertion_comparison += counter
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
from random import randint
arr = [randint(-9999,9999) for x in range(20000)]
arr1 = arr.copy()
mergesort(0,len(arr)-1,arr)
print(merge_comparison)
hybrid_algorithm(0,len(arr1)-1,arr1)
print(hybrid_comparison)

'''
mergesort(0,len(arr)-1,arr)
print(merge_comparison)
hybrid_algorithm(0,len(arr1),arr1)
print(hybrid_comparison)'''