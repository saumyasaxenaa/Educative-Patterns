def Solution(K, str):
    maxLength = 0
    windowStart = 0
    charFreq = {}
    for windowEnd in range(len(str)):
        leftchar = str[windowEnd]
        if leftchar not in charFreq:
            charFreq[leftchar] = 0
        charFreq[leftchar] += 1
        if len(charFreq) > K:
            rightchar = str[windowStart]
            charFreq[rightchar] += 1
            if charFreq[rightchar] == 0:
                del charFreq[rightchar]
            windowStart += 1
        maxLength = max(maxLength, windowEnd-windowStart+1)
    return maxLength
s = 'cbbebi'
k = 3
res = Solution(3,'cbbebi')
print(f'Longest Substring of length: {res}')