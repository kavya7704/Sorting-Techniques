def selectionSort(arr,n):
    Min = 0
    for i in range(0,n):
        Min = i
        for j in range(i+1,n):
            if arr[j] < arr[Min]:
                Min = j
        arr[i],arr[Min] = arr[Min],arr[i]
    return arr
print(selectionSort([9,2,5,1,6,2,8],7))
