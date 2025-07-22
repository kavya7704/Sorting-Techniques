def mergeSort(arr,n):
    low = 0
    high = n - 1
    
    def mS(arr,low,high):
        if low == high:
            return
        
        mid = (low + high) // 2
        
        mS(arr,low,mid)
        mS(arr,mid+1,high)
        Sort(arr,low,mid,high)

    def Sort(arr,low,mid,high):
        i = low
        j = mid + 1
        k = []
        while i <= mid and j <= high:
            if arr[i] <= arr[j]:
                k.append(arr[i])
                i += 1
            else:
                k.append(arr[j])
                j += 1
        while i <= mid:
            k.append(arr[i])
            i += 1
        while j <= high:
            k.append(arr[j])
            j += 1
        
        for ind,val in enumerate(k):
            arr[ind + low] = val

    mS(arr,low,high)
    return arr

nums = [9,2,5,1,6,2,8]
n = 7
print(mergeSort(nums,n))
