def three_sum(arr: list) -> list:
    arr.sort()
    n = len(arr)
    result = []
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                if arr[i] + arr[j] + arr[k] == 0 and [arr[i], arr[j], arr[k]] not in result:
                    result.append([arr[i], arr[j], arr[k]])
    return result


print(three_sum([-1,0,1,2,-1,-4]))
