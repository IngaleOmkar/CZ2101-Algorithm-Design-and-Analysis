from random import randint
from timeit import default_timer as timer
import csv

h_list = [] # Global hybrid list
m_list = [] # Global merge sort list
s = 4 # Global variable for hybrid algorithm shift parameter
ic = 0 
h_c = 0
m_c = 0

def hybrid_sort(l, r): # m and n are inclusive 
    global ic, h_c
    start = timer() * 1000
    if(r - l <= 0):
        return 0
    elif(r - l + 1 < s):
        ic += insertion_sort(l, r)
    else:
        m = (l + r)//2
        hybrid_sort(l, m)
        hybrid_sort(m + 1, r)
        h_c = merge_hybrid(l, m, r)
    end = timer() * 1000
    return end-start

def merge_hybrid(l,m,r):
    global h_list
    a = l # "Running index" for left sub-array
    b = m + 1 # "Running index" for right sub-array
    c = 0
    while(a <= m and b <= r): #both sub-arrays "not empty"
        if(h_list[a] <= h_list[b]):
            a += 1
        else:
            num = h_list[b]
            shift(a, b)
            h_list[a] = num
            a += 1
            b += 1
            m += 1
        c += 1
    return c

def merge_sort(l, r): # m and n are inclusive 
    global m_c
    start = timer() * 1000
    global m_comparisons
    if(r - l <= 0):
        return 0
    else:
        m = (l + r)//2
        merge_sort(l, m)
        merge_sort(m + 1, r)
        m_c = merge_merge(l, m, r)
    end = timer() * 1000
    return end - start

def merge_merge(l,m,r):
    global m_list
    a = l # "Running index" for left sub-array
    b = m + 1 # "Running index" for right sub-array
    c = 0
    while(a <= m and b <= r): #both sub-arrays "not empty"
        if(m_list[a] <= m_list[b]):
            a += 1
        else:
            num = m_list[b]
            shift_merge(a, b)
            m_list[a] = num
            a += 1
            b += 1
            m += 1
        c += 1
    return c

# Working 
def insertion_sort(l, r):
    global h_list
    c = 0
    if(r - l + 1 <= 1):
        return 0
    for i in range(l + 1, r+1):
        for j in range (i, l, -1):
            c += 1
            if(h_list[j] < h_list[j - 1]):
                h_list[j], h_list[j-1] = h_list[j-1], h_list[j]
            else:
                break
    return c

def shift(i, j):
    global h_list
    for ind in range(j,i,-1):
        h_list[ind] = h_list[ind - 1]

def shift_merge(i, j):
    global m_list
    for ind in range(j,i,-1):
        m_list[ind] = m_list[ind - 1]

####################### TESTING ###########################

h_list = [randint(-9999,9999) for x in range(100)]
m_list = h_list.copy()
h = hybrid_sort(0,len(h_list)-1)
m = merge_sort(0,len(m_list)-1)
print("H:\t", h, "\tM:\t", m)
print(ic+h_c)
print(m_c)