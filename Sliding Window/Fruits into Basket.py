def Solution(arr):
    maxCount = 0
    basket = {}
    windowStart = 0
    for windowEnd in range(len(arr)):
        rightChar = arr[windowEnd]
        if rightChar not in basket:
            basket[rightChar] = 0
        basket[rightChar] += 1
        while len(basket) > 2:
            leftChar = arr[windowStart]
            basket[leftChar] -= 1
            if basket[leftChar] == 0:
                del basket[leftChar]
            windowStart += 1
        maxCount = max(maxCount, windowEnd-windowStart+1)
    return maxCount

print(Solution(['A', 'B', 'C', 'B', 'B', 'C']))
