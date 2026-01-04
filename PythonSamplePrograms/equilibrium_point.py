def findEquilibrium(arr):
    # code here
    arr_sum = sum(arr)
    left_sum = arr[0]
    for i in range(1, len(arr)-1):
        if left_sum == arr_sum - left_sum - arr[i]:
            return i
        left_sum += arr[i]
    return -1