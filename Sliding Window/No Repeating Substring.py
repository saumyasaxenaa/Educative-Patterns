def Solution(str):
    maxLength = 0
    count = {}
    windowStart = 0
    for windowEnd in range(len(str)):
        rightChar = str[windowEnd]
        if rightChar in count:
            print('Saw a Repeat!!!!!')
            windowStart = max(windowStart, count[rightChar]+1)
            print(f'Start: {windowStart}')
            print(f'Stop:{windowEnd}')
        count[rightChar] = windowEnd
        maxLength = max(maxLength, windowEnd-windowStart+1)
        print(f'Count: {count}')
        print(f'Start: {windowStart}, Stop:{windowEnd},Max Length: {maxLength}')
    return maxLength
print(Solution('aabccbb'))
