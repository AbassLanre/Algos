def median(arr1,arr2):
    arr = arr1+arr2
    arr.sort()
    middle = int(len(arr)/2)
    if len(arr)%2 == 0:
        median = (arr[middle-1] + arr[middle])/2
    else:
        median = arr[middle]
    return median

print(median([1,3,3,5],[2,4,6]))