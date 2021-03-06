def Solution(str,pattern):
    windowStart = 0
    matched = 0
    frequency = {}

    for char in pattern:
        if char not in frequency:
            frequency[char] = 0
        frequency[char] += 1

    for windowEnd in range(len(str)):
        rightChar = str[windowEnd]
        if rightChar in frequency:
            frequency[rightChar] -= 1
            if frequency[rightChar] == 0:
                matched += 1
        if matched == len(frequency):
            return True
        if windowEnd >= len(pattern) - 1:
            leftChar = str[windowStart]
            windowStart += 1
            if leftChar in frequency:
                if frequency[leftChar] == 0:
                    matched -= 1
                frequency[leftChar] += 1
    return False

print(Solution('oidbcaf','abc'))
print(Solution('odicf','dc'))