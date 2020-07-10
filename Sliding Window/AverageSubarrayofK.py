def Solution(K, arr):
    result = []
    windowStart, windowSum = 0, 0.0
    for windowEnd in range(len(arr)):
        windowSum += arr[windowEnd]
        if windowEnd >= K-1:
            result.append(windowSum/K)
            windowSum -= arr[windowStart]
            windowStart += 1

    return result

res = Solution(5,[1, 3, 2, 6, -1, 4, 1, 8, 2])
print(f'The averages of subarrays:{res}')