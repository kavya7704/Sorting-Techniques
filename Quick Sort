def quickSort(arr):
    def partition(arr,low,high):
        i = low
        j = high
        pivot = arr[low]
        while i < j:
            while arr[i] <= pivot and i < high:
                i += 1
            while arr[j] >= pivot and j > low:
                j -= 1
            if i < j:
                arr[i],arr[j] = arr[j],arr[i]
        arr[low],arr[j] = arr[j],arr[low]
        return j
    
    def qs(arr,low,high):
        if low < high:
            pInd = partition(arr,low,high)
            qs(arr,low,pInd-1)
            qs(arr,pInd+1,high)
    low = 0
    high = len(arr) - 1
    qs(arr,low,high)
    return arr

print(quickSort([9,2,5,1,6,2,8]))
