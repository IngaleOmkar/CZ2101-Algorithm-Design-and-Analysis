from timeit import default_timer as timer

class sort():
    ##################### HYBRID ALGORITHM ######################

    def __init__(self,s):
        self.s = s
        self.ht = 0
        self.it = 0
        self.mt = 0

    def hybrid_algorithm(self, n, m, arr):
        start = timer() * 1000
        if(m <= n):
            return 0,0
        elif(m > n):
            if(m - n + 1 < self.s):
                self.insertionSort(arr, n, m + 1)
                self.ht += self.it
            else:
                mid = (m + n)//2
                self.hybrid_algorithm(n, mid, arr)[1]
                self.hybrid_algorithm(mid + 1, m, arr)[1]
                self.ht = self.merge(n, mid, m, arr)
        end = timer() * 1000
        return [end - start, self.ht]

    ##################### MERGE SORT #####################

    def mergesort(self, n, m, arr):
        start = timer() * 1000
        if(m <= n):
            return 0,0
        elif(m > n):
            mid = (m + n)//2
            self.mergesort(n, mid, arr)[1]
            self.mergesort(mid + 1, m, arr)[1]
            self.mt = self.merge(n, mid, m, arr)
        end = timer() * 1000
        return [end - start, self.mt]

    def merge(self, n, mid, m, arr):
        comparisons = 0
        a = n # "Running index" for left sub-array
        b = mid + 1 # "Running index" for right sub-array
        while(a <= mid and b <= m): #both sub-arrays "not empty"
            if(arr[a] <= arr[b]):
                a += 1
                comparisons += 1
            else:
                num = arr[b]
                self.shift(a, b, arr)
                arr[a] = num
                a += 1
                b += 1
                mid += 1
                comparisons += 1
            
        return comparisons

    ################### INSERTION SORT ###################

    def insertionSort(self, arr, l, r):
        comparisons = 0
        start = timer() * 1000
        if(len(arr) <= 1):
            return 0,0
        for i in range(l + 1, r):
            for j in range (i, l, -1):
                if(arr[j] < arr[j - 1]):
                    comparisons += 1
                    self.swap(j, j -1, arr)
                else:
                    comparisons += 1
                    break
        end = timer() * 1000
        self.it += comparisons
        return end - start, comparisons

    ############## HELPER FUNCTIONS #############

    def shift(self, i, j, arr):
        for ind in range(j,i,-1):
            arr[ind] = arr[ind - 1]

    def applyMergeSort(self, arr):
        m = len(arr) - 1
        self.mergesort(0, len(arr) - 1, arr)

    def swap(self, i, j, arr):
        arr[i], arr[j] = arr[j], arr[i]
