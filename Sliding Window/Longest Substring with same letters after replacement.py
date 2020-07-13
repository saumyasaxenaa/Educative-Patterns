def Solution(str, K):
    maxLength = 0
    windowStart = 0
    maxRepeatingCount = 0
    frequency = {}
    for windowEnd in range(len(str)):
        rightChar = str[windowEnd]
        if rightChar not in frequency:
            frequency[rightChar] = 0
        frequency[rightChar] += 1
        maxRepeatingCount = max(maxRepeatingCount, frequency[rightChar])
        print(f'Max Repeating:{maxRepeatingCount}')
        print(f'The frequency count:{frequency}')
        if (windowEnd-windowStart+1-maxRepeatingCount) > K:
            print('Need to change the window')
            print(f'Start: {windowStart}, Stop: {windowEnd}')
            leftChar = str[windowStart]
            frequency[leftChar] -= 1
            windowStart += 1
            print(f'After changing the window: {frequency}')
        maxLength = max(maxLength, windowEnd-windowStart+1)
        print(f'Start:{windowStart}, Stop:{windowEnd}, MaxLength:{maxLength}')
    return maxLength
print(Solution('abccde',1))
