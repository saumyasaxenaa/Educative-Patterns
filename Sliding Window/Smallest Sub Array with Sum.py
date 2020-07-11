def Solution(s,arr):
    minLength = float('inf')
    windowStart, windowSum = 0,0
    for windowEnd in range(len(arr)):
        windowSum += arr[windowEnd]
        while windowSum >= s:
            minLength = min(minLength, windowEnd - windowStart+1)
            windowSum -= arr[windowStart]
            windowStart += 1
    return minLength

res = Solution(7,[2, 1, 5, 2, 8])
print(f'Smallest subarray:{res}')