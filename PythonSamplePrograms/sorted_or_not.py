def sorted_or_not(arr: list) -> bool:
    ascending = True
    descending = True
    n = len(arr)

    for i in range(n-1):
        if arr[i] > arr[i+1]:
            ascending = False
        if arr[i] < arr[i+1]:
            descending = False
        if not ascending and not descending:
            return False
    return True


print(sorted_or_not([1,2,3,4,5,6]))
print(sorted_or_not([1,2,5,8,2,3]))
print(sorted_or_not([7,6,5,4,3,2,1]))
