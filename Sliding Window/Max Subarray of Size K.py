def Solution(K,arr):
    maxSum = 0
    windowStart, windowSum = 0,0
    for windowEnd in range(len(arr)):
        windowSum += arr[windowEnd]
        if windowEnd >= K-1:
            maxSum = max(windowSum, maxSum)
            windowSum -= arr[windowStart]
            windowStart += 1
    return maxSum

res = Solution(2,[2, 3, 4, 1, ])
print(f'Max sum of Subarrays:{res}')